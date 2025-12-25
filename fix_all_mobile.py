#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_all_mobile.py
Correction complète des problèmes mobile
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
JS_DIR = BASE_DIR / "assets" / "js"

print("🦉 CORRECTION COMPLÈTE MOBILE")
print("=" * 50)

# ============================================
# 1. CRÉER text-animation.js
# ============================================
def create_text_animation():
    JS_DIR.mkdir(parents=True, exist_ok=True)
    file_path = JS_DIR / "text-animation.js"

    content = """/**
 * text-animation.js
 * Gestion des animations de texte
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('✅ Text animations chargé');

    // Fade-in au scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.fade-in').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});
"""

    file_path.write_text(content, encoding='utf-8')
    print(f"✅ Créé : {file_path.name}")

# ============================================
# 2. CORRIGER stats.js
# ============================================
def fix_stats_js():
    file_path = JS_DIR / "stats.js"

    content = """/**
 * stats.js
 * Gestion des statistiques
 */

document.addEventListener('DOMContentLoaded', () => {

    const stats = {
        pageViews: 0,
        uniqueVisitors: 0,

        init() {
            this.loadFromStorage();
            this.trackPageView();
            this.updateDisplay();
        },

        loadFromStorage() {
            const stored = localStorage.getItem('owlhub_stats');
            if (stored) {
                const data = JSON.parse(stored);
                this.pageViews = data.pageViews || 0;
                this.uniqueVisitors = data.uniqueVisitors || 0;
            }
        },

        saveToStorage() {
            localStorage.setItem('owlhub_stats', JSON.stringify({
                pageViews: this.pageViews,
                uniqueVisitors: this.uniqueVisitors
            }));
        },

        trackPageView() {
            this.pageViews++;
            if (!sessionStorage.getItem('owlhub_visitor')) {
                this.uniqueVisitors++;
                sessionStorage.setItem('owlhub_visitor', 'true');
            }
            this.saveToStorage();
        },

        updateDisplay() {
            const pvEl = document.getElementById('stat-pageviews');
            const vEl = document.getElementById('stat-visitors');

            if (pvEl) pvEl.textContent = this.pageViews;
            if (vEl) vEl.textContent = this.uniqueVisitors;
        }
    };

    stats.init();
    console.log('✅ Stats module chargé');
});
"""

    file_path.write_text(content, encoding='utf-8')
    print(f"✅ Corrigé : {file_path.name}")

# ============================================
# 3. CORRIGER LE VIEWPORT dans index.html
# ============================================
def fix_viewport():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print(f"❌ {html_file} introuvable")
        return False

    content = html_file.read_text(encoding='utf-8')

    # Corriger le viewport
    viewport_tag = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">'

    if 'viewport' in content:
        content = re.sub(
            r'<meta name="viewport"[^>]*>',
            viewport_tag,
            content
        )
    else:
        content = content.replace(
            '<meta charset="UTF-8">',
            f'<meta charset="UTF-8">\n    {viewport_tag}'
        )

    html_file.write_text(content, encoding='utf-8')
    print("✅ Viewport corrigé dans index.html")
    return True

# ============================================
# 4. CORRIGER LE MENU BURGER dans theme.js
# ============================================
def fix_burger_menu():
    theme_file = JS_DIR / "theme.js"

    if not theme_file.exists():
        print(f"❌ {theme_file} introuvable")
        return False

    content = theme_file.read_text(encoding='utf-8')

    # Rechercher la section navigation mobile
    burger_code = """
    // ============================================
    // NAVIGATION MOBILE BURGER
    // ============================================
    const initMobileNav = () => {
        const burger = document.querySelector('.mobile-menu-toggle');
        const mobileNav = document.querySelector('.mobile-nav');
        const overlay = document.querySelector('.mobile-overlay');

        if (!burger || !mobileNav) {
            console.warn('⚠️ Éléments burger manquants');
            return;
        }

        // Toggle menu
        const toggleMenu = () => {
            const isOpen = burger.classList.contains('active');

            burger.classList.toggle('active');
            mobileNav.classList.toggle('active');
            if (overlay) overlay.classList.toggle('active');
            document.body.style.overflow = isOpen ? '' : 'hidden';

            console.log('🍔 Menu burger:', isOpen ? 'fermé' : 'ouvert');
        };

        // Event listeners
        burger.addEventListener('click', toggleMenu);

        if (overlay) {
            overlay.addEventListener('click', toggleMenu);
        }

        // Fermer au clic sur un lien
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', toggleMenu);
        });

        // Fermer avec Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && burger.classList.contains('active')) {
                toggleMenu();
            }
        });

        console.log('📱 Navigation mobile initialisée');
    };
"""

    # Remplacer ou ajouter
    if 'initMobileNav' in content:
        # Remplacer la fonction existante
        content = re.sub(
            r'const initMobileNav = \(\) => \{[^}]*\};',
            burger_code.strip(),
            content,
            flags=re.DOTALL
        )
    else:
        # Ajouter avant le DOMContentLoaded
        content = content.replace(
            "document.addEventListener('DOMContentLoaded'",
            burger_code + "\n    document.addEventListener('DOMContentLoaded'"
        )

    # S'assurer que initMobileNav est appelé
    if 'initMobileNav();' not in content:
        content = content.replace(
            "initOwlManager();",
            "initOwlManager();\n    initMobileNav();"
        )

    theme_file.write_text(content, encoding='utf-8')
    print("✅ Menu burger corrigé dans theme.js")
    return True

