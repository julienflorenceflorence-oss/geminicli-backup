/**
 * iCloud Email Studio — GitHub Design System
 * Application Logic & HTML Email Rendering Engine
 */

document.addEventListener("DOMContentLoaded", () => {
    // UI Elements
    const selectTemplate = document.getElementById("select-template");
    const markdownInput = document.getElementById("markdown-input");
    const emailSubjectInput = document.getElementById("email-subject");
    const renderedOutput = document.getElementById("email-rendered-output");
    const mockupSubjectDisplay = document.getElementById("mockup-subject-display");
    const charCountDisplay = document.getElementById("char-count");
    
    // Actions & Buttons
    const btnCopyRich = document.getElementById("btn-copy-rich");
    const btnDownloadHtml = document.getElementById("btn-download-html");
    const btnCopyRawHtml = document.getElementById("btn-copy-raw-html");
    const btnCopyCli = document.getElementById("btn-copy-cli");
    const btnIcloudGuide = document.getElementById("btn-icloud-guide");
    
    // Modal & Toast
    const modalIcloud = document.getElementById("modal-icloud");
    const btnCloseModal = document.getElementById("btn-close-modal");
    const btnCloseModalFooter = document.getElementById("btn-close-modal-footer");
    const toast = document.getElementById("toast-notification");
    const toastMessage = document.getElementById("toast-message");

    // Component Buttons
    const componentButtons = document.querySelectorAll(".component-btn");
    const themeButtons = document.querySelectorAll(".theme-btn");
    const tabButtons = document.querySelectorAll(".tab-btn");

    let templatesData = [];

    // 1. INITIALIZATION & TEMPLATES LOADING
    async function initApp() {
        try {
            const response = await fetch("../Data/templates.json");
            if (response.ok) {
                templatesData = await response.json();
                populateTemplateDropdown();
            } else {
                throw new Error("Local JSON not loaded");
            }
        } catch (e) {
            console.warn("Using fallback preset templates data.");
            templatesData = getFallbackTemplates();
            populateTemplateDropdown();
        }

        // Load first template by default
        if (templatesData.length > 0) {
            loadTemplate(templatesData[0].id);
        }

        attachEventListeners();
        renderEmailContent();
    }

    function populateTemplateDropdown() {
        selectTemplate.innerHTML = templatesData.map(t => `<option value="${t.id}">${t.title} (${t.category})</option>`).join("");
    }

    function loadTemplate(templateId) {
        const found = templatesData.find(t => t.id === templateId);
        if (found) {
            markdownInput.value = found.markdown;
            emailSubjectInput.value = found.title;
            mockupSubjectDisplay.textContent = found.title;
            renderEmailContent();
        }
    }

    // 2. GITHUB FLAVORED MARKDOWN & ALERTS RENDERER
    function renderEmailContent() {
        const rawMarkdown = markdownInput.value;
        charCountDisplay.textContent = `${rawMarkdown.length} caractères`;
        mockupSubjectDisplay.textContent = emailSubjectInput.value || "Sans objet";

        let htmlContent = "";

        if (window.marked) {
            htmlContent = window.marked.parse(rawMarkdown);
        } else {
            htmlContent = simpleMarkdownFallback(rawMarkdown);
        }

        // Parse GitHub Alert Block callouts (> [!NOTE], > [!TIP], > [!IMPORTANT], > [!WARNING])
        htmlContent = parseGitHubAlerts(htmlContent);

        // Parse Inline Badges (`TEXT`)
        htmlContent = parseBadges(htmlContent);

        // Inject into DOM preview container
        renderedOutput.innerHTML = htmlContent;
        updateCliCommandPreview();
    }

    function parseGitHubAlerts(html) {
        // Replace blockquotes containing [!NOTE], [!TIP], [!IMPORTANT], [!WARNING]
        const alertTypes = {
            "NOTE": { class: "alert-note", title: "Note", icon: "ℹ️" },
            "TIP": { class: "alert-tip", title: "Conseil", icon: "💡" },
            "IMPORTANT": { class: "alert-important", title: "Important", icon: "⚠️" },
            "WARNING": { class: "alert-warning", title: "Attention", icon: "🔔" }
        };

        return html.replace(/<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING)\][\s\S]*?<\/blockquote>/gi, (match, type) => {
            const config = alertTypes[type.toUpperCase()] || alertTypes["NOTE"];
            // Extract text after [!TYPE]
            let innerText = match.replace(/<blockquote>\s*<p>\s*\[!(NOTE|TIP|IMPORTANT|WARNING)\]/i, "").replace(/<\/p>\s*<\/blockquote>/i, "");
            
            return `
                <div class="github-alert ${config.class}">
                    <div class="github-alert-title">${config.icon} ${config.title}</div>
                    <div>${innerText}</div>
                </div>
            `;
        });
    }

    function parseBadges(html) {
        // Convert inline code tags `TEXT` to GitHub Badges inside headers/tables
        return html.replace(/<code>(.*?)<\/code>/g, '<span class="github-badge">$1</span>');
    }

    // 3. CSS INLINER FOR EMAIL CLIENT COMPATIBILITY (Apple Mail / iCloud Mail)
    function generateInlinedHtml() {
        const isDark = renderedOutput.classList.contains("github-dark-preview");

        const themeBg = isDark ? "#0d1117" : "#ffffff";
        const themeText = isDark ? "#c9d1d9" : "#24292f";
        const themeHeaderColor = isDark ? "#f0f6fc" : "#1f2328";
        const themeBorder = isDark ? "#30363d" : "#d0d7de";
        const themeTableHeaderBg = isDark ? "#161b22" : "#f6f8fa";

        // Duplicate preview nodes & inject explicit style="" attributes
        const container = document.createElement("div");
        container.style.cssText = `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6; color: ${themeText}; background-color: ${themeBg}; padding: 24px; border-radius: 8px;`;

        // Clone rendered content
        container.innerHTML = renderedOutput.innerHTML;

        // Apply inline styles to headings
        container.querySelectorAll("h1").forEach(h1 => {
            h1.style.cssText = `font-size: 20px; font-weight: 600; color: ${themeHeaderColor}; border-bottom: 1px solid ${themeBorder}; padding-bottom: 8px; margin-top: 24px; margin-bottom: 16px;`;
        });

        container.querySelectorAll("h2, h3").forEach(h => {
            h.style.cssText = `font-size: 16px; font-weight: 600; color: ${themeHeaderColor}; margin-top: 20px; margin-bottom: 12px;`;
        });

        // Apply inline styles to tables
        container.querySelectorAll("table").forEach(table => {
            table.style.cssText = `border-collapse: collapse; width: 100%; margin: 16px 0; border: 1px solid ${themeBorder};`;
        });

        container.querySelectorAll("th").forEach(th => {
            th.style.cssText = `background-color: ${themeTableHeaderBg}; font-weight: 600; padding: 8px 12px; border: 1px solid ${themeBorder}; text-align: left; color: ${themeHeaderColor};`;
        });

        container.querySelectorAll("td").forEach(td => {
            td.style.cssText = `padding: 8px 12px; border: 1px solid ${themeBorder}; text-align: left; color: ${themeText};`;
        });

        // Apply inline styles to GitHub Alerts
        container.querySelectorAll(".github-alert").forEach(alert => {
            let bg = isDark ? "rgba(56, 139, 253, 0.15)" : "#ddf4ff";
            let border = "#388bfd";
            let color = isDark ? "#58a6ff" : "#0969da";

            if (alert.classList.contains("alert-tip")) {
                bg = isDark ? "rgba(63, 185, 80, 0.15)" : "#dafbe1";
                border = "#3fb950";
                color = isDark ? "#3fb950" : "#1a7f37";
            } else if (alert.classList.contains("alert-important")) {
                bg = isDark ? "rgba(163, 113, 247, 0.15)" : "#f0e6ff";
                border = "#a371f7";
                color = isDark ? "#a371f7" : "#8250df";
            } else if (alert.classList.contains("alert-warning")) {
                bg = isDark ? "rgba(210, 153, 34, 0.15)" : "#fff8c5";
                border = "#d29922";
                color = isDark ? "#d29922" : "#9a6700";
            }

            alert.style.cssText = `padding: 12px 16px; margin: 16px 0; border-left: 4px solid ${border}; background-color: ${bg}; color: ${color}; border-radius: 6px; font-size: 13.5px;`;
        });

        // Apply inline styles to Badges
        container.querySelectorAll(".github-badge").forEach(badge => {
            badge.style.cssText = `display: inline-block; padding: 2px 8px; font-size: 11px; font-weight: 600; border-radius: 12px; background-color: ${isDark ? "#21262d" : "#f6f8fa"}; border: 1px solid ${themeBorder}; color: ${themeText};`;
        });

        // Apply inline styles to CTA Buttons
        container.querySelectorAll(".github-btn-cta").forEach(btn => {
            btn.style.cssText = `display: inline-block; background-color: #2ea44f; color: #ffffff !important; font-weight: 600; padding: 10px 20px; border-radius: 6px; text-decoration: none; margin: 16px 0;`;
        });

        return container.outerHTML;
    }

    // 4. CLIPBOARD & EXPORT ACTIONS
    async function copyRichTextToClipboard() {
        const inlinedHtml = generateInlinedHtml();
        const plainText = markdownInput.value;

        try {
            if (navigator.clipboard && window.ClipboardItem) {
                const blobHtml = new Blob([inlinedHtml], { type: "text/html" });
                const blobText = new Blob([plainText], { type: "text/plain" });

                await navigator.clipboard.write([
                    new ClipboardItem({
                        "text/html": blobHtml,
                        "text/plain": blobText
                    })
                ]);
                showToast("Prêt pour Apple Mail ! Collez simplement (Cmd + V) dans votre email.");
            } else {
                fallbackCopyText(inlinedHtml);
                showToast("Code HTML copié dans le presse-papier !");
            }
        } catch (err) {
            console.error("Clipboard write error:", err);
            fallbackCopyText(inlinedHtml);
            showToast("HTML copié dans le presse-papier.");
        }
    }

    function downloadHtmlFile() {
        const inlinedHtml = `<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>${emailSubjectInput.value || "Email"}</title>
</head>
<body style="margin:0; padding:20px; background-color: #0d1117;">
${generateInlinedHtml()}
</body>
</html>`;

        const blob = new Blob([inlinedHtml], { type: "text/html" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `email_template_${Date.now()}.html`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        showToast("Fichier .HTML téléchargé !");
    }

    function fallbackCopyText(text) {
        const textarea = document.createElement("textarea");
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand("copy");
        document.body.removeChild(textarea);
    }

    function updateCliCommandPreview() {
        const recipient = document.getElementById("smtp-recipient").value || "destinataire@exemple.com";
        const subject = emailSubjectInput.value || "Sujet";
        const cliPreview = document.getElementById("cli-command-preview");
        if (cliPreview) {
            cliPreview.textContent = `python3 ../Python/send_icloud_email.py --to "${recipient}" --subject "${subject}"`;
        }
    }

    // 5. EVENT LISTENERS & HANDLERS
    function attachEventListeners() {
        selectTemplate.addEventListener("change", (e) => loadTemplate(e.target.value));
        markdownInput.addEventListener("input", renderEmailContent);
        emailSubjectInput.addEventListener("input", renderEmailContent);
        document.getElementById("smtp-recipient").addEventListener("input", updateCliCommandPreview);

        btnCopyRich.addEventListener("click", copyRichTextToClipboard);
        btnDownloadHtml.addEventListener("click", downloadHtmlFile);
        btnCopyRawHtml.addEventListener("click", () => {
            fallbackCopyText(generateInlinedHtml());
            showToast("HTML Brut copié !");
        });

        btnCopyCli.addEventListener("click", () => {
            const cliText = document.getElementById("cli-command-preview").textContent;
            fallbackCopyText(cliText);
            showToast("Commande Terminal copiée !");
        });

        // Modal Controls
        btnIcloudGuide.addEventListener("click", () => modalIcloud.classList.add("active"));
        btnCloseModal.addEventListener("click", () => modalIcloud.classList.remove("active"));
        btnCloseModalFooter.addEventListener("click", () => modalIcloud.classList.remove("active"));

        // Component Injectors
        componentButtons.forEach(btn => {
            btn.addEventListener("click", () => {
                const action = btn.dataset.action;
                insertComponentSnippet(action);
            });
        });

        // Theme Switcher Controls
        themeButtons.forEach(btn => {
            btn.addEventListener("click", () => {
                themeButtons.forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                const theme = btn.dataset.theme;

                renderedOutput.classList.remove("github-dark-preview", "apple-mail-preview");
                if (theme === "dark") {
                    renderedOutput.classList.add("github-dark-preview");
                } else if (theme === "email-client") {
                    renderedOutput.classList.add("apple-mail-preview");
                }
            });
        });

        // Tab Switcher
        tabButtons.forEach(tab => {
            tab.addEventListener("click", () => {
                tabButtons.forEach(t => t.classList.remove("active"));
                tab.classList.add("active");

                document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));
                const targetId = `tab-content-${tab.dataset.tab}`;
                document.getElementById(targetId).classList.add("active");
            });
        });
    }

    function insertComponentSnippet(action) {
        const snippets = {
            "alert-note": "\n> [!NOTE]\n> **Titre de la Note** : Saisissez votre texte de précision ici.\n\n",
            "alert-tip": "\n> [!TIP]\n> **Conseil** : Optimisation recommandée pour cette étape.\n\n",
            "alert-important": "\n> [!IMPORTANT]\n> **Point Majeur** : Action requise avant validation.\n\n",
            "alert-warning": "\n> [!WARNING]\n> **Avertissement** : Attention aux échéances à venir.\n\n",
            "badge": " `STATUT_ACTIF` ",
            "table": "\n| Colonne 1 | Colonne 2 | Statut |\n| :--- | :--- | :--- |\n| Élément A | Description A | `VALIDÉ` |\n| Élément B | Description B | `EN COURS` |\n\n",
            "cta-button": "\n[Accéder au Projet sur GitHub](https://github.com)\n\n",
            "code-block": "\n```bash\npython3 send_icloud_email.py --to recipient@domain.com\n```\n\n"
        };

        const snippet = snippets[action] || "";
        const cursorPos = markdownInput.selectionStart;
        const textBefore = markdownInput.value.substring(0, cursorPos);
        const textAfter = markdownInput.value.substring(cursorPos);

        markdownInput.value = textBefore + snippet + textAfter;
        markdownInput.focus();
        markdownInput.setSelectionRange(cursorPos + snippet.length, cursorPos + snippet.length);
        renderEmailContent();
    }

    function showToast(message) {
        toastMessage.textContent = message;
        toast.classList.add("show");
        setTimeout(() => toast.classList.remove("show"), 3500);
    }

    function simpleMarkdownFallback(text) {
        return text
            .replace(/^# (.*$)/gim, '<h1>$1</h1>')
            .replace(/^## (.*$)/gim, '<h2>$1</h2>')
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/\n\n/g, '<br><br>');
    }

    function getFallbackTemplates() {
        return [
            {
                id: "default",
                title: "Compte-Rendu Stratégique GitHub",
                category: "General",
                markdown: "# 🚀 Compte-Rendu de Réunion\n\n> [!NOTE]\n> **Décision Actée** : Validation du plan d'action.\n\n### Actions\n| Tâche | Responsable | Statut |\n| :--- | :--- | :--- |\n| Dashboard | Julien F. | `EN COURS` |\n"
            }
        ];
    }

    initApp();
});
