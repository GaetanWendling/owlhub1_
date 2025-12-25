#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_html_mobile.py
Ajoute les éléments mobile manquants dans le HTML
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 CORRECTION HTML + CSS MOBILE")
print("=" * 60)

# ============================================
# 1. CORRIGER index.html
# ============================================
def fix_index_html():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print("❌ index.html introuvable")
        return False

    content = html_file.read_text(encoding='utf-8')

    # Trouver le header existant
    header_match = re.search(r'<header[^>]*>(.*?)</header>', content, re.DOTALL)

    if not header_match:
        print("❌ Aucun header trouvé")
        return False

    old_header = header_match.group(1)

    # Vérifier si les éléments mobile existent déjà
    if 'mobile-menu-toggle' in old_header:
        print("ℹ️ Éléments mobile déjà présents")
        return True

    # Construire le nouveau header complet
    new_header_content = """
        <nav class="nav-container">
            <a href="#home" class="logo">
                🦉 <span class="gradient-text">OwlHub</span>
            </a>

            <!-- Navigation Desktop -->
            <ul class="nav-links desktop-nav">
                <li><a href="#home">Accueil</a></li>
                <li><a href="#features">Fonctionnalités</a></li>
                <li><a href="#about">À propos</a></li>
                <li><a href="#stats">Statistiques</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>

            <!-- Bouton Theme -->
            <button id="theme-toggle" class="theme-toggle" aria-label="Changer de thème">
                <span class="sun">☀️</span>
                <span class="moon">🌙</span>
            </button>

            <!-- Bouton Burger Mobile -->
            <button class="mobile-menu-toggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </nav>

        <!-- Navigation Mobile -->
        <nav class="mobile-nav">
            <ul>
                <li><a href="#home">🏠 Accueil</a></li>
                <li><a href="#features">✨ Fonctionnalités</a></li>
                <li><a href="#about">📖 À propos</a></li>
                <li><a href="#stats">📊 Statistiques</a></li>
                <li><a href="#contact">📧 Contact</a></li>
            </ul>
        </nav>

        <!-- Overlay -->
        <div class="mobile-overlay"></div>
    """

    # Remplacer le contenu du header
    new_content = content.replace(
        header_match.group(0),
        f'<header>{new_header_content}</header>'
    )

    # Vérifier et corriger le viewport
    if 'maximum-scale=5.0' not in new_content:
        new_content = re.sub(
            r'<meta name="viewport"[^>]*>',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">',
            new_content
        )

    html_file.write_text(new_content, encoding='utf-8')
    print("✅ index.html corrigé avec éléments mobile")
    return True

# ============================================
# 2. AJOUTER LES STYLES MOBILE
# ============================================
def add_mobile_css():
    css_file = BASE_DIR / "assets" / "css" / "style.css"

    if not css_file.exists():
        print("❌ style.css introuvable")
        return False

    content = css_file.read_text(encoding='utf-8')

    # Vérifier si les styles sont déjà présents
    if 'mobile-menu-toggle' in content:
        print("ℹ️ Styles mobile déjà présents dans style.css")
        return True

    mobile_css = """

/* ============================================
   NAVIGATION MOBILE
   ============================================ */

/* Bouton burger */
.mobile-menu-toggle {
    display: none;
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 10001;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    border-radius: 12px;
    width: 50px;
    height: 50px;
    cursor: pointer;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 5px;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
    padding: 0;
}

.mobile-menu-toggle:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

.mobile-menu-toggle:active {
    transform: scale(0.95);
}

/* Barres du burger */
.mobile-menu-toggle span {
    display: block;
    width: 24px;
    height: 3px;
    background: white;
    border-radius: 3px;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

/* Animation en X */
.mobile-menu-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(7px, 7px);
}

.mobile-menu-toggle.active span:nth-child(2) {
    opacity: 0;
    transform: translateX(-20px);
}

.mobile-menu-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -7px);
}

/* Panneau mobile */
.mobile-nav {
    display: none;
    position: fixed;
    top: 0;
    right: -100%;
    width: 300px;
    max-width: 85vw;
    height: 100vh;
    background: var(--card-bg, rgba(255, 255, 255, 0.95));
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    z-index: 10000;
    padding: 100px 30px 30px;
    transition: right 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: -10px 0 40px rgba(0, 0, 0, 0.2);
    overflow-y: auto;
}

.mobile-nav.active {
    right: 0;
}

.mobile-nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.mobile-nav li {
    margin: 0;
    opacity: 0;
    transform: translateX(50px);
}

.mobile-nav.active li {
    animation: slideInMobile 0.5s ease forwards;
}

.mobile-nav.active li:nth-child(1) { animation-delay: 0.1s; }
.mobile-nav.active li:nth-child(2) { animation-delay: 0.15s; }
.mobile-nav.active li:nth-child(3) { animation-delay: 0.2s; }
.mobile-nav.active li:nth-child(4) { animation-delay: 0.25s; }
.mobile-nav.active li:nth-child(5) { animation-delay: 0.3s; }

@keyframes slideInMobile {
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.mobile-nav a {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px 20px;
    color: var(--text-primary, #333);
    text-decoration: none;
    font-size: 1.1rem;
    font-weight: 500;
    border-radius: 12px;
    margin: 8px 0;
    transition: all 0.3s ease;
    border-left: 3px solid transparent;
}

.mobile-nav a:hover,
.mobile-nav a:active {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    border-left-color: #667eea;
    transform: translateX(5px);
}

/* Overlay */
.mobile-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(2px);
    z-index: 9999;
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}

.mobile-overlay.active {
    opacity: 1;
    pointer-events: all;
}

/* Media queries */
@media (max-width: 768px) {
    .mobile-menu-toggle {
        display: flex !important;
    }

    .mobile-nav {
        display: block !important;
    }

    .mobile-overlay {
        display: block !important;
    }

    .desktop-nav,
    nav .nav-links {
        display: none !important;
    }

    header {
        padding: 15px 20px;
    }

    .nav-container {
        justify-content: space-between;
    }

    .logo {
        margin-right: 60px;
    }
}

@media (max-width: 480px) {
    .mobile-nav {
        width: 280px;
    }

    .mobile-menu-toggle {
        width: 45px;
        height: 45px;
        top: 15px;
        right: 15px;
    }

    .mobile-menu-toggle span {
        width: 22px;
    }
}
"""

    content += mobile_css
    css_file.write_text(content, encoding='utf-8')
    print("✅ Styles mobile ajoutés dans style.css")
    return True

# ============================================
# 3. VÉRIFIER theme.js
# ============================================
def verify_theme_js():
    js_file = BASE_DIR / "assets" / "js" / "theme.js"

    if not js_file.exists():
        print("❌ theme.js introuvable")
        return False

    content = js_file.read_text(encoding='utf-8')

    checks = {
        "mobileNav object": "const mobileNav = {" in content or "const mobileNav={" in content,
        "init function": "init()" in content,
        "toggle function": "toggle()" in content,
        "burger listener": "mobile-menu-toggle" in content
    }

    print("\n📋 Vérification theme.js :")
    all_ok = True
    for check, result in checks.items():
        status = "✅" if result else "❌"
        print(f"   {status} {check}")
        if not result:
            all_ok = False

    return all_ok

# ============================================
# EXÉCUTION
# ============================================
fix_index_html()
add_mobile_css()
verify_theme_js()

print("\n" + "=" * 60)
print("✅ CORRECTIONS HTML/CSS TERMINÉES")
print("=" * 60)
print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
