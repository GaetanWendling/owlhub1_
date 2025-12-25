#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rebuild_owlhub.py
RECONSTRUCTION COMPLÈTE DU SITE OWLHUB
"""

from pathlib import Path

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
CSS_DIR = BASE_DIR / "assets" / "css"
JS_DIR = BASE_DIR / "assets" / "js"
IMG_DIR = BASE_DIR / "assets" / "images"

for directory in [CSS_DIR, JS_DIR, IMG_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

print("🦉 OWLHUB - Reconstruction complète")
print("=" * 50)

# ============================================
# 1. style.css
# ============================================
CSS_CONTENT = """/* OWLHUB - STYLES PRINCIPAUX */

:root {
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-tertiary: #21262d;
    --text-primary: #c9d1d9;
    --text-secondary: #8b949e;
    --accent-primary: #58a6ff;
    --accent-secondary: #1f6feb;
    --border-color: #30363d;
    --shadow: rgba(0, 0, 0, 0.3);
}

[data-theme="light"] {
    --bg-primary: #ffffff;
    --bg-secondary: #f6f8fa;
    --bg-tertiary: #ffffff;
    --text-primary: #24292f;
    --text-secondary: #57606a;
    --accent-primary: #0969da;
    --accent-secondary: #0550ae;
    --border-color: #d0d7de;
    --shadow: rgba(0, 0, 0, 0.1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    overflow-x: hidden;
    transition: background-color 0.3s ease;
}

#particles-canvas {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    z-index: 0 !important;
    pointer-events: none !important;
}

header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border-color);
    padding: 1rem 2rem;
    z-index: 1000;
    transition: box-shadow 0.3s ease;
}

header.scrolled {
    box-shadow: 0 4px 12px var(--shadow);
}

nav {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--accent-primary);
    text-decoration: none;
}

.nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
}

.nav-links a {
    color: var(--text-primary);
    text-decoration: none;
    transition: color 0.3s;
    position: relative;
}

.nav-links a::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--accent-primary);
    transition: width 0.3s;
}

.nav-links a:hover::after {
    width: 100%;
}

.theme-toggle {
    background: none;
    border: 2px solid var(--border-color);
    color: var(--text-primary);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
}

.theme-toggle:hover {
    background: var(--accent-primary);
    border-color: var(--accent-primary);
    color: white;
}

.hamburger {
    display: none;
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
}

.hamburger span {
    width: 25px;
    height: 3px;
    background: var(--text-primary);
    transition: all 0.3s;
}

.hamburger.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
}

.hamburger.active span:nth-child(2) {
    opacity: 0;
}

.hamburger.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -6px);
}

.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
    position: relative;
    z-index: 1;
}

.hero-content h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.hero-content p {
    font-size: 1.25rem;
    color: var(--text-secondary);
    margin-bottom: 2rem;
}

.cta-button {
    display: inline-block;
    padding: 1rem 2rem;
    background: var(--accent-primary);
    color: white;
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.3s;
}

.cta-button:hover {
    background: var(--accent-secondary);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px var(--shadow);
}

.stats-section {
    padding: 4rem 2rem;
    position: relative;
    z-index: 1;
}

.stats-grid {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.stat-card {
    background: var(--bg-secondary);
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid var(--border-color);
    transition: transform 0.3s;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px var(--shadow);
}

.stat-number {
    font-size: 3rem;
    font-weight: bold;
    color: var(--accent-primary);
    margin-bottom: 0.5rem;
}

.stat-label {
    color: var(--text-secondary);
}

footer {
    background: var(--bg-secondary);
    padding: 2rem;
    text-align: center;
    border-top: 1px solid var(--border-color);
    position: relative;
    z-index: 1;
}

.owl-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 999;
    animation: float 3s ease-in-out infinite;
}

.owl-container img {
    width: 80px;
    height: 80px;
    transition: transform 0.3s;
}

.owl-container img:hover {
    transform: scale(1.1) rotate(5deg);
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

@media (max-width: 768px) {
    .hamburger {
        display: flex;
    }

    .nav-links {
        position: fixed;
        top: 0;
        right: -100%;
        height: 100vh;
        width: 250px;
        background: var(--bg-secondary);
        flex-direction: column;
        padding: 5rem 2rem;
        transition: right 0.3s;
        box-shadow: -4px 0 12px var(--shadow);
    }

    .nav-links.active {
        right: 0;
    }

    .hero-content h1 {
        font-size: 2rem;
    }
}
"""

(CSS_DIR / "style.css").write_text(CSS_CONTENT, encoding='utf-8')
print("✅ style.css créé")

# ============================================
# 2. main.js
# ============================================
JS_MAIN = """// OWLHUB - FICHIER PRINCIPAL
console.log('🦉 OwlHub Main.js chargé');

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    if (counters.length === 0) return;

    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };

        updateCounter();
    });
}

