#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create_owlhub_complete.py
Crée TOUT le site OwlHub dans C:\\Users\\gaeta\\OneDrive\\Bureau\\owlhub_
"""

from pathlib import Path

# ============================================
# CONFIGURATION
# ============================================
BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
ASSETS_DIR = BASE_DIR / "assets"
CSS_DIR = ASSETS_DIR / "css"
JS_DIR = ASSETS_DIR / "js"
IMG_DIR = ASSETS_DIR / "images"

def create_directories():
    """Créer la structure des dossiers"""
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    CSS_DIR.mkdir(parents=True, exist_ok=True)
    JS_DIR.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    print("✅ Structure de dossiers créée")

# ============================================
# HTML - INDEX.HTML
# ============================================
def create_index_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OwlHub Dashboard - Tableaux de bord Power BI sur mesure</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>

            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link active">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link">À propos</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>

            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-container">
            <div class="hero-content">
                <h1 class="hero-title">
                    Transformez vos données en <span id="animated-word" class="animated-word">insights</span>
                </h1>
                <p class="hero-description">
                    Des tableaux de bord Power BI sur mesure qui transforment vos données brutes en décisions stratégiques.
                </p>

                <div class="hero-cta">
                    <a href="offres.html" class="btn btn-primary">Découvrir nos offres</a>
                    <a href="contact.html" class="btn btn-secondary">Nous contacter</a>
                </div>
            </div>

            <div class="hero-visual">
                <!-- Code Window -->
                <div class="code-window">
                    <div class="code-window-header">
                        <div class="code-dots">
                            <span class="dot dot-red"></span>
                            <span class="dot dot-yellow"></span>
                            <span class="dot dot-green"></span>
                        </div>
                        <span class="code-window-title">Transform.m</span>
                    </div>
                    <div class="code-window-body">
                        <pre><code id="typing-code" class="code-content"></code></pre>
                    </div>
                </div>

                <!-- Stats Grid -->
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-value" data-target="50">0</div>
                        <div class="stat-label">Projets réalisés</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" data-target="95">0</div>
                        <div class="stat-label">Satisfaction client</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" data-target="24">0</div>
                        <div class="stat-label">Heures économisées</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" data-target="100">0</div>
                        <div class="stat-label">Sur mesure</div>
                    </div>
                </div>

                <!-- Owl Mascot -->
                <img src="assets/images/owl_dark.png" alt="OwlHub Mascot" class="owl-mascot" id="owl-mascot">
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Transformez vos données en décisions stratégiques</p>
            </div>

            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="assets/js/particles.js"></script>
    <script src="assets/js/text-animation.js"></script>
    <script src="assets/js/typing.js"></script>
    <script src="assets/js/stats.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "index.html").write_text(content, encoding='utf-8')
    print("✅ index.html créé")

# ============================================
# HTML - OFFRES.HTML
# ============================================
def create_offres_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nos Offres - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link active">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link">À propos</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub" class="page-owl" id="page-owl">
        <h1 class="page-title">Nos Offres</h1>
        <p class="page-subtitle">Choisissez la solution qui correspond à vos besoins</p>
    </header>

    <!-- Content -->
    <section class="page-content">
        <div class="container">
            <div class="pricing-grid">
                <!-- Offre Essentiel -->
                <div class="pricing-card">
                    <div class="pricing-header">
                        <h3>Dashboard Essentiel</h3>
                        <div class="pricing-price">
                            <span class="price-amount">1 500€</span>
                            <span class="price-period">HT</span>
                        </div>
                    </div>
                    <div class="pricing-features">
                        <h4>✨ Inclus :</h4>
                        <ul>
                            <li>✓ 1 page Power BI interactive</li>
                            <li>✓ 5 visualisations personnalisées</li>
                            <li>✓ Connexion à 2 sources de données</li>
                            <li>✓ Formation utilisateur (2h)</li>
                            <li>✓ Support 30 jours</li>
                        </ul>
                        <div class="pricing-duration">
                            <strong>⏱️ Durée :</strong> 1-2 semaines
                        </div>
                    </div>
                    <a href="contact.html" class="btn btn-primary btn-full">Démarrer</a>
                </div>

                <!-- Offre Premium -->
                <div class="pricing-card pricing-featured">
                    <div class="pricing-badge">🔥 Populaire</div>
                    <div class="pricing-header">
                        <h3>Dashboard Premium</h3>
                        <div class="pricing-price">
                            <span class="price-amount">3 500€</span>
                            <span class="price-period">HT</span>
                        </div>
                    </div>
                    <div class="pricing-features">
                        <h4>✨ Inclus :</h4>
                        <ul>
                            <li>✓ 3-5 pages Power BI interactives</li>
                            <li>✓ 15+ visualisations avancées</li>
                            <li>✓ Connexion multi-sources illimitée</li>
                            <li>✓ Modèle de données optimisé</li>
                            <li>✓ Mesures DAX personnalisées</li>
                            <li>✓ Formation complète (1 jour)</li>
                            <li>✓ Support 90 jours prioritaire</li>
                            <li>✓ Documentation technique</li>
                        </ul>
                        <div class="pricing-duration">
                            <strong>⏱️ Durée :</strong> 3-4 semaines
                        </div>
                    </div>
                    <a href="contact.html" class="btn btn-primary btn-full">Démarrer</a>
                </div>

                <!-- Offre Enterprise -->
                <div class="pricing-card">
                    <div class="pricing-header">
                        <h3>Dashboard Enterprise</h3>
                        <div class="pricing-price">
                            <span class="price-amount">Sur devis</span>
                        </div>
                    </div>
                    <div class="pricing-features">
                        <h4>✨ Inclus :</h4>
                        <ul>
                            <li>✓ Solution complète multi-rapports</li>
                            <li>✓ Architecture de données complexe</li>
                            <li>✓ Intégration API & automatisation</li>
                            <li>✓ Sécurité niveau entreprise (RLS)</li>
                            <li>✓ Performance optimisée</li>
                            <li>✓ Formation équipe complète</li>
                            <li>✓ Support continu 12 mois</li>
                            <li>✓ Évolutions incluses</li>
                        </ul>
                        <div class="pricing-duration">
                            <strong>⏱️ Durée :</strong> 6-12 semaines
                        </div>
                    </div>
                    <a href="contact.html" class="btn btn-primary btn-full">Nous contacter</a>
                </div>
            </div>

            <!-- CTA Section -->
            <div class="cta-section">
                <h2>Besoin d'un accompagnement sur mesure ?</h2>
                <p>Discutons de votre projet et trouvons ensemble la solution idéale</p>
                <a href="contact.html" class="btn btn-primary btn-large">Prendre rendez-vous</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Transformez vos données en décisions stratégiques</p>
            </div>
            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "offres.html").write_text(content, encoding='utf-8')
    print("✅ offres.html créé")

# ============================================
# HTML - METHODE.HTML
# ============================================
def create_methode_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notre Méthode - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link active">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link">À propos</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub" class="page-owl" id="page-owl">
        <h1 class="page-title">Notre Méthode</h1>
        <p class="page-subtitle">Un processus éprouvé en 3 phases pour des dashboards performants</p>
    </header>

    <section class="page-content">
        <div class="container">
            <div class="method-timeline">
                <!-- Phase 1 -->
                <div class="method-phase">
                    <div class="phase-number">01</div>
                    <div class="phase-content">
                        <h2 class="phase-title">🔍 Analyse & Cadrage</h2>
                        <p class="phase-description">
                            Nous commençons par comprendre vos enjeux métier, vos sources de données
                            et vos objectifs décisionnels.
                        </p>
                        <ul class="phase-list">
                            <li>Atelier de cadrage avec vos équipes</li>
                            <li>Audit de vos sources de données</li>
                            <li>Définition des KPI critiques</li>
                            <li>Maquettage des écrans principaux</li>
                            <li>Validation du périmètre fonctionnel</li>
                        </ul>
                        <div class="phase-duration">⏱️ Durée : 3-5 jours</div>
                    </div>
                </div>

                <!-- Phase 2 -->
                <div class="method-phase">
                    <div class="phase-number">02</div>
                    <div class="phase-content">
                        <h2 class="phase-title">⚙️ Développement & Intégration</h2>
                        <p class="phase-description">
                            Nous construisons votre dashboard avec les meilleures pratiques
                            Power BI et une attention particulière à la performance.
                        </p>
                        <ul class="phase-list">
                            <li>Connexion et transformation des données (Power Query)</li>
                            <li>Modélisation du schéma en étoile</li>
                            <li>Création des mesures DAX optimisées</li>
                            <li>Design des visualisations interactives</li>
                            <li>Tests de performance et ajustements</li>
                            <li>Mise en place de la sécurité (RLS si nécessaire)</li>
                        </ul>
                        <div class="phase-duration">⏱️ Durée : 10-20 jours</div>
                    </div>
                </div>

                <!-- Phase 3 -->
                <div class="method-phase">
                    <div class="phase-number">03</div>
                    <div class="phase-content">
                        <h2 class="phase-title">🚀 Formation & Déploiement</h2>
                        <p class="phase-description">
                            Nous vous accompagnons jusqu'à l'autonomie complète avec une formation
                            adaptée et un support post-déploiement.
                        </p>
                        <ul class="phase-list">
                            <li>Formation utilisateurs sur-mesure</li>
                            <li>Documentation technique complète</li>
                            <li>Guide d'utilisation illustré</li>
                            <li>Déploiement sur Power BI Service</li>
                            <li>Configuration des actualisations automatiques</li>
                            <li>Support post-déploiement inclus</li>
                        </ul>
                        <div class="phase-duration">⏱️ Durée : 2-3 jours</div>
                    </div>
                </div>
            </div>

            <div class="cta-section">
                <h2>Prêt à démarrer votre projet ?</h2>
                <p>Planifions ensemble votre atelier de cadrage</p>
                <a href="contact.html" class="btn btn-primary btn-large">Prendre rendez-vous</a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Transformez vos données en décisions stratégiques</p>
            </div>
            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "methode.html").write_text(content, encoding='utf-8')
    print("✅ methode.html créé")

# ============================================
# HTML - POWER-BI.HTML
# ============================================
def create_powerbi_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power BI - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link active">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link">À propos</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub" class="page-owl" id="page-owl">
        <h1 class="page-title">Pourquoi Power BI ?</h1>
        <p class="page-subtitle">La plateforme de Business Intelligence de référence</p>
    </header>

    <section class="page-content">
        <div class="container">
            <div class="content-section">
                <h2>🎯 Power BI : Le leader de la BI moderne</h2>
                <p class="lead">
                    Power BI de Microsoft est reconnu comme leader du marché de la Business Intelligence
                    par Gartner depuis 15 années consécutives.
                </p>
            </div>

            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>Visualisations Puissantes</h3>
                    <p>
                        Plus de 200 types de visualisations interactives pour raconter l'histoire
                        de vos données de manière percutante.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🔗</div>
                    <h3>Connexion Universelle</h3>
                    <p>
                        Connectez-vous à plus de 100 sources de données : Excel, SQL, Azure,
                        Salesforce, Google Analytics, et bien plus.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Performance Optimale</h3>
                    <p>
                        Moteur de compression VertiPaq qui traite des millions de lignes
                        en quelques secondes.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🔒</div>
                    <h3>Sécurité Enterprise</h3>
                    <p>
                        Row-Level Security (RLS), chiffrement, conformité RGPD,
                        certifications ISO/SOC.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">📱</div>
                    <h3>Mobile First</h3>
                    <p>
                        Applications natives iOS et Android pour accéder à vos dashboards
                        partout, tout le temps.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🤖</div>
                    <h3>IA Intégrée</h3>
                    <p>
                        Insights automatiques, Q&A en langage naturel, prévisions intelligentes
                        via Azure Machine Learning.
                    </p>
                </div>
            </div>

            <div class="content-section">
                <h2>🛠️ Les Technologies que Nous Maîtrisons</h2>
                <div class="tech-stack">
                    <div class="tech-item">
                        <strong>Power Query (M)</strong>
                        <p>Transformation et nettoyage de données</p>
                    </div>
                    <div class="tech-item">
                        <strong>DAX</strong>
                        <p>Langage de formules pour mesures complexes</p>
                    </div>
                    <div class="tech-item">
                        <strong>Power BI Service</strong>
                        <p>Publication et partage cloud</p>
                    </div>
                    <div class="tech-item">
                        <strong>Dataflows</strong>
                        <p>ETL cloud pour centraliser les transformations</p>
                    </div>
                    <div class="tech-item">
                        <strong>Power BI API</strong>
                        <p>Intégration et automatisation</p>
                    </div>
                    <div class="tech-item">
                        <strong>Azure Integration</strong>
                        <p>Connexion aux services Azure (Synapse, Data Lake, etc.)</p>
                    </div>
                </div>
            </div>

            <div class="content-section comparison-section">
                <h2>⚖️ Power BI vs Alternatives</h2>
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>Critère</th>
                            <th>Power BI</th>
                            <th>Tableau</th>
                            <th>Qlik</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Prix</td>
                            <td>⭐⭐⭐⭐⭐ (10€/mois)</td>
                            <td>⭐⭐ (70€/mois)</td>
                            <td>⭐⭐ (Sur devis élevé)</td>
                        </tr>
                        <tr>
                            <td>Facilité d'utilisation</td>
                            <td>⭐⭐⭐⭐⭐</td>
                            <td>⭐⭐⭐⭐</td>
                            <td>⭐⭐⭐</td>
                        </tr>
                        <tr>
                            <td>Intégration Microsoft</td>
                            <td>⭐⭐⭐⭐⭐ (Natif)</td>
                            <td>⭐⭐⭐</td>
                            <td>⭐⭐⭐</td>
                        </tr>
                        <tr>
                            <td>Communauté</td>
                            <td>⭐⭐⭐⭐⭐ (Très active)</td>
                            <td>⭐⭐⭐⭐</td>
                            <td>⭐⭐⭐</td>
                        </tr>
                        <tr>
                            <td>IA & Analytics avancés</td>
                            <td>⭐⭐⭐⭐⭐</td>
                            <td>⭐⭐⭐⭐</td>
                            <td>⭐⭐⭐⭐</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="cta-section">
                <h2>Prêt à exploiter la puissance de Power BI ?</h2>
                <p>Découvrons ensemble comment Power BI peut transformer votre activité</p>
                <a href="contact.html" class="btn btn-primary btn-large">Discutons de votre projet</a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Transformez vos données en décisions stratégiques</p>
            </div>
            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "power-bi.html").write_text(content, encoding='utf-8')
    print("✅ power-bi.html créé")

# ============================================
# HTML - A-PROPOS.HTML
# ============================================
def create_apropos_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>À Propos - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link active">À propos</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub" class="page-owl" id="page-owl">
        <h1 class="page-title">À Propos</h1>
        <p class="page-subtitle">Votre partenaire expert en dashboards Power BI</p>
    </header>

    <section class="page-content">
        <div class="container">
            <div class="about-intro">
                <h2>👋 Bonjour, je suis [Votre Nom]</h2>
                <p class="lead">
                    Consultant Power BI indépendant passionné par la transformation de données brutes
                    en insights actionnables. Depuis 5 ans, j'accompagne des entreprises de toutes tailles
                    dans leur transition vers une culture data-driven.
                </p>
            </div>

            <div class="values-grid">
                <div class="value-card">
                    <div class="value-icon">🎯</div>
                    <h3>Excellence Technique</h3>
                    <p>
                        Maîtrise approfondie de Power BI, DAX, Power Query et des bonnes pratiques
                        de modélisation de données.
                    </p>
                </div>

                <div class="value-card">
                    <div class="value-icon">🤝</div>
                    <h3>Approche Partenaire</h3>
                    <p>
                        Je ne suis pas qu'un prestataire, je deviens votre partenaire de réussite
                        avec un accompagnement personnalisé.
                    </p>
                </div>

                <div class="value-card">
                    <div class="value-icon">📚</div>
                    <h3>Pédagogie</h3>
                    <p>
                        Formation et transfert de compétences pour vous rendre autonome
                        sur vos dashboards.
                    </p>
                </div>

                <div class="value-card">
                    <div class="value-icon">⚡</div>
                    <h3>Réactivité</h3>
                    <p>
                        Disponibilité et réponses rapides pour avancer efficacement
                        sur vos projets.
                    </p>
                </div>
            </div>

            <div class="expertise-section">
                <h2>🎓 Expertises & Certifications</h2>
                <div class="expertise-grid">
                    <div class="expertise-item">
                        <strong>Microsoft Certified: Power BI Data Analyst Associate</strong>
                        <p>Certification officielle Microsoft sur Power BI</p>
                    </div>
                    <div class="expertise-item">
                        <strong>DAX Avancé</strong>
                        <p>Mesures complexes, Time Intelligence, Variables</p>
                    </div>
                    <div class="expertise-item">
                        <strong>Power Query / M</strong>
                        <p>Transformations avancées et optimisation ETL</p>
                    </div>
                    <div class="expertise-item">
                        <strong>Modélisation de données</strong>
                        <p>Schéma en étoile, Snowflake, optimisation performances</p>
                    </div>
                    <div class="expertise-item">
                        <strong>Power BI Service</strong>
                        <p>Workspaces, Gateway, Row-Level Security</p>
                    </div>
                    <div class="expertise-item">
                        <strong>Intégrations Azure</strong>
                        <p>Azure SQL, Synapse Analytics, Data Lake</p>
                    </div>
                </div>
            </div>

            <div class="stats-section">
                <h2>📊 Quelques Chiffres</h2>
                <div class="stats-about-grid">
                    <div class="stat-about-card">
                        <div class="stat-about-number">50+</div>
                        <div class="stat-about-label">Projets livrés</div>
                    </div>
                    <div class="stat-about-card">
                        <div class="stat-about-number">30+</div>
                        <div class="stat-about-label">Clients satisfaits</div>
                    </div>
                    <div class="stat-about-card">
                        <div class="stat-about-number">5</div>
                        <div class="stat-about-label">Années d'expérience</div>
                    </div>
                    <div class="stat-about-card">
                        <div class="stat-about-number">95%</div>
                        <div class="stat-about-label">Taux de satisfaction</div>
                    </div>
                </div>
            </div>

            <div class="cta-section">
                <h2>Travaillons ensemble !</h2>
                <p>Discutons de votre projet et de vos enjeux data</p>
                <a href="contact.html" class="btn btn-primary btn-large">Me contacter</a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Transformez vos données en décisions stratégiques</p>
            </div>
            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "a-propos.html").write_text(content, encoding='utf-8')
    print("✅ a-propos.html créé")

# ============================================
# HTML - CONTACT.HTML
# ============================================
def create_contact_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link">À propos</a></li>
                <li><a href="contact.html" class="nav-link active">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub" class="page-owl" id="page-owl">
        <h1 class="page-title">Contactez-nous</h1>
        <p class="page-subtitle">Discutons de votre projet dashboard</p>
    </header>

    <section class="page-content">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-form-wrapper">
                    <h2>📨 Envoyez-nous un message</h2>
                    <form class="contact-form" id="contact-form">
                        <div class="form-group">
                            <label for="name">Nom complet *</label>
                            <input type="text" id="name" name="name" required>
                        </div>

                        <div class="form-group">
                            <label for="email">Email *</label>
                            <input type="email" id="email" name="email" required>
                        </div>

                        <div class="form-group">
                            <label for="phone">Téléphone</label>
                            <input type="tel" id="phone" name="phone">
                        </div>

                        <div class="form-group">
                            <label for="company">Société</label>
                            <input type="text" id="company" name="company">
                        </div>

                        <div class="form-group">
                            <label for="service">Service souhaité *</label>
                            <select id="service" name="service" required>
                                <option value="">-- Sélectionnez --</option>
                                <option value="essentiel">Dashboard Essentiel</option>
                                <option value="premium">Dashboard Premium</option>
                                <option value="enterprise">Dashboard Enterprise</option>
                                <option value="autre">Autre / Devis personnalisé</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="message">Message *</label>
                            <textarea id="message" name="message" rows="6" required placeholder="Décrivez-nous votre projet, vos enjeux et vos objectifs..."></textarea>
                        </div>

                        <button type="submit" class="btn btn-primary btn-full">Envoyer le message</button>
                    </form>
                </div>

                <div class="contact-info-wrapper">
                    <h2>📞 Informations de contact</h2>

                    <div class="contact-info-item">
                        <div class="contact-icon">✉️</div>
                        <div class="contact-details">
                            <strong>Email</strong>
                            <a href="mailto:contact@owlhub.fr">contact@owlhub.fr</a>
                        </div>
                    </div>

                    <div class="contact-info-item">
                        <div class="contact-icon">📱</div>
                        <div class="contact-details">
                            <strong>Téléphone</strong>
                            <a href="tel:+33123456789">+33 1 23 45 67 89</a>
                        </div>
                    </div>

                    <div class="contact-info-item">
                        <div class="contact-icon">📍</div>
                        <div class="contact-details">
                            <strong>Localisation</strong>
                            <p>Paris, France<br>Interventions à distance</p>
                        </div>
                    </div>

                    <div class="contact-info-item">
                        <div class="contact-icon">⏰</div>
                        <div class="contact-details">
                            <strong>Disponibilité</strong>
                            <p>Lun - Ven : 9h - 18h<br>Réponse sous 24h</p>
                        </div>
                    </div>

                    <div class="contact-cta">
                        <h3>🚀 Démarrage rapide</h3>
                        <p>Réponse garantie sous 24h ouvrées. Premier échange offert pour cadrer votre projet.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Transformez vos données en décisions stratégiques</p>
            </div>
            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
    <script src="assets/js/contact-form.js"></script>
</body>
</html>"""

    (BASE_DIR / "contact.html").write_text(content, encoding='utf-8')
    print("✅ contact.html créé")

