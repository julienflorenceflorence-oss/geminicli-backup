/**
 * Google Apps Script pour DPE Watcher Premium
 * -------------------------------------------
 * Ce script gère la base de données DPE (Historique, DPE Actifs) et génère
 * automatiquement un Dashboard d'analyse de la classification sous charte Prestige.
 */

function doPost(e) {
  try {
    var requestData = JSON.parse(e.postData.contents);
    var action = requestData.action;
    
    if (action === "check_and_add") {
      var result = handleCheckAndAdd(requestData.dpes);
      return ContentService.createTextOutput(JSON.stringify(result))
                           .setMimeType(ContentService.MimeType.JSON);
    } else {
      return ContentService.createTextOutput(JSON.stringify({ "error": "Action inconnue" }))
                           .setMimeType(ContentService.MimeType.JSON);
    }
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ "error": error.toString() }))
                         .setMimeType(ContentService.MimeType.JSON);
  }
}

function handleCheckAndAdd(dpes) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // 1. Obtenir ou créer l'onglet "Historique" (déduplication)
  var sheetHistory = ss.getSheetByName("Historique");
  if (!sheetHistory) {
    sheetHistory = ss.insertSheet("Historique");
    sheetHistory.appendRow(["numero_dpe", "date_recup"]);
    sheetHistory.getRange(1, 1, 1, 2).setFontWeight("bold").setBackground("#0F1115").setFontColor("#D4AF37");
  }
  
  // 2. Obtenir ou créer l'onglet "DPE_Actifs" (consultation utilisateur)
  var sheetActifs = ss.getSheetByName("DPE_Actifs");
  if (!sheetActifs) {
    sheetActifs = ss.insertSheet("DPE_Actifs");
    sheetActifs.appendRow([
      "Commune", "Adresse", "Code Postal", "Date Établissement", 
      "N° DPE", "Type Bâtiment", "Classe DPE", "Période Construction", "Surface Habitable (m²)", "Date Récupération"
    ]);
    sheetActifs.getRange(1, 1, 1, 10).setFontWeight("bold").setBackground("#0F1115").setFontColor("#D4AF37");
    sheetActifs.setFrozenRows(1);
  }
  
  // 3. Charger tous les DPE déjà traités en mémoire
  var historyLastRow = sheetHistory.getLastRow();
  var processedDpesMap = {};
  if (historyLastRow > 1) {
    var historyValues = sheetHistory.getRange(2, 1, historyLastRow - 1, 1).getValues();
    for (var i = 0; i < historyValues.length; i++) {
      var numDpe = historyValues[i][0].toString().trim();
      if (numDpe) {
        processedDpesMap[numDpe] = true;
      }
    }
  }
  
  var newDpeList = [];
  var historyRowsToAdd = [];
  var activeRowsToAdd = [];
  var nowStr = Utilities.formatDate(new Date(), "Europe/Paris", "dd/MM/yyyy HH:mm:ss");
  
  // 4. Parcourir les DPE envoyés
  for (var j = 0; j < dpes.length; j++) {
    var dpe = dpes[j];
    var num = dpe.numero_dpe ? dpe.numero_dpe.toString().trim() : "";
    
    if (num && !processedDpesMap[num]) {
      processedDpesMap[num] = true;
      newDpeList.push(dpe);
      
      // Ajouter à l'historique
      historyRowsToAdd.push([num, nowStr]);
      
      // Formater la date d'établissement
      var dateEtab = dpe.date_etablissement_dpe || "";
      if (dateEtab && dateEtab.indexOf("-") > -1) {
        var parts = dateEtab.split("-");
        dateEtab = parts[2] + "/" + parts[1] + "/" + parts[0];
      }
      
      // Ajouter à l'onglet actif
      activeRowsToAdd.push([
        dpe.nom_commune_brut || "",
        dpe.adresse_brut || "",
        dpe.code_postal_brut || "",
        dateEtab,
        num,
        dpe.type_batiment || "",
        dpe.etiquette_dpe || "",
        dpe.periode_construction || "",
        dpe.surface_habitable_logement || "",
        nowStr
      ]);
    }
  }
  
  // 5. Insérer les lignes
  if (historyRowsToAdd.length > 0) {
    sheetHistory.getRange(sheetHistory.getLastRow() + 1, 1, historyRowsToAdd.length, 2).setValues(historyRowsToAdd);
  }
  
  if (activeRowsToAdd.length > 0) {
    var startRow = sheetActifs.getLastRow() + 1;
    sheetActifs.getRange(startRow, 1, activeRowsToAdd.length, 10).setValues(activeRowsToAdd);
    
    var lastRow = sheetActifs.getLastRow();
    if (lastRow > 1) {
      sheetActifs.getRange(2, 1, lastRow - 1, 10).sort({column: 10, ascending: false});
    }
  }
  
  // 6. Mettre à jour ou créer l'onglet "Dashboard"
  generateDashboard(ss);
  
  return {
    "success": true,
    "new_dpes": newDpeList
  };
}

