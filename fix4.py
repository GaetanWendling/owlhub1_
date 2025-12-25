#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
force_fix_all.py
Correction forcée complète : HTML + JS
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 CORRECTION FORCÉE COMPLÈTE")
print("=" * 60)

# ============================================
# 1. RECONSTRUIRE index.html HEADER
# ============================================
def rebuild_header():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print("❌ index.html introuvable")
        return False

    content = html_file.read_text(encoding='utf-8')

    # Nouveau header complet
    new_header = """<header>
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
    </header>"""

    # Chercher différents patterns de header
    patterns = [
        r'<header[^>]*>.*?</header>',
        r'<header>.*?</header>',
        r'<header\s+[^>]*>[\s\S]*?</header>'
    ]

    header_found = False
    for pattern in patterns:
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, new_header, content, flags=re.DOTALL | re.IGNORECASE)
            header_found = True
            print("✅ Header remplacé")
            break

    if not header_found:
        # Insérer après <body>
        body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + new_header + '\n' + content[insert_pos:]
            print("✅ Header inséré après <body>")
        else:
            print("❌ Impossible de trouver <body>")
            return False

    # Corriger le viewport
    content = re.sub(
        r'<meta\s+name="viewport"[^>]*>',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">',
        content,
        flags=re.IGNORECASE
    )

    html_file.write_text(content, encoding='utf-8')
    print("✅ index.html reconstruit")
    return True

# ============================================
# 2. RECONSTRUIRE theme.js COMPLET
# ============================================
def rebuild_theme_js():
    js_file = BASE_DIR / "assets" / "js" / "theme.js"
    js_file.parent.mkdir(parents=True, exist_ok=True)

    content = """/**
 * theme.js - Gestion du thème et du menu mobile
 */

// ============================================
// GESTION DU THÈME
// ============================================
const themeToggle = {
    button: null,

    init() {
        this.button = document.getElementById('theme-toggle');
        if (!this.button) return;

        // Charger le thème sauvegardé
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);

        // Listener
        this.button.addEventListener('click', () => this.toggle());

        console.log('✅ Theme toggle initialisé');
    },

    toggle() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        // Animation du bouton
        this.button.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            this.button.style.transform = 'rotate(0deg)';
        }, 300);
    }
};

// ============================================
// MENU MOBILE
// ============================================
const mobileNav = {
    burger: null,
    nav: null,
    overlay: null,
    isOpen: false,

    init() {
        // Sélectionner les éléments
        this.burger = document.querySelector('.mobile-menu-toggle');
        this.nav = document.querySelector('.mobile-nav');
        this.overlay = document.querySelector('.mobile-overlay');

        if (!this.burger || !this.nav || !this.overlay) {
            console.warn('⚠️ Éléments mobile manquants');
            return;
        }

        // Listeners
        this.burger.addEventListener('click', () => this.toggle());
        this.overlay.addEventListener('click', () => this.close());

        // Fermer au clic sur un lien
        this.nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                setTimeout(() => this.close(), 300);
            });
        });

        console.log('✅ Menu mobile initialisé');
    },

    toggle() {
        this.isOpen ? this.close() : this.open();
    },

    open() {
        this.isOpen = true;
        this.burger.classList.add('active');
        this.nav.classList.add('active');
        this.overlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // Bloquer le scroll
        console.log('📱 Menu ouvert');
    },

    close() {
        this.isOpen = false;
        this.burger.classList.remove('active');
        this.nav.classList.remove('active');
        this.overlay.classList.remove('active');
        document.body.style.overflow = ''; // Restaurer le scroll
        console.log('📱 Menu fermé');
    }
};

// ============================================
// INITIALISATION AU CHARGEMENT
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    console.log('🦉 Initialisation theme.js');

    themeToggle.init();
    mobileNav.init();

    console.log('✅ theme.js chargé');
});

// Export pour debug
window.mobileNav = mobileNav;
window.themeToggle = themeToggle;
"""

    js_file.write_text(content, encoding='utf-8')
    print("✅ theme.js reconstruit")

# ============================================
# 3. VÉRIFIER LA STRUCTURE FINALE
# ============================================
def verify_structure():
    print("\n📋 VÉRIFICATION FINALE")
    print("-" * 60)

    # Vérifier index.html
    html_file = BASE_DIR / "index.html"
    if html_file.exists():
        content = html_file.read_text(encoding='utf-8')
        checks = {
            "Header existe": bool(re.search(r'<header[^>]*>', content, re.IGNORECASE)),
            "Burger button": 'mobile-menu-toggle' in content,
            "Mobile nav": 'mobile-nav' in content,
            "Overlay": 'mobile-overlay' in content
        }

        for check, result in checks.items():
            status = "✅" if result else "❌"
            print(f"{status} {check}")

    # Vérifier theme.js
    js_file = BASE_DIR / "assets" / "js" / "theme.js"
    if js_file.exists():
        content = js_file.read_text(encoding='utf-8')
        checks_js = {
            "mobileNav object": 'const mobileNav' in content,
            "init function": 'init()' in content,
            "toggle function": 'toggle()' in content,
            "open function": 'open()' in content,
            "close function": 'close()' in content
        }

        print("\n📄 theme.js :")
        for check, result in checks_js.items():
            status = "✅" if result else "❌"
            print(f"{status} {check}")

# ============================================
# EXÉCUTION
# ============================================
rebuild_header()
rebuild_theme_js()
verify_structure()

print("\n" + "=" * 60)
print("✅ RECONSTRUCTION COMPLÈTE TERMINÉE")
print("=" * 60)
print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