# ============================================
# CSS COMPLET - EN PLUSIEURS PARTIES
# ============================================
def create_css():
    css_content = """/* ============================================
   OWLHUB DASHBOARD - STYLE COMPLET
   ============================================ */

/* Reset & Variables */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    /* Colors */
    --primary: #3b82f6;
    --primary-hover: #2563eb;
    --secondary: #64748b;
    --gradient-start: #3b82f6;
    --gradient-end: #8b5cf6;

    /* Light theme */
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --bg-tertiary: #f1f5f9;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-tertiary: #94a3b8;
    --border: #e2e8f0;
    --border-hover: #cbd5e1;

    /* Shadows */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

    /* Owl glow */
    --owl-glow: rgba(59, 130, 246, 0.5);

    /* Code colors */
    --code-bg: #1e293b;
    --code-text: #e2e8f0;
    --code-keyword: #60a5fa;
    --code-string: #34d399;
    --code-comment: #94a3b8;
    --code-function: #a78bfa;
}

[data-theme="dark"] {
    --primary: #ef4444;
    --primary-hover: #dc2626;
    --gradient-start: #ef4444;
    --gradient-end: #f97316;

    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-tertiary: #334155;
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-tertiary: #64748b;
    --border: #334155;
    --border-hover: #475569;

    --owl-glow: rgba(239, 68, 68, 0.5);
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    overflow-x: hidden;
    transition: background-color 0.3s ease, color 0.3s ease;
}

/* Particles Canvas */
#particles-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
}

/* ============================================
   NAVIGATION
   ============================================ */

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    z-index: 1000;
    transition: all 0.3s ease;
}

[data-theme="light"] .navbar {
    background: rgba(248, 250, 252, 0.9);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: 800;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.25rem;
    z-index: 10;
}

.logo-owl {
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.logo-hub {
    color: var(--text-primary);
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
    align-items: center;
}

.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
    position: relative;
}

.nav-link:hover {
    color: var(--primary);
}

.nav-link.active {
    color: var(--primary);
}

.nav-link.active::after {
    content: '';
    position: absolute;
    bottom: -0.5rem;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--primary);
}

.nav-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.theme-toggle {
    background: var(--bg-tertiary);
    border: 1px solid var(--border);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
}

.theme-toggle:hover {
    background: var(--bg-secondary);
    border-color: var(--border-hover);
    transform: scale(1.1);
}

.theme-icon {
    font-size: 1.25rem;
}

[data-theme="dark"] .theme-icon.sun {
    display: block;
}

[data-theme="dark"] .theme-icon.moon {
    display: none;
}

[data-theme="light"] .theme-icon.sun {
    display: none;
}

[data-theme="light"] .theme-icon.moon {
    display: block;
}

/* ============================================
   HERO SECTION
   ============================================ */

.hero {
    position: relative;
    padding: 8rem 2rem 4rem;
    min-height: 100vh;
    display: flex;
    align-items: center;
}

.hero-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

.hero-content {
    z-index: 1;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1.5rem;
}

.animated-word {
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: inline-block;
    transition: all 0.3s ease;
}

.hero-description {
    font-size: 1.25rem;
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.8;
}

.hero-cta {
    display: flex;
    gap: 1rem;
}

.btn {
    padding: 0.875rem 1.75rem;
    border-radius: 0.5rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    display: inline-block;
    cursor: pointer;
    border: none;
    font-size: 1rem;
}

.btn-primary {
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    color: white;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.btn-secondary {
    background: var(--bg-tertiary);
    color: var(--text-primary);
    border: 1px solid var(--border);
}

.btn-secondary:hover {
    background: var(--bg-secondary);
    border-color: var(--border-hover);
}

.btn-large {
    padding: 1.25rem 2.5rem;
    font-size: 1.125rem;
}

.btn-full {
    width: 100%;
    text-align: center;
}

/* ============================================
   HERO VISUAL
   ============================================ */

.hero-visual {
    position: relative;
    z-index: 1;
}

.code-window {
    background: var(--code-bg);
    border-radius: 0.75rem;
    overflow: hidden;
    box-shadow: var(--shadow-xl);
    margin-bottom: 2rem;
}

.code-window-header {
    background: rgba(255, 255, 255, 0.05);
    padding: 0.75rem 1rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.code-dots {
    display: flex;
    gap: 0.5rem;
}

.dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}

.dot-red { background: #ef4444; }
.dot-yellow { background: #f59e0b; }
.dot-green { background: #10b981; }

.code-window-title {
    color: var(--code-text);
    font-size: 0.875rem;
    font-family: 'Fira Code', monospace;
}

.code-window-body {
    padding: 1.5rem;
    max-height: 300px;
    overflow: auto;
}

.code-content {
    font-family: 'Fira Code', monospace;
    font-size: 0.875rem;
    line-height: 1.6;
    color: var(--code-text);
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}

.stat-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 0.75rem;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    border-color: var(--primary);
}

.stat-value {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.stat-label {
    color: var(--text-secondary);
    font-size: 0.875rem;
    font-weight: 500;
}

/* Owl Mascot */
.owl-mascot {
    width: 200px;
    height: 200px;
    object-fit: contain;
    display: block;
    margin: 0 auto;
    filter: drop-shadow(0 0 30px var(--owl-glow));
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-20px);
    }
}

/* ============================================
   PAGE HEADER
   ============================================ */

.page-header {
    position: relative;
    padding: 8rem 2rem 4rem;
    text-align: center;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border);
}

.page-owl {
    width: 120px;
    height: 120px;
    object-fit: contain;
    margin: 0 auto 2rem;
    filter: drop-shadow(0 0 30px var(--owl-glow));
    animation: float 3s ease-in-out infinite;
}

.page-title {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 1rem;
}

.page-subtitle {
    font-size: 1.25rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 0 auto;
}

/* ============================================
   PAGE CONTENT
   ============================================ */

.page-content {
    position: relative;
    padding: 4rem 2rem;
    z-index: 1;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

/* ============================================
   PRICING GRID (OFFRES)
   ============================================ */

.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

.pricing-card {
    background: var(--bg-secondary);
    border: 2px solid var(--border);
    border-radius: 1rem;
    padding: 2rem;
    transition: all 0.3s ease;
    position: relative;
}

.pricing-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-xl);
    border-color: var(--primary);
}

.pricing-featured {
    border-color: var(--primary);
    box-shadow: var(--shadow-lg);
}

.pricing-badge {
    position: absolute;
    top: -12px;
    right: 20px;
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 2rem;
    font-size: 0.875rem;
    font-weight: 600;
}

.pricing-header {
    text-align: center;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border);
}

.pricing-header h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.pricing-price {
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 0.5rem;
}

.price-amount {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.price-period {
    color: var(--text-secondary);
    font-size: 1rem;
}

.pricing-features h4 {
    font-size: 1rem;
    margin-bottom: 1rem;
    color: var(--text-secondary);
}

.pricing-features ul {
    list-style: none;
    margin-bottom: 1.5rem;
}

.pricing-features li {
    padding: 0.5rem 0;
    color: var(--text-secondary);
}

.pricing-duration {
    background: var(--bg-tertiary);
    padding: 1rem;
    border-radius: 0.5rem;
    margin-top: 1.5rem;
    font-size: 0.875rem;
    color: var(--text-secondary);
}

/* ============================================
   METHOD TIMELINE (METHODE)
   ============================================ */

.method-timeline {
    display: flex;
    flex-direction: column;
    gap: 3rem;
    margin-bottom: 4rem;
}

.method-phase {
    display: grid;
    grid-template-columns: 100px 1fr;
    gap: 2rem;
    align-items: start;
}

.phase-number {
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    font-weight: 800;
    box-shadow: var(--shadow-lg);
}

.phase-content {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 1rem;
    padding: 2rem;
}

.phase-title {
    font-size: 1.75rem;
    margin-bottom: 1rem;
}

.phase-description {
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    line-height: 1.8;
}

.phase-list {
    list-style: none;
    margin-bottom: 1.5rem;
}

.phase-list li {
    padding: 0.5rem 0;
    padding-left: 1.5rem;
    position: relative;
    color: var(--text-secondary);
}

.phase-list li::before {
    content: '✓';
    position: absolute;
    left: 0;
    color: var(--primary);
    font-weight: 800;
}

.phase-duration {
    background: var(--bg-tertiary);
    padding: 1rem;
    border-radius: 0.5rem;
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-secondary);
}

/* ============================================
   CTA SECTION
   ============================================ */

.cta-section {
    text-align: center;
    background: var(--bg-secondary);
    border: 2px solid var(--border);
    border-radius: 1rem;
    padding: 4rem 2rem;
    margin-top: 4rem;
}

.cta-section h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.cta-section p {
    color: var(--text-secondary);
    font-size: 1.125rem;
    margin-bottom: 2rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* ============================================
   FEATURES GRID (POWER-BI)
   ============================================ */

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

.feature-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 1rem;
    padding: 2rem;
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    border-color: var(--primary);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.feature-card h3 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
}

.feature-card p {
    color: var(--text-secondary);
    line-height: 1.8;
}

/* ============================================
   ABOUT PAGE
   ============================================ */

.about-intro {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 4rem;
}

.about-intro h2 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
}

.lead {
    font-size: 1.25rem;
    color: var(--text-secondary);
    line-height: 1.8;
}

.values-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

.value-card {
    text-align: center;
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 1rem;
    padding: 2rem;
    transition: all 0.3s ease;
}

.value-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    border-color: var(--primary);
}

.value-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.value-card h3 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
}

.value-card p {
    color: var(--text-secondary);
    line-height: 1.8;
}

.expertise-section {
    margin-bottom: 4rem;
}

.expertise-section h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 2rem;
}

.expertise-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.expertise-item {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 0.75rem;
    padding: 1.5rem;
}

.expertise-item strong {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--primary);
}

.expertise-item p {
    color: var(--text-secondary);
    font-size: 0.875rem;
}

.stats-section {
    margin-bottom: 4rem;
}

.stats-section h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 2rem;
}

.stats-about-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
}

.stat-about-card {
    text-align: center;
    background: var(--bg-secondary);
    border: 2px solid var(--border);
    border-radius: 1rem;
    padding: 2rem;
    transition: all 0.3s ease;
}

.stat-about-card:hover {
    transform: scale(1.05);
    border-color: var(--primary);
}

.stat-about-number {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.stat-about-label {
    color: var(--text-secondary);
    font-weight: 500;
}

/* ============================================
   CONTACT PAGE
   ============================================ */

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
}

.contact-form-wrapper h2,
.contact-info-wrapper h2 {
    font-size: 1.75rem;
    margin-bottom: 2rem;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: var(--text-secondary);
}

.form-group input,
.form-group select,
.form-group textarea {
    padding: 0.875rem;
    border: 1px solid var(--border);
    border-radius: 0.5rem;
    background: var(--bg-secondary);
    color: var(--text-primary);
    font-family: inherit;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.contact-info-item {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 0.75rem;
}

.contact-icon {
    font-size: 2rem;
}

.contact-details strong {
    display: block;
    margin-bottom: 0.5rem;
}

.contact-details a {
    color: var(--primary);
    text-decoration: none;
}

.contact-details a:hover {
    text-decoration: underline;
}

.contact-details p {
    color: var(--text-secondary);
    line-height: 1.6;
}

.contact-cta {
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    color: white;
    padding: 2rem;
    border-radius: 1rem;
    margin-top: 2rem;
}

.contact-cta h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.contact-cta p {
    color: rgba(255, 255, 255, 0.9);
}

/* ============================================
   FOOTER
   ============================================ */

.footer {
    background: var(--bg-secondary);
    border-top: 1px solid var(--border);
    padding: 3rem 2rem 1rem;
    margin-top: 4rem;
}

.footer-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 2fr 3fr;
    gap: 3rem;
    margin-bottom: 2rem;
}

.footer-brand {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.footer-logo {
    font-size: 1.5rem;
    font-weight: 800;
}

.footer-tagline {
    color: var(--text-secondary);
    font-size: 0.875rem;
}

.footer-links {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
}

.footer-column h4 {
    margin-bottom: 1rem;
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-secondary);
}

.footer-column ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.footer-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 0.875rem;
    transition: color 0.3s ease;
}

.footer-link:hover {
    color: var(--primary);
}

.footer-bottom {
    max-width: 1200px;
    margin: 0 auto;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    text-align: center;
}

.footer-bottom p {
    color: var(--text-tertiary);
    font-size: 0.875rem;
}

/* ============================================
   RESPONSIVE
   ============================================ */

@media (max-width: 768px) {
    .hero-container {
        grid-template-columns: 1fr;
    }

    .hero-title {
        font-size: 2.5rem;
    }

    .nav-menu {
        display: none;
    }

    .pricing-grid {
        grid-template-columns: 1fr;
    }

    .method-phase {
        grid-template-columns: 1fr;
    }

    .contact-grid {
        grid-template-columns: 1fr;
    }

    .footer-container {
        grid-template-columns: 1fr;
    }

    .footer-links {
        grid-template-columns: 1fr;
    }
}"""

    (CSS_DIR / "style.css").write_text(css_content, encoding='utf-8')
    print("✅ style.css créé")

