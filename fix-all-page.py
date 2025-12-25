#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

# HTML UNIVERSEL pour toutes les pages
UNIVERSAL_TEMPLATE = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title} - OwlHub</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <header>
        <nav>
            <a href="index.html" class="logo">🦉 OwlHub</a>
            <ul class="nav-links">
                <li><a href="index.html">Accueil</a></li>
                <li><a href="methode.html">Méthode</a></li>
                <li><a href="offres.html">Offres</a></li>
                <li><a href="power-bi.html">Power BI</a></li>
                <li><a href="a-propos.html">À propos</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <button class="theme-toggle">☀️</button>
            <button class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </nav>
    </header>

    <main style="min-height: 100vh; padding-top: 80px; position: relative; z-index: 1;">
        {page_content}
    </main>

    <footer>
        <p>&copy; 2025 OwlHub. Tous droits réservés.</p>
    </footer>

    <div class="owl-container">
        <img src="assets/images/owl_dark.png" alt="OwlHub Mascotte">
    </div>

    <script src="assets/js/particles-config.js"></script>
    <script src="assets/js/main.js"></script>
    <script src="assets/js/theme.js"></script>
    <script src="assets/js/hamburger.js"></script>
</body>
</html>
"""

# Contenus des pages
PAGES = {
    "methode.html": {
        "title": "Notre Méthode",
        "content": """
        <section class="hero">
            <div class="hero-content">
                <h1>Notre Méthode</h1>
                <p>Une approche structurée pour votre transformation digitale</p>
            </div>
        </section>
        <section style="padding: 4rem 2rem;">
            <div style="max-width: 1200px; margin: 0 auto;">
                <h2>Les 4 étapes clés</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>1. Analyse</h3>
                        <p>Audit approfondi de vos besoins</p>
                    </div>
                    <div class="stat-card">
                        <h3>2. Conception</h3>
                        <p>Design de la solution optimale</p>
                    </div>
                    <div class="stat-card">
                        <h3>3. Développement</h3>
                        <p>Réalisation technique sur-mesure</p>
                    </div>
                    <div class="stat-card">
                        <h3>4. Accompagnement</h3>
                        <p>Formation et support continu</p>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "offres.html": {
        "title": "Nos Offres",
        "content": """
        <section class="hero">
            <div class="hero-content">
                <h1>Nos Offres</h1>
                <p>Des solutions adaptées à chaque besoin</p>
            </div>
        </section>
        <section style="padding: 4rem 2rem;">
            <div style="max-width: 1200px; margin: 0 auto;">
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>Automatisation</h3>
                        <p>Scripts Python, VBA, Power Automate</p>
                        <a href="contact.html" class="cta-button" style="display: inline-block; margin-top: 1rem;">En savoir plus</a>
                    </div>
                    <div class="stat-card">
                        <h3>Power BI</h3>
                        <p>Dashboards interactifs et analyses</p>
                        <a href="power-bi.html" class="cta-button" style="display: inline-block; margin-top: 1rem;">Découvrir</a>
                    </div>
                    <div class="stat-card">
                        <h3>Développement Web</h3>
                        <p>Sites modernes et performants</p>
                        <a href="contact.html" class="cta-button" style="display: inline-block; margin-top: 1rem;">Demander un devis</a>
                    </div>
                    <div class="stat-card">
                        <h3>Sur-mesure</h3>
                        <p>Solutions 100% personnalisées</p>
                        <a href="contact.html" class="cta-button" style="display: inline-block; margin-top: 1rem;">Nous contacter</a>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "power-bi.html": {
        "title": "Power BI",
        "content": """
        <section class="hero">
            <div class="hero-content">
                <h1>Expertise Power BI</h1>
                <p>Transformez vos données en insights actionnables</p>
            </div>
        </section>
        <section style="padding: 4rem 2rem;">
            <div style="max-width: 1200px; margin: 0 auto;">
                <h2>Nos services Power BI</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>Dashboards</h3>
                        <p>Création de tableaux de bord interactifs</p>
                    </div>
                    <div class="stat-card">
                        <h3>Modélisation</h3>
                        <p>Architecture de données optimisée</p>
                    </div>
                    <div class="stat-card">
                        <h3>DAX</h3>
                        <p>Mesures et calculs avancés</p>
                    </div>
                    <div class="stat-card">
                        <h3>Formation</h3>
                        <p>Accompagnement de vos équipes</p>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "a-propos.html": {
        "title": "À propos",
        "content": """
        <section class="hero">
            <div class="hero-content">
                <h1>À propos d'OwlHub</h1>
                <p>Votre partenaire transformation digitale</p>
            </div>
        </section>
        <section style="padding: 4rem 2rem;">
            <div style="max-width: 800px; margin: 0 auto; text-align: center;">
                <h2>Notre Mission</h2>
                <p style="font-size: 1.2rem; line-height: 1.8; margin: 2rem 0;">
                    OwlHub accompagne les entreprises dans leur transformation digitale
                    en proposant des solutions sur-mesure d'automatisation, de data visualisation
                    et de développement web.
                </p>
                <div style="margin-top: 3rem;">
                    <h3>Nos valeurs</h3>
                    <div class="stats-grid" style="margin-top: 2rem;">
                        <div class="stat-card">
                            <h4>Excellence</h4>
                            <p>Qualité irréprochable</p>
                        </div>
                        <div class="stat-card">
                            <h4>Innovation</h4>
                            <p>Technologies de pointe</p>
                        </div>
                        <div class="stat-card">
                            <h4>Proximité</h4>
                            <p>Accompagnement personnalisé</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "contact.html": {
        "title": "Contact",
        "content": """
        <section class="hero">
            <div class="hero-content">
                <h1>Contactez-nous</h1>
                <p>Discutons de votre projet</p>
            </div>
        </section>
        <section style="padding: 4rem 2rem;">
            <div style="max-width: 600px; margin: 0 auto;">
                <form style="background: var(--bg-secondary); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color);">
                    <div style="margin-bottom: 1.5rem;">
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-primary);">Nom</label>
                        <input type="text" style="width: 100%; padding: 0.75rem; background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; color: var(--text-primary);">
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-primary);">Email</label>
                        <input type="email" style="width: 100%; padding: 0.75rem; background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; color: var(--text-primary);">
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-primary);">Message</label>
                        <textarea rows="5" style="width: 100%; padding: 0.75rem; background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 8px; color: var(--text-primary);"></textarea>
                    </div>
                    <button type="submit" class="cta-button" style="width: 100%;">Envoyer</button>
                </form>
            </div>
        </section>
        """
    }
}

print("🦉 Correction de toutes les pages")
print("=" * 50)

for filename, data in PAGES.items():
    html = UNIVERSAL_TEMPLATE.format(
        page_title=data["title"],
        page_content=data["content"]
    )
    (BASE_DIR / filename).write_text(html, encoding='utf-8')
    print(f"✅ {filename} corrigé")

print("\n🎉 Toutes les pages ont été mises à jour !")
print("\n🚀 Déploiement:")
print("  git add .")
print("  git commit -m 'Fix: correction toutes les pages'")
print("  git push origin main")
