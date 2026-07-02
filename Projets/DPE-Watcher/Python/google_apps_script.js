/**
 * Google Apps Script pour DPE Watcher
 * -----------------------------------
 * Ce script est à intégrer directement dans votre Google Sheet (Extensions > Apps Script).
 * Il sert d'API passerelle pour stocker l'historique des DPE et lister les DPE actifs.
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
  
  // 3. Charger tous les DPE déjà traités en mémoire pour comparaison ultra-rapide
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
      // DPE non traité -> C'est un nouveau !
      processedDpesMap[num] = true;
      newDpeList.push(dpe);
      
      // Ajouter à l'historique
      historyRowsToAdd.push([num, nowStr]);
      
      // Formater la date d'établissement
      var dateEtab = dpe.date_etablissement_dpe || "";
      if (dateEtab && dateEtab.indexOf("-") > -1) {
        var parts = dateEtab.split("-");
        dateEtab = parts[2] + "/" + parts[1] + "/" + parts[0]; // YYYY-MM-DD -> DD/MM/YYYY
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
  
  // 5. Insérer les lignes dans les feuilles (en masse pour de meilleures performances)
  if (historyRowsToAdd.length > 0) {
    sheetHistory.getRange(sheetHistory.getLastRow() + 1, 1, historyRowsToAdd.length, 2).setValues(historyRowsToAdd);
  }
  
  if (activeRowsToAdd.length > 0) {
    var startRow = sheetActifs.getLastRow() + 1;
    sheetActifs.getRange(startRow, 1, activeRowsToAdd.length, 10).setValues(activeRowsToAdd);
    
    // Appliquer un tri décroissant sur la date de récupération ou la date d'établissement
    // Pour que les plus récents soient toujours en haut de la liste visible
    var lastRow = sheetActifs.getLastRow();
    if (lastRow > 1) {
      sheetActifs.getRange(2, 1, lastRow - 1, 10).sort({column: 10, ascending: false}); // Tri par Date Récupération décroissante
    }
  }
  
  return {
    "success": true,
    "new_dpes": newDpeList
  };
}