# Continuer dans le prochain message...
# ============================================
# HTML - POWER-BI.HTML
# ============================================
def create_power_bi_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power BI - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>

            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link active">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link">À propos</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>

            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub Mascot" class="page-owl" id="page-owl">
        <h1 class="page-title">Power BI Excellence</h1>
        <p class="page-subtitle">Transformez vos données en insights actionnables avec des dashboards Power BI performants</p>
    </header>

    <main class="page-content">
        <div class="container">
            <section class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>Visualisations Impactantes</h3>
                    <p>Graphiques interactifs et tableaux de bord intuitifs qui racontent l'histoire de vos données</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Performance Optimisée</h3>
                    <p>Modèles de données optimisés et requêtes DAX performantes pour des temps de chargement rapides</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🔄</div>
                    <h3>Automatisation Complète</h3>
                    <p>Actualisation automatique des données via Power Query et connexions aux sources multiples</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🎨</div>
                    <h3>Design sur Mesure</h3>
                    <p>Interface adaptée à votre charte graphique et aux besoins spécifiques de vos utilisateurs</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">📱</div>
                    <h3>Responsive Design</h3>
                    <p>Dashboards parfaitement adaptés à tous les écrans : desktop, tablette et mobile</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🔐</div>
                    <h3>Sécurité & Gouvernance</h3>
                    <p>Gestion des droits d'accès (RLS) et respect des normes de sécurité des données</p>
                </div>
            </section>

            <section class="cta-section">
                <h2>Prêt à transformer vos données ?</h2>
                <p>Discutons de votre projet Power BI et créons ensemble des dashboards qui feront la différence</p>
                <a href="contact.html" class="btn btn-primary btn-large">Démarrer un projet</a>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Dashboards Power BI sur mesure pour décideurs exigeants</p>
            </div>

            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>

                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>

                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "power-bi.html").write_text(content, encoding='utf-8')
    print("✅ power-bi.html créé")

