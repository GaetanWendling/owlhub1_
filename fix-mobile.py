#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_mobile_issues.py
Corrige le zoom mobile et le menu burger
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 CORRECTION MOBILE")
print("=" * 50)

# ============================================
# 1. CORRIGER LE VIEWPORT DANS index.html
# ============================================
def fix_viewport():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print(f"❌ Fichier introuvable : {html_file}")
        return False

    content = html_file.read_text(encoding='utf-8')

    # Remplacer ou ajouter le viewport correct
    if 'viewport' in content:
        content = re.sub(
            r'<meta name="viewport"[^>]*>',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">',
            content
        )
    else:
        # Ajouter après <meta charset>
        content = content.replace(
            '<meta charset="UTF-8">',
            '<meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
        )

    html_file.write_text(content, encoding='utf-8')
    print("✅ Viewport corrigé dans index.html")
    return True

# ============================================
# 2. CORRIGER LE MENU BURGER DANS theme.js
# ============================================
def fix_burger_menu():
    js_file = BASE_DIR / "assets" / "js" / "theme.js"

    if not js_file.exists():
        print(f"❌ Fichier introuvable : {js_file}")
        return False

    content = js_file.read_text(encoding='utf-8')

    # Supprimer l'ancien code burger s'il existe
    content = re.sub(
        r'// ={40,}\s*// MENU BURGER.*?// ={40,}',
        '',
        content,
        flags=re.DOTALL
    )

    # Ajouter le nouveau code burger fonctionnel
    burger_code = """
// ============================================
// MENU BURGER MOBILE
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    const burgerBtn = document.getElementById('burger-menu');
    const nav = document.querySelector('.nav-links');

    if (burgerBtn && nav) {
        // Clic sur le burger
        burgerBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();

            const isOpen = burgerBtn.classList.contains('active');

            if (isOpen) {
                // Fermer le menu
                burgerBtn.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            } else {
                // Ouvrir le menu
                burgerBtn.classList.add('active');
                nav.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        });

        // Fermer le menu en cliquant sur un lien
        const navLinks = nav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                burgerBtn.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Fermer le menu en cliquant en dehors
        document.addEventListener('click', (e) => {
            if (!nav.contains(e.target) && !burgerBtn.contains(e.target)) {
                burgerBtn.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }
});
"""

    # Ajouter avant la dernière ligne
    content = content.rstrip() + '\n' + burger_code + '\n'

    js_file.write_text(content, encoding='utf-8')
    print("✅ Menu burger corrigé dans theme.js")
    return True

# ============================================
# 3. CORRIGER LE CSS DU MENU BURGER
# ============================================
def fix_burger_css():
    css_file = BASE_DIR / "assets" / "css" / "style.css"

    if not css_file.exists():
        print(f"❌ Fichier introuvable : {css_file}")
        return False

    content = css_file.read_text(encoding='utf-8')

    # Supprimer l'ancien CSS burger
    content = re.sub(
        r'/\* ={40,} \*/\s*/\* MENU BURGER.*?/\* ={40,} \*/',
        '',
        content,
        flags=re.DOTALL
    )

    # Ajouter le nouveau CSS burger
    burger_css = """
/* ============================================ */
/* MENU BURGER MOBILE */
/* ============================================ */

.burger-menu {
    display: none;
    flex-direction: column;
    gap: 6px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 10px;
    z-index: 1001;
}

.burger-menu span {
    width: 30px;
    height: 3px;
    background: var(--text);
    border-radius: 3px;
    transition: all 0.3s ease;
}

/* Animation croix */
.burger-menu.active span:nth-child(1) {
    transform: rotate(45deg) translate(9px, 9px);
}

.burger-menu.active span:nth-child(2) {
    opacity: 0;
}

.burger-menu.active span:nth-child(3) {
    transform: rotate(-45deg) translate(9px, -9px);
}

/* RESPONSIVE MOBILE */
@media (max-width: 768px) {
    .burger-menu {
        display: flex;
    }

    .nav-links {
        position: fixed;
        top: 70px;
        left: 0;
        right: 0;
        background: var(--card);
        flex-direction: column;
        gap: 0;
        padding: 2rem;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        max-height: calc(100vh - 70px);
        overflow-y: auto;
    }

    .nav-links.active {
        transform: translateX(0);
    }

    .nav-links a {
        padding: 1rem 0;
        border-bottom: 1px solid var(--border);
        width: 100%;
        text-align: center;
    }

    .nav-links a:last-child {
        border-bottom: none;
    }
}
"""

    # Ajouter avant les dernières media queries
    if '@media (max-width: 768px)' in content:
        # Remplacer la section mobile existante
        content = re.sub(
            r'@media \(max-width: 768px\) \{[^}]*\.nav-links[^}]*\}[^}]*\}',
            burger_css,
            content
        )
    else:
        content += '\n' + burger_css

    css_file.write_text(content, encoding='utf-8')
    print("✅ CSS burger corrigé")
    return True

# ============================================
# EXÉCUTION
# ============================================
try:
    success = True
    success &= fix_viewport()
    success &= fix_burger_menu()
    success &= fix_burger_css()

    if success:
        print("\n" + "=" * 50)
        print("✅ CORRECTIONS APPLIQUÉES")
        print("=" * 50)
        print("\n📋 Modifications :")
        print("  ✅ Viewport optimisé mobile")
        print("  ✅ Menu burger fonctionnel")
        print("  ✅ Animation X corrigée")

        print("\n🚀 Prochaine étape :")
        print("  python force_push.py")
    else:
        print("\n❌ Certaines corrections ont échoué")

except Exception as e:
    print(f"\n❌ ERREUR : {e}")
    import traceback
    traceback.print_exc()

print("\n🦉 Script terminé")
