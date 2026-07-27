// État Global de l'Application
let targets = [];

// Initialisation au chargement du DOM
document.addEventListener('DOMContentLoaded', () => {
  loadInitialData();
  setupEventListeners();
  renderApp();
});

// Chargement des données (LocalStorage ou par défaut)
function loadInitialData() {
  const saved = localStorage.getItem('prospection_funnel_targets');
  if (saved) {
    try {
      targets = JSON.parse(saved);
    } catch (e) {
      console.error("Erreur de lecture du localStorage, chargement des données par défaut", e);
      targets = [...DEFAULT_TARGETS];
    }
  } else {
    targets = [...DEFAULT_TARGETS];
    saveToLocalStorage();
  }
}

function saveToLocalStorage() {
  localStorage.setItem('prospection_funnel_targets', JSON.stringify(targets));
}

// Configuration des Événements
function setupEventListeners() {
  // Navigation par Onglets
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
      
      const targetTab = e.currentTarget.getAttribute('data-tab');
      e.currentTarget.classList.add('active');
      document.getElementById(targetTab).classList.add('active');

      if (targetTab === 'analytics-view') renderAnalytics();
      if (targetTab === 'generator-view') populateGeneratorOptions();
    });
  });

  // Filtres & Recherche
  document.getElementById('search-input').addEventListener('input', renderApp);
  document.getElementById('filter-category').addEventListener('change', renderApp);
  document.getElementById('filter-location').addEventListener('change', renderApp);

  // Modales
  document.getElementById('btn-add-target').addEventListener('click', () => openModal());
  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.getElementById('modal-cancel').addEventListener('click', closeModal);
  document.getElementById('target-form').addEventListener('submit', handleFormSubmit);

  // Exporter JSON
  document.getElementById('btn-export-data').addEventListener('click', exportDataJSON);

  // Générateur
  document.getElementById('btn-generate-message').addEventListener('click', generateMessageText);
  document.getElementById('btn-copy-message').addEventListener('click', copyMessageToClipboard);
}

// Rendu Général
function renderApp() {
  const filtered = getFilteredTargets();
  renderKanban(filtered);
  renderTable(filtered);
  updateHeaderStats();
}

// Filtrage des données
function getFilteredTargets() {
  const query = document.getElementById('search-input').value.toLowerCase().trim();
  const category = document.getElementById('filter-category').value;
  const location = document.getElementById('filter-location').value;

  return targets.filter(item => {
    const matchesSearch = !query || 
      item.name.toLowerCase().includes(query) ||
      item.targetRole.toLowerCase().includes(query) ||
      item.pitch.toLowerCase().includes(query) ||
      item.location.toLowerCase().includes(query);

    const matchesCategory = category === 'ALL' || 
      (category === 'SportTech' ? item.category.includes('SportTech') : item.category === category);
    const matchesLocation = location === 'ALL' || item.location.includes(location);

    return matchesSearch && matchesCategory && matchesLocation;
  });
}

// Rendu du Kanban (Pipeline Visual)
function renderKanban(dataList) {
  const container = document.getElementById('kanban-board-container');
  container.innerHTML = '';

  STAGES.forEach(stage => {
    const columnData = dataList.filter(item => item.status === stage.id);
    
    const colEl = document.createElement('div');
    colEl.className = 'kanban-column';
    colEl.setAttribute('data-stage', stage.id);

    colEl.innerHTML = `
      <div class="column-header">
        <div class="column-title" style="color: ${stage.color}">
          ${stage.label}
        </div>
        <span class="column-badge">${columnData.length}</span>
      </div>
      <div class="cards-container" data-stage="${stage.id}">
        ${columnData.map(target => createCardHTML(target)).join('')}
      </div>
    `;

    container.appendChild(colEl);
  });

  setupDragAndDrop();
}

// Création HTML d'une Carte Kanban
function createCardHTML(target) {
  return `
    <div class="target-card" draggable="true" data-id="${target.id}">
      <div class="card-header">
        <div class="card-company">${target.name}</div>
        <div class="ice-tag">ICE ${target.iceScore}</div>
      </div>
      <div class="card-role">${target.targetRole}</div>
      <div class="card-meta">
        <div class="meta-row">📍 ${target.location}</div>
        <div class="meta-row">👤 ${target.contactPerson || 'À définir'}</div>
      </div>
      <div class="card-pitch">"${target.pitch}"</div>
      <div class="card-footer">
        <span style="font-size: 11px; color: var(--text-muted);">Action: ${target.nextActionDate || 'Non définie'}</span>
        <div class="card-actions">
          <button class="icon-btn" onclick="editTarget('${target.id}')" title="Éditer">✏️</button>
          <button class="icon-btn" onclick="deleteTarget('${target.id}')" title="Supprimer">🗑️</button>
        </div>
      </div>
    </div>
  `;
}