# ============================================
# HTML - A-PROPOS.HTML
# ============================================
def create_apropos_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>À propos - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>

            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link active">À propos</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>

            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub Mascot" class="page-owl" id="page-owl">
        <h1 class="page-title">À propos d'OwlHub</h1>
        <p class="page-subtitle">Une expertise Power BI au service de vos décisions stratégiques</p>
    </header>

    <main class="page-content">
        <div class="container">
            <section class="about-intro">
                <h2>Notre Mission</h2>
                <p class="lead">Transformer la complexité de vos données en tableaux de bord Power BI clairs, élégants et actionnables. Nous croyons que chaque entreprise mérite des outils de Business Intelligence à la hauteur de ses ambitions.</p>
            </section>

            <section class="values-grid">
                <div class="value-card">
                    <div class="value-icon">🎯</div>
                    <h3>Excellence</h3>
                    <p>Chaque dashboard est conçu avec le souci du détail et optimisé pour la performance</p>
                </div>

                <div class="value-card">
                    <div class="value-icon">💡</div>
                    <h3>Innovation</h3>
                    <p>Nous utilisons les dernières fonctionnalités Power BI pour créer des solutions modernes</p>
                </div>

                <div class="value-card">
                    <div class="value-icon">🤝</div>
                    <h3>Partenariat</h3>
                    <p>Nous travaillons main dans la main avec vous pour comprendre vos besoins réels</p>
                </div>

                <div class="value-card">
                    <div class="value-icon">📈</div>
                    <h3>Impact</h3>
                    <p>Nos dashboards génèrent des insights qui transforment votre prise de décision</p>
                </div>
            </section>

            <section class="expertise-section">
                <h2>Notre Expertise</h2>
                <div class="expertise-grid">
                    <div class="expertise-item">
                        <strong>Power BI Desktop & Service</strong>
                        <p>Maîtrise complète de l'écosystème Power BI, du développement à la publication</p>
                    </div>

                    <div class="expertise-item">
                        <strong>Modélisation de données</strong>
                        <p>Création de modèles en étoile optimisés et relations complexes</p>
                    </div>

                    <div class="expertise-item">
                        <strong>DAX & Power Query</strong>
                        <p>Mesures DAX avancées et transformations de données performantes</p>
                    </div>

                    <div class="expertise-item">
                        <strong>Sécurité RLS</strong>
                        <p>Implémentation de Row-Level Security pour un accès contrôlé</p>
                    </div>

                    <div class="expertise-item">
                        <strong>Intégration API</strong>
                        <p>Connexion aux sources de données variées (SQL, Excel, Web Services)</p>
                    </div>

                    <div class="expertise-item">
                        <strong>UX/UI Design</strong>
                        <p>Interface utilisateur intuitive et design moderne</p>
                    </div>
                </div>
            </section>

            <section class="stats-section">
                <h2>Quelques Chiffres</h2>
                <div class="stats-about-grid">
                    <div class="stat-about-card">
                        <div class="stat-about-number">50+</div>
                        <div class="stat-about-label">Dashboards créés</div>
                    </div>

                    <div class="stat-about-card">
                        <div class="stat-about-number">30+</div>
                        <div class="stat-about-label">Clients satisfaits</div>
                    </div>

                    <div class="stat-about-card">
                        <div class="stat-about-number">5+</div>
                        <div class="stat-about-label">Années d'expérience</div>
                    </div>

                    <div class="stat-about-card">
                        <div class="stat-about-number">100%</div>
                        <div class="stat-about-label">Satisfaction client</div>
                    </div>
                </div>
            </section>

            <section class="cta-section">
                <h2>Travaillons ensemble</h2>
                <p>Vous avez un projet Power BI ? Discutons-en autour d'un café (virtuel ou non) !</p>
                <a href="contact.html" class="btn btn-primary btn-large">Prendre contact</a>
            </section>
        </div>
    </main>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Dashboards Power BI sur mesure pour décideurs exigeants</p>
            </div>

            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>

                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>

                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "a-propos.html").write_text(content, encoding='utf-8')
    print("✅ a-propos.html créé")