# ============================================
# 5. AJOUTER LES STYLES MOBILE dans theme.css
# ============================================
def fix_mobile_styles():
    css_file = BASE_DIR / "assets" / "css" / "theme.css"

    if not css_file.exists():
        print(f"❌ {css_file} introuvable")
        return False

    content = css_file.read_text(encoding='utf-8')

    mobile_styles = """
/* ============================================
   NAVIGATION MOBILE - BURGER MENU
   ============================================ */

.mobile-menu-toggle {
    display: none;
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 10000;
    background: var(--owl-gradient);
    border: none;
    border-radius: 8px;
    width: 48px;
    height: 48px;
    cursor: pointer;
    padding: 0;
    transition: transform 0.3s ease;
}

.mobile-menu-toggle:hover {
    transform: scale(1.05);
}

.mobile-menu-toggle span {
    display: block;
    width: 24px;
    height: 2px;
    background: white;
    margin: 5px auto;
    transition: all 0.3s ease;
    border-radius: 2px;
}

/* Animation de transformation en X */
.mobile-menu-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(6px, 6px);
}

.mobile-menu-toggle.active span:nth-child(2) {
    opacity: 0;
}

.mobile-menu-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(6px, -6px);
}

/* Menu mobile */
.mobile-nav {
    display: none;
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background: var(--card-bg);
    backdrop-filter: blur(20px);
    z-index: 9999;
    padding: 80px 30px 30px;
    transition: right 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: -5px 0 30px rgba(0,0,0,0.3);
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
    margin: 20px 0;
    opacity: 0;
    transform: translateX(50px);
    animation: slideInRight 0.4s ease forwards;
}

.mobile-nav.active li:nth-child(1) { animation-delay: 0.1s; }
.mobile-nav.active li:nth-child(2) { animation-delay: 0.2s; }
.mobile-nav.active li:nth-child(3) { animation-delay: 0.3s; }
.mobile-nav.active li:nth-child(4) { animation-delay: 0.4s; }
.mobile-nav.active li:nth-child(5) { animation-delay: 0.5s; }

@keyframes slideInRight {
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.mobile-nav a {
    display: block;
    color: var(--text-primary);
    text-decoration: none;
    font-size: 1.1rem;
    font-weight: 500;
    padding: 12px 0;
    transition: all 0.3s ease;
    border-bottom: 2px solid transparent;
}

.mobile-nav a:hover {
    color: var(--owl-primary);
    border-bottom-color: var(--owl-primary);
    transform: translateX(10px);
}

/* Overlay */
.mobile-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    z-index: 9998;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.mobile-overlay.active {
    opacity: 1;
}

/* Media queries */
@media (max-width: 768px) {
    .mobile-menu-toggle {
        display: block;
    }

    .mobile-nav {
        display: block;
    }

    .mobile-overlay {
        display: block;
    }

    /* Cacher la nav desktop */
    nav.desktop-nav {
        display: none !important;
    }
}
"""

    # Ajouter si pas déjà présent
    if 'mobile-menu-toggle' not in content:
        content += '\n' + mobile_styles
        css_file.write_text(content, encoding='utf-8')
        print("✅ Styles mobile ajoutés dans theme.css")
    else:
        print("ℹ️ Styles mobile déjà présents")

    return True

# ============================================
# EXÉCUTION
# ============================================
create_text_animation()
fix_stats_js()
fix_viewport()
fix_burger_menu()
fix_mobile_styles()

print("\n" + "="*50)
print("✅ CORRECTIONS TERMINÉES")
print("="*50)
print("\n📋 Prochaines étapes :")
print("1. Exécuter : python force_push_hibwho.py")
print("2. Attendre 2-3 minutes")
print("3. Tester : https://hibwho.github.io/owlhub1_/")
print("4. F12 → Toggle device toolbar → iPhone SE")
print("5. Cliquer sur le burger (en haut à droite)")