// Configuration Drag & Drop
function setupDragAndDrop() {
  const cards = document.querySelectorAll('.target-card');
  const containers = document.querySelectorAll('.cards-container');

  cards.forEach(card => {
    card.addEventListener('dragstart', (e) => {
      card.classList.add('dragging');
      e.dataTransfer.setData('text/plain', card.getAttribute('data-id'));
    });

    card.addEventListener('dragend', () => {
      card.classList.remove('dragging');
    });
  });

  containers.forEach(container => {
    container.addEventListener('dragover', (e) => {
      e.preventDefault();
      container.classList.add('drag-over');
    });

    container.addEventListener('dragleave', () => {
      container.classList.remove('drag-over');
    });

    container.addEventListener('drop', (e) => {
      e.preventDefault();
      container.classList.remove('drag-over');
      const targetId = e.dataTransfer.getData('text/plain');
      const newStage = container.getAttribute('data-stage');

      updateTargetStatus(targetId, newStage);
    });
  });
}

// Mise à jour du Statut d'une Cible
function updateTargetStatus(targetId, newStatus) {
  const index = targets.findIndex(t => t.id === targetId);
  if (index !== -1) {
    targets[index].status = newStatus;
    targets[index].lastContact = new Date().toISOString().split('T')[0];
    saveToLocalStorage();
    renderApp();
  }
}

// Rendu du Tableau CRM
function renderTable(dataList) {
  const tbody = document.getElementById('table-body');
  tbody.innerHTML = '';

  dataList.forEach(item => {
    const tr = document.createElement('tr');
    const stageObj = STAGES.find(s => s.id === item.status) || STAGES[0];

    tr.innerHTML = `
      <td><strong>${item.name}</strong></td>
      <td>${item.category}</td>
      <td>${item.location}</td>
      <td>${item.targetRole}</td>
      <td><span class="ice-tag">ICE ${item.iceScore}</span></td>
      <td>
        <span class="badge" style="background: ${stageObj.color}20; color: ${stageObj.color}; border: 1px solid ${stageObj.color}50;">
          ${stageObj.label}
        </span>
      </td>
      <td>${item.nextActionDate || '-'}</td>
      <td>
        <button class="icon-btn" onclick="editTarget('${item.id}')">✏️</button>
        <button class="icon-btn" onclick="deleteTarget('${item.id}')">🗑️</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

// Statistiques d'en-tête
function updateHeaderStats() {
  document.getElementById('stat-total-count').textContent = targets.length;
  
  const avgIce = targets.length > 0 
    ? (targets.reduce((acc, curr) => acc + (parseFloat(curr.iceScore) || 0), 0) / targets.length).toFixed(1)
    : '0.0';
  document.getElementById('stat-avg-ice').textContent = avgIce;

  const pending = targets.filter(t => t.status === 'A contacter' || t.status === 'Échange / Relance').length;
  document.getElementById('stat-actions-pending').textContent = pending;
}

// Rendu des Analytics
function renderAnalytics() {
  const total = targets.length;
  if (total === 0) return;

  const inDiscussion = targets.filter(t => t.status === 'Échange / Relance').length;
  const interviews = targets.filter(t => t.status === 'Entretien' || t.status === 'Proposition').length;
  const contacted = targets.filter(t => t.status !== 'A contacter').length;
  const highIce = targets.filter(t => parseFloat(t.iceScore) >= 9.0).length;

  const responseRate = contacted > 0 ? Math.round(((inDiscussion + interviews) / contacted) * 100) : 0;

  document.getElementById('analytic-response-rate').textContent = `${responseRate}%`;
  document.getElementById('analytic-interviews-count').textContent = interviews;
  document.getElementById('analytic-high-ice-count').textContent = highIce;
  document.getElementById('analytic-in-discussion').textContent = inDiscussion;

  // Visualisation des barres du Funnel
  const barsContainer = document.getElementById('funnel-bars-container');
  barsContainer.innerHTML = '';

  STAGES.forEach(stage => {
    const count = targets.filter(t => t.status === stage.id).length;
    const percentage = Math.round((count / total) * 100);

    const barWrapper = document.createElement('div');
    barWrapper.className = 'funnel-bar-wrapper';
    barWrapper.innerHTML = `
      <div class="funnel-bar-header">
        <span>${stage.label}</span>
        <span><strong>${count}</strong> cibles (${percentage}%)</span>
      </div>
      <div class="funnel-bar-bg">
        <div class="funnel-bar-fill" style="width: ${percentage}%; background: ${stage.color}"></div>
      </div>
    `;
    barsContainer.appendChild(barWrapper);
  });
}

// Générateur de Message
function populateGeneratorOptions() {
  const select = document.getElementById('generator-target-select');
  select.innerHTML = targets.map(t => `<option value="${t.id}">${t.name} (${t.targetRole})</option>`).join('');
}

function generateMessageText() {
  const targetId = document.getElementById('generator-target-select').value;
  const canal = document.getElementById('generator-canal-select').value;
  const target = targets.find(t => t.id === targetId);

  if (!target) return;

  const contact = target.contactPerson || 'Bonjour';
  let message = '';

  if (canal === 'linkedin') {
    message = `Bonjour ${contact},\n\nJ'ai suivi avec beaucoup d'intérêt l'évolution de ${target.name} sur le secteur ${target.category}.\n\nFort de 15 ans d'expérience sur le terrain (management opérationnel & conduite de projets digitaux), j'accompagne les équipes pour réussir l'implémentation du rôle de ${target.targetRole}.\n\nVoici ce que je peux apporter immédiatement : ${target.pitch}\n\nSeriez-vous ouvert à un échange informel de 10 minutes cette semaine ?\n\nBien cordialement,`;
  } else if (canal === 'email') {
    message = `Objet : Candidature spontanée / Échange stratégique - ${target.targetRole} - ${target.name}\n\nBonjour ${contact},\n\nJe vous contacte directement au sujet des opportunités de déploiement et d'accompagnement client chez ${target.name}.\n\n${target.pitch}\n\nMon parcours me permet d'aligner la réalité du terrain avec les exigences d'un outil SaaS performant. Je serais ravi de vous présenter mon approche lors d'un bref entretien téléphonique.\n\nDans l'attente de votre retour,\n\nBien à vous,`;
  } else {
    message = `Bonjour ${contact},\n\nJe me permets de revenir vers vous suite à mon précédent message concernant le rôle de ${target.targetRole} chez ${target.name}.\n\nPour rappel : ${target.pitch}\n\nAvez-vous eu l'opportunité de consulter mon profil ?\n\nExcellente journée,`;
  }

  document.getElementById('generator-message-output').textContent = message;
  document.getElementById('generator-preview-title').textContent = `Accroche pour ${target.name} (${canal.toUpperCase()})`;
}

function copyMessageToClipboard() {
  const text = document.getElementById('generator-message-output').textContent;
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.getElementById('btn-copy-message');
    btn.textContent = '✅ Copié !';
    setTimeout(() => btn.textContent = '📋 Copier le texte', 2000);
  });
}