# ============================================
# HTML - CONTACT.HTML
# ============================================
def create_contact_html():
    content = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact - OwlHub Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
            </a>

            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Accueil</a></li>
                <li><a href="offres.html" class="nav-link">Offres</a></li>
                <li><a href="methode.html" class="nav-link">Méthode</a></li>
                <li><a href="power-bi.html" class="nav-link">Power BI</a></li>
                <li><a href="a-propos.html" class="nav-link">À propos</a></li>
                <li><a href="contact.html" class="nav-link active">Contact</a></li>
            </ul>

            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle">
                    <span class="theme-icon sun">☀️</span>
                    <span class="theme-icon moon">🌙</span>
                </button>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <img src="assets/images/owl_dark.png" alt="OwlHub Mascot" class="page-owl" id="page-owl">
        <h1 class="page-title">Contactez-nous</h1>
        <p class="page-subtitle">Parlons de votre projet Power BI</p>
    </header>

    <main class="page-content">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-form-wrapper">
                    <h2>Envoyez-nous un message</h2>
                    <form class="contact-form" action="#" method="POST">
                        <div class="form-group">
                            <label for="name">Nom complet *</label>
                            <input type="text" id="name" name="name" required>
                        </div>

                        <div class="form-group">
                            <label for="email">Email *</label>
                            <input type="email" id="email" name="email" required>
                        </div>

                        <div class="form-group">
                            <label for="company">Entreprise</label>
                            <input type="text" id="company" name="company">
                        </div>

                        <div class="form-group">
                            <label for="offer">Offre souhaitée</label>
                            <select id="offer" name="offer">
                                <option value="">-- Sélectionnez une offre --</option>
                                <option value="starter">Dashboard Starter</option>
                                <option value="pro">Dashboard Pro</option>
                                <option value="enterprise">Solution Enterprise</option>
                                <option value="other">Autre demande</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="message">Message *</label>
                            <textarea id="message" name="message" rows="6" required></textarea>
                        </div>

                        <button type="submit" class="btn btn-primary btn-full">Envoyer le message</button>
                    </form>
                </div>

                <div class="contact-info-wrapper">
                    <h2>Informations de contact</h2>

                    <div class="contact-info-item">
                        <div class="contact-icon">📧</div>
                        <div class="contact-details">
                            <strong>Email</strong>
                            <a href="mailto:contact@owlhub.fr">contact@owlhub.fr</a>
                            <p>Réponse sous 24h ouvrées</p>
                        </div>
                    </div>

                    <div class="contact-info-item">
                        <div class="contact-icon">📞</div>
                        <div class="contact-details">
                            <strong>Téléphone</strong>
                            <a href="tel:+33123456789">+33 1 23 45 67 89</a>
                            <p>Lun-Ven: 9h-18h</p>
                        </div>
                    </div>

                    <div class="contact-info-item">
                        <div class="contact-icon">💼</div>
                        <div class="contact-details">
                            <strong>LinkedIn</strong>
                            <a href="https://linkedin.com" target="_blank">Suivez-nous</a>
                            <p>Restez informé de nos actualités</p>
                        </div>
                    </div>

                    <div class="contact-cta">
                        <h3>Besoin d'un devis rapide ?</h3>
                        <p>Décrivez votre projet en quelques lignes et recevez une estimation sous 48h.</p>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <div class="footer-logo">
                    <span class="logo-owl">Owl</span><span class="logo-hub">Hub</span>
                </div>
                <p class="footer-tagline">Dashboards Power BI sur mesure pour décideurs exigeants</p>
            </div>

            <div class="footer-links">
                <div class="footer-column">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html" class="footer-link">Accueil</a></li>
                        <li><a href="offres.html" class="footer-link">Offres</a></li>
                        <li><a href="methode.html" class="footer-link">Méthode</a></li>
                    </ul>
                </div>

                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="power-bi.html" class="footer-link">Power BI</a></li>
                        <li><a href="a-propos.html" class="footer-link">À propos</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>
                </div>

                <div class="footer-column">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@owlhub.fr" class="footer-link">contact@owlhub.fr</a></li>
                        <li><a href="tel:+33123456789" class="footer-link">+33 1 23 45 67 89</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="footer-bottom">
            <p>&copy; 2024 OwlHub Dashboard. Tous droits réservés.</p>
        </div>
    </footer>

    <script src="assets/js/particles.js"></script>
    <script src="assets/js/theme.js"></script>