function initStatsObserver() {
    const statsSection = document.querySelector('.stats-section');
    if (!statsSection) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log('👁️ Stats visibles, démarrage animation');
                animateCounters();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    observer.observe(statsSection);
    console.log('✅ Observer des stats activé');
}

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    console.log('✅ Smooth scroll initialisé');
}

function initHeaderScroll() {
    const header = document.querySelector('header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    console.log('✅ Header scroll initialisé');
}

function initCardAnimations() {
    const cards = document.querySelectorAll('.stat-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = ` $ {index * 0.1}s`;
    });
    console.log(`✅  $ {cards.length} cartes interactives initialisées`);
}

function init() {
    console.log('🚀 Initialisation OwlHub...');
    initStatsObserver();
    initSmoothScroll();
    initHeaderScroll();
    initCardAnimations();
    console.log('✅ OwlHub complètement initialisé');
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

window.OwlHub = {
    version: '1.0.0',
    animateCounters,
    init
};

console.log('🦉 OwlHub API disponible via window.OwlHub');
"""

(JS_DIR / "main.js").write_text(JS_MAIN, encoding='utf-8')
print("✅ main.js créé")

# ============================================
# 3. theme.js
# ============================================
JS_THEME = """// GESTION DU THÈME
const themeToggle = document.querySelector('.theme-toggle');
const htmlElement = document.documentElement;
const owlImage = document.querySelector('.owl-container img');

const savedTheme = localStorage.getItem('theme') || 'dark';
htmlElement.setAttribute('data-theme', savedTheme);
updateThemeButton(savedTheme);
updateOwlImage(savedTheme);

console.log(`🎨 Thème actif:  $ {savedTheme}`);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeButton(newTheme);
        updateOwlImage(newTheme);

        console.log(`🔄 Thème changé:  $ {newTheme}`);

        if (typeof updateParticles === 'function') {
            updateParticles(newTheme);
        }
    });
    console.log('✅ Bouton thème initialisé');
}

function updateThemeButton(theme) {
    if (!themeToggle) return;
    themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
}

function updateOwlImage(theme) {
    if (!owlImage) return;
    owlImage.src = theme === 'dark'
        ? 'assets/images/owl_dark.png'
        : 'assets/images/owl_light.png';
}
"""

(JS_DIR / "theme.js").write_text(JS_THEME, encoding='utf-8')
print("✅ theme.js créé")

# ============================================
# 4. hamburger.js
# ============================================
JS_HAMBURGER = """// MENU HAMBURGER
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
        console.log('🍔 Menu toggled');
    });

    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });

    document.addEventListener('click', (e) => {
        if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        }
    });

    console.log('✅ Menu hamburger initialisé');
}
"""

(JS_DIR / "hamburger.js").write_text(JS_HAMBURGER, encoding='utf-8')
print("✅ hamburger.js créé")

# ============================================
# 5. index.html
# ============================================
INDEX_HTML = """<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OwlHub - Transformation Digitale</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <header>
        <nav>
            <a href="#" class="logo">🦉 OwlHub</a>
            <ul class="nav-links">
                <li><a href="#hero">Accueil</a></li>
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

    <section id="hero" class="hero">
        <div class="hero-content">
            <h1>Transformez vos idées en solutions digitales</h1>
            <p>Automatisation • Power BI • Web • Sur-mesure</p>
            <a href="contact.html" class="cta-button">Commencer maintenant</a>
        </div>
    </section>

    <section class="stats-section">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number" data-target="127">0</div>
                <div class="stat-label">Projets réalisés</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="98">0</div>
                <div class="stat-label">% Satisfaction client</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="1500">0</div>
                <div class="stat-label">Heures économisées</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="100">0</div>
                <div class="stat-label">% Sur mesure</div>
            </div>
        </div>
    </section>

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

(BASE_DIR / "index.html").write_text(INDEX_HTML, encoding='utf-8')
print("✅ index.html créé")

# ============================================
# RÉSUMÉ
# ============================================
print("\n" + "=" * 50)
print("🎉 RECONSTRUCTION TERMINÉE")
print("=" * 50)
print(f"📁 Dossier: {BASE_DIR}")
print("\n✅ Fichiers créés:")
print("  • assets/css/style.css")
print("  • assets/js/main.js")
print("  • assets/js/theme.js")
print("  • assets/js/hamburger.js")
print("  • index.html")
print("\n🚀 DÉPLOIEMENT:")
print("  git add .")
print("  git commit -m 'Rebuild complet'")
print("  git push origin main")
print("\n🦉 OwlHub prêt !")