function generateDashboard(ss) {
  var sheetDash = ss.getSheetByName("Dashboard");
  if (!sheetDash) {
    sheetDash = ss.insertSheet("Dashboard", 0); // Placer en premier onglet
  }
  
  // Désactiver le quadrillage pour un rendu plus épuré (Prestige)
  sheetDash.setGridlines(false);
  
  // 1. En-tête Titre
  sheetDash.getRange("A1:K1").merge().setValue("VEILLE STRATÉGIQUE DPE & PASSOIRES THERMIQUES")
           .setFontWeight("bold").setFontSize(16).setFontColor("#D4AF37")
           .setBackground("#0F1115").setHorizontalAlignment("center").setVerticalAlignment("middle");
  sheetDash.setRowHeight(1, 50);
  
  // 2. Encadré Informations Réglementaires
  sheetDash.getRange("B3:J3").merge().setValue("CALENDRIER DES INTERDICTIONS DE LOUER (LOI CLIMAT & RÉSILIENCE)")
           .setFontWeight("bold").setFontSize(10).setFontColor("#0F1115").setBackground("#E5E7EB")
           .setHorizontalAlignment("center");
           
  var rulesData = [
    ["Classe G", "Interdiction totale depuis le 01/01/2025", "Statut : DÉJÀ INTERDIT à la location (nouveau bail/renouvellement)"],
    ["Classe F", "Interdiction à partir du 01/01/2028", "Statut : PROCHAINE ÉCHÉANCE (dans 1 an et demi) - PRIORITÉ PROSPECTION"],
    ["Classe E", "Interdiction à partir du 01/01/2034", "Statut : AUTORISÉ POUR L'INSTANT"]
  ];
  sheetDash.getRange("B4:D6").setValues(rulesData);
  sheetDash.getRange("B4:B6").setFontWeight("bold").setHorizontalAlignment("center");
  sheetDash.getRange("B4:D6").setBorder(true, true, true, true, true, true, "#E5E7EB", SpreadsheetApp.BorderStyle.SOLID);
  
  // Colorer les statuts réglementaires
  sheetDash.getRange("D4").setFontColor("#DC2626").setFontWeight("bold"); // Rouge pour G
  sheetDash.getRange("D5").setFontColor("#D97706").setFontWeight("bold"); // Orange pour F
  sheetDash.getRange("D6").setFontColor("#2563EB").setFontWeight("bold"); // Bleu pour E

  // 3. Section des KPIs de Prospection (Chiffres clés)
  sheetDash.getRange("B8:J8").merge().setValue("INDICATEURS CLÉS - PARC DPE IDENTIFIÉ")
           .setFontWeight("bold").setFontSize(11).setFontColor("#D4AF37").setBackground("#0F1115")
           .setHorizontalAlignment("center");
  sheetDash.setRowHeight(8, 25);
  
  // Formules dynamiques calculant les volumes sur DPE_Actifs
  var kpiTitles = [
    ["DPE Analysés (Total)", "Passoires Thermiques (F & G)", "Classe G (Déjà Interdits)", "Classe F (Interdits 2028)", "Classe E (Interdits 2034)"]
  ];
  sheetDash.getRange("B9:F9").setValues(kpiTitles).setFontWeight("bold").setBackground("#F3F4F6").setHorizontalAlignment("center");
  
  var kpiFormulas = [
    [
      '=NBVAL(DPE_Actifs!E2:E)', 
      '=COUNTIF(DPE_Actifs!G2:G; "F") + COUNTIF(DPE_Actifs!G2:G; "G")', 
      '=COUNTIF(DPE_Actifs!G2:G; "G")', 
      '=COUNTIF(DPE_Actifs!G2:G; "F")', 
      '=COUNTIF(DPE_Actifs!G2:G; "E")'
    ]
  ];
  
  sheetDash.getRange("B10:F10").setFormulas(kpiFormulas).setFontSize(14).setFontWeight("bold").setHorizontalAlignment("center");
  sheetDash.getRange("B9:F10").setBorder(true, true, true, true, true, true, "#E5E7EB", SpreadsheetApp.BorderStyle.SOLID);
  
  // Style sur les valeurs KPI
  sheetDash.getRange("B10").setFontColor("#1F2937"); // Noir
  sheetDash.getRange("C10").setFontColor("#DC2626"); // Rouge (Total F+G)
  sheetDash.getRange("D10").setFontColor("#DC2626"); // Rouge (G)
  sheetDash.getRange("E10").setFontColor("#D97706"); // Orange (F)
  sheetDash.getRange("F10").setFontColor("#2563EB"); // Bleu (E)

  // 4. Section Tableau Répartition Complète A-G
  sheetDash.getRange("B12:C12").merge().setValue("RÉPARTITION DPE A-G").setFontWeight("bold").setBackground("#E5E7EB").setHorizontalAlignment("center");
  var labels = [["A"], ["B"], ["C"], ["D"], ["E"], ["F"], ["G"]];
  sheetDash.getRange("B13:B19").setValues(labels).setFontWeight("bold").setHorizontalAlignment("center");
  
  var distributionFormulas = [
    ['=COUNTIF(DPE_Actifs!G2:G; "A")'],
    ['=COUNTIF(DPE_Actifs!G2:G; "B")'],
    ['=COUNTIF(DPE_Actifs!G2:G; "C")'],
    ['=COUNTIF(DPE_Actifs!G2:G; "D")'],
    ['=COUNTIF(DPE_Actifs!G2:G; "E")'],
    ['=COUNTIF(DPE_Actifs!G2:G; "F")'],
    ['=COUNTIF(DPE_Actifs!G2:G; "G")']
  ];
  sheetDash.getRange("C13:C19").setFormulas(distributionFormulas).setHorizontalAlignment("center");
  sheetDash.getRange("B12:C19").setBorder(true, true, true, true, true, true, "#E5E7EB", SpreadsheetApp.BorderStyle.SOLID);

  // 5. Générer le graphique s'il n'existe pas déjà
  var charts = sheetDash.getCharts();
  if (charts.length === 0) {
    var chart = sheetDash.newChart()
        .setChartType(Charts.ChartType.COLUMN)
        .addRange(sheetDash.getRange("B12:C19"))
        .setPosition(12, 5, 1, 1)
        .setOption('title', 'Répartition des Classes Énergétiques')
        .setOption('colors', ['#D4AF37']) // Couleur Or Prestige
        .setOption('legend', {position: 'none'})
        .setOption('vAxis', {title: 'Nombre de logements'})
        .setOption('hAxis', {title: 'Classe DPE'})
        .build();
    sheetDash.insertChart(chart);
  }

  // Ajustement des colonnes pour le dashboard
  sheetDash.setColumnWidth(1, 30);  // Marge gauche
  sheetDash.setColumnWidth(2, 180); // Classe / Label
  sheetDash.setColumnWidth(3, 260); // Valeur / Formule
  sheetDash.setColumnWidth(4, 380); // Statut / Description
}