</body>
</html>"""

    (BASE_DIR / "contact.html").write_text(content, encoding='utf-8')
    print("✅ contact.html créé")

# Continue dans le prochain message pour les JS...
# ============================================
# JS - PARTICLES.JS
# ============================================
def create_particles_js():
    content = """// particles.js - Animation de particules interactive
class ParticlesAnimation {
    constructor() {
        this.canvas = document.getElementById('particles-canvas');
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mousePosition = { x: null, y: null };
        this.numberOfParticles = 80;

        this.init();
    }

    init() {
        this.resizeCanvas();
        this.createParticles();
        this.animate();

        // Event listeners
        window.addEventListener('resize', () => this.resizeCanvas());
        window.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        window.addEventListener('mouseout', () => this.handleMouseOut());
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    createParticles() {
        this.particles = [];
        for (let i = 0; i < this.numberOfParticles; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                radius: Math.random() * 2 + 1,
                opacity: Math.random() * 0.5 + 0.2
            });
        }
    }

    handleMouseMove(e) {
        this.mousePosition.x = e.clientX;
        this.mousePosition.y = e.clientY;
    }

    handleMouseOut() {
        this.mousePosition.x = null;
        this.mousePosition.y = null;
    }

    drawParticle(particle) {
        this.ctx.beginPath();
        this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);

        // Couleur adaptée au thème
        const theme = document.documentElement.getAttribute('data-theme');
        const color = theme === 'dark' ? '59, 130, 246' : '239, 68, 68'; // blue ou red

        this.ctx.fillStyle = `rgba(${color}, ${particle.opacity})`;
        this.ctx.fill();
    }

    connectParticles(p1, p2, distance) {
        const maxDistance = 150;
        const opacity = (1 - distance / maxDistance) * 0.3;

        this.ctx.beginPath();
        this.ctx.moveTo(p1.x, p1.y);
        this.ctx.lineTo(p2.x, p2.y);

        const theme = document.documentElement.getAttribute('data-theme');
        const color = theme === 'dark' ? '59, 130, 246' : '239, 68, 68';

        this.ctx.strokeStyle = `rgba(${color}, ${opacity})`;
        this.ctx.lineWidth = 1;
        this.ctx.stroke();
    }

    updateParticle(particle) {
        // Déplacement
        particle.x += particle.vx;
        particle.y += particle.vy;

        // Rebond sur les bords
        if (particle.x < 0 || particle.x > this.canvas.width) {
            particle.vx *= -1;
        }
        if (particle.y < 0 || particle.y > this.canvas.height) {
            particle.vy *= -1;
        }

        // Interaction avec la souris
        if (this.mousePosition.x !== null && this.mousePosition.y !== null) {
            const dx = this.mousePosition.x - particle.x;
            const dy = this.mousePosition.y - particle.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 120) {
                const force = (120 - distance) / 120;
                particle.x -= (dx / distance) * force * 2;
                particle.y -= (dy / distance) * force * 2;
            }
        }
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Mise à jour et dessin des particules
        this.particles.forEach(particle => {
            this.updateParticle(particle);
            this.drawParticle(particle);
        });

        // Connexions entre particules proches
        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 150) {
                    this.connectParticles(this.particles[i], this.particles[j], distance);
                }
            }
        }

        requestAnimationFrame(() => this.animate());
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    new ParticlesAnimation();
});"""

    (JS_DIR / "particles.js").write_text(content, encoding='utf-8')
    print("✅ particles.js créé")

# ============================================
# JS - THEME.JS
# ============================================
def create_theme_js():
    content = """// theme.js - Gestion du thème clair/sombre