// Modal Formulaire
function openModal(editId = null) {
  const modal = document.getElementById('target-modal');
  const form = document.getElementById('target-form');
  form.reset();

  if (editId) {
    const target = targets.find(t => t.id === editId);
    if (target) {
      document.getElementById('modal-title').textContent = `Éditer la cible : ${target.name}`;
      document.getElementById('form-target-id').value = target.id;
      document.getElementById('form-name').value = target.name;
      document.getElementById('form-category').value = target.category;
      document.getElementById('form-role').value = target.targetRole;
      document.getElementById('form-location').value = target.location;
      document.getElementById('form-ice').value = target.iceScore;
      document.getElementById('form-status').value = target.status;
      document.getElementById('form-contact').value = target.contactPerson || '';
      document.getElementById('form-pitch').value = target.pitch || '';
      document.getElementById('form-notes').value = target.notes || '';
    }
  } else {
    document.getElementById('modal-title').textContent = 'Ajouter une Nouvelle Cible';
    document.getElementById('form-target-id').value = '';
  }

  modal.classList.add('active');
}

function closeModal() {
  document.getElementById('target-modal').classList.remove('active');
}

function handleFormSubmit(e) {
  e.preventDefault();
  const editId = document.getElementById('form-target-id').value;

  const targetData = {
    id: editId || `target-${Date.now()}`,
    name: document.getElementById('form-name').value,
    category: document.getElementById('form-category').value,
    targetRole: document.getElementById('form-role').value,
    location: document.getElementById('form-location').value,
    iceScore: parseFloat(document.getElementById('form-ice').value) || 8.0,
    status: document.getElementById('form-status').value,
    contactPerson: document.getElementById('form-contact').value,
    pitch: document.getElementById('form-pitch').value,
    notes: document.getElementById('form-notes').value,
    lastContact: editId ? (targets.find(t => t.id === editId)?.lastContact || '') : '',
    nextActionDate: new Date(Date.now() + 3*86400000).toISOString().split('T')[0]
  };

  if (editId) {
    const idx = targets.findIndex(t => t.id === editId);
    if (idx !== -1) targets[idx] = targetData;
  } else {
    targets.unshift(targetData);
  }

  saveToLocalStorage();
  closeModal();
  renderApp();
}

window.editTarget = function(id) {
  openModal(id);
};

window.deleteTarget = function(id) {
  if (confirm("Voulez-vous vraiment supprimer cette cible du funnel ?")) {
    targets = targets.filter(t => t.id !== id);
    saveToLocalStorage();
    renderApp();
  }
};

// Export JSON
function exportDataJSON() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(targets, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", `Prospection_Funnel_Export_${new Date().toISOString().split('T')[0]}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
}