class ThemeManager {
    constructor() {
        this.themeToggle = document.getElementById('theme-toggle');
        this.currentTheme = localStorage.getItem('theme') || 'dark';

        this.init();
    }

    init() {
        // Appliquer le thème sauvegardé
        this.applyTheme(this.currentTheme);

        // Event listener sur le bouton
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', () => this.toggleTheme());
        }
    }

    applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        this.currentTheme = theme;

        // Changer l'image du hibou si présente
        this.updateOwlImage(theme);
    }

    toggleTheme() {
        const newTheme = this.currentTheme === 'dark' ? 'light' : 'dark';
        this.applyTheme(newTheme);

        // Animation du bouton
        this.themeToggle.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            this.themeToggle.style.transform = 'rotate(0deg)';
        }, 300);
    }

    updateOwlImage(theme) {
        const owlImages = document.querySelectorAll('.hero-owl, .page-owl, #page-owl');
        owlImages.forEach(img => {
            if (theme === 'dark') {
                img.src = img.src.replace('owl_light.png', 'owl_dark.png');
            } else {
                img.src = img.src.replace('owl_dark.png', 'owl_light.png');
            }
        });
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    new ThemeManager();
});"""

    (JS_DIR / "theme.js").write_text(content, encoding='utf-8')
    print("✅ theme.js créé")

# ============================================
# JS - TYPING.JS (pour l'animation du hero)
# ============================================
def create_typing_js():
    content = """// typing.js - Animation de texte qui s'écrit
class TypingAnimation {
    constructor(element, words, typingSpeed = 100, deletingSpeed = 50, delayBetweenWords = 2000) {
        this.element = element;
        this.words = words;
        this.typingSpeed = typingSpeed;
        this.deletingSpeed = deletingSpeed;
        this.delayBetweenWords = delayBetweenWords;
        this.wordIndex = 0;
        this.charIndex = 0;
        this.isDeleting = false;

        this.type();
    }

    type() {
        const currentWord = this.words[this.wordIndex];

        if (this.isDeleting) {
            // Effacer
            this.element.textContent = currentWord.substring(0, this.charIndex - 1);
            this.charIndex--;

            if (this.charIndex === 0) {
                this.isDeleting = false;
                this.wordIndex = (this.wordIndex + 1) % this.words.length;
                setTimeout(() => this.type(), 500);
                return;
            }
        } else {
            // Écrire
            this.element.textContent = currentWord.substring(0, this.charIndex + 1);
            this.charIndex++;

            if (this.charIndex === currentWord.length) {
                this.isDeleting = true;
                setTimeout(() => this.type(), this.delayBetweenWords);
                return;
            }
        }

        const speed = this.isDeleting ? this.deletingSpeed : this.typingSpeed;
        setTimeout(() => this.type(), speed);
    }
}

// Initialisation pour la page d'accueil
document.addEventListener('DOMContentLoaded', () => {
    const animatedWord = document.querySelector('.animated-word');
    if (animatedWord) {
        const words = ['Données', 'KPIs', 'Insights', 'Décisions'];
        new TypingAnimation(animatedWord, words);
    }
});"""

    (JS_DIR / "typing.js").write_text(content, encoding='utf-8')
    print("✅ typing.js créé")

# ============================================
# JS - SCROLL.JS (animations au scroll)
# ============================================
def create_scroll_js():
    content = """// scroll.js - Animations au défilement
class ScrollAnimations {
    constructor() {
        this.elements = document.querySelectorAll('.feature-card, .pricing-card, .method-phase, .value-card, .stat-card');
        this.navbar = document.querySelector('.navbar');

        this.init();
    }

    init() {
        this.observeElements();
        this.handleNavbarScroll();
        window.addEventListener('scroll', () => this.handleNavbarScroll());
    }

    observeElements() {
        const options = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, options);

        this.elements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(20px)';
            element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(element);
        });
    }

    handleNavbarScroll() {
        if (window.scrollY > 50) {
            this.navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
            this.navbar.style.backgroundColor = 'rgba(15, 23, 42, 0.95)';
        } else {
            this.navbar.style.boxShadow = 'none';
            this.navbar.style.backgroundColor = 'rgba(15, 23, 42, 0.8)';
        }
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    new ScrollAnimations();
});"""

    (JS_DIR / "scroll.js").write_text(content, encoding='utf-8')
    print("✅ scroll.js créé")

# ============================================
# CSS - STYLES COMPLÉMENTAIRES (pour pages About et Contact)
# ============================================
def add_extra_css_styles():
    extra_css = """

/* ============================================
   ABOUT PAGE - STYLES COMPLÉMENTAIRES
   ============================================ */

.about-intro {
    text-align: center;
    margin-bottom: 4rem;
}

.about-intro h2 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.lead {
    font-size: 1.25rem;
    color: var(--text-secondary);
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.8;
}

.values-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

.value-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
}

.value-card:hover {
    transform: translateY(-5px);
    border-color: var(--primary);
    box-shadow: var(--shadow-lg);
}

.value-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.value-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}

.value-card p {
    color: var(--text-secondary);
    line-height: 1.6;
}

.expertise-section {
    margin-bottom: 4rem;
}

.expertise-section h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 2rem;
}

.expertise-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.expertise-item {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.5rem;
}

.expertise-item strong {
    display: block;
    color: var(--primary);
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}

.expertise-item p {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.5;
}

.stats-section {
    margin-bottom: 4rem;
}

.stats-section h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 2rem;
}

.stats-about-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
}

.stat-about-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
}

.stat-about-card:hover {
    transform: scale(1.05);
    border-color: var(--primary);
}

.stat-about-number {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.stat-about-label {
    color: var(--text-secondary);
    font-size: 1rem;
}

/* ============================================
   CONTACT PAGE - STYLES COMPLÉMENTAIRES
   ============================================ */

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    margin-bottom: 4rem;
}

.contact-form-wrapper,
.contact-info-wrapper {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2.5rem;
}

.contact-form-wrapper h2,
.contact-info-wrapper h2 {
    font-size: 1.75rem;
    margin-bottom: 1.5rem;
    color: var(--text-primary);
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group label {
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
    background: var(--bg-tertiary);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    color: var(--text-primary);
    font-family: inherit;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.form-group textarea {
    resize: vertical;
    min-height: 120px;
}

.btn-full {
    width: 100%;
}

.contact-info-item {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border);
}

.contact-info-item:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

.contact-icon {
    font-size: 2rem;
    flex-shrink: 0;
}

.contact-details {
    flex: 1;
}

.contact-details strong {
    display: block;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}

.contact-details a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    transition: color 0.3s ease;
}

.contact-details a:hover {
    color: var(--primary-hover);
}

.contact-details p {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-top: 0.25rem;
}

.contact-cta {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1));
    border: 1px solid var(--primary);
    border-radius: 8px;
    padding: 1.5rem;
    margin-top: 2rem;
}

.contact-cta h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: var(--primary);
}

.contact-cta p {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.6;
}

@media (max-width: 768px) {
    .contact-grid {
        grid-template-columns: 1fr;
    }

    .stats-about-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}"""

    # Ajouter au fichier CSS existant
    with open(CSS_DIR / "style.css", "a", encoding='utf-8') as f:
        f.write(extra_css)
    print("✅ Styles complémentaires ajoutés au CSS")

# ============================================
# MISE À JOUR DU MAIN
# ============================================
if __name__ == "__main__":
    print("🦉 CRÉATION COMPLÈTE DU SITE OWLHUB")
    print("=" * 60)

    create_directories()

    print("\n📄 Création des fichiers HTML...")
    create_index_html()
    create_offres_html()
    create_methode_html()
    create_power_bi_html()
    create_apropos_html()
    create_contact_html()

    print("\n🎨 Création du CSS...")
    create_css()
    add_extra_css_styles()

    print("\n⚡ Création des fichiers JavaScript...")
    create_particles_js()
    create_theme_js()
    create_typing_js()
    create_scroll_js()

    print("\n" + "=" * 60)
    print("✅ SITE OWLHUB CRÉÉ AVEC SUCCÈS !")
    print(f"📁 Emplacement : {BASE_DIR}")
    print("\n📋 Prochaines étapes :")
    print("  1. Ajouter les images du hibou dans assets/images/")
    print("  2. Ouvrir index.html dans un navigateur")
    print("  3. Tester toutes les pages et animations")
    print("\n🦉 Profite de ton nouveau site !")
