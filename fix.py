#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_final_site.py
Corrections finales pour owlhub_
- Orange → Rouge (#ef4444)
- Fenêtre code M fonctionnelle
- Page header réduite (padding: 6rem → 3rem)
- Menu burger visible mobile
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 CORRECTIONS FINALES - owlhub_")
print("=" * 50)

# ============================================
# 1. CORRECTION CSS : Orange → Rouge
# ============================================
def fix_css():
    css_file = BASE_DIR / "assets" / "css" / "style.css"

    if not css_file.exists():
        print(f"❌ Fichier introuvable : {css_file}")
        return

    content = css_file.read_text(encoding='utf-8')

    # Remplacer TOUTES les occurrences d'orange
    replacements = [
        ('#f97316', '#ef4444'),  # Orange → Rouge
        ('#fb923c', '#ef4444'),  # Orange clair → Rouge
        ('#ea580c', '#dc2626'),  # Orange foncé → Rouge foncé
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    # S'assurer que le gradient est rouge uniquement
    content = re.sub(
        r'--gradient-end:\s*#[a-fA-F0-9]{6};',
        '--gradient-end: #dc2626;',
        content
    )

    css_file.write_text(content, encoding='utf-8')
    print("✅ CSS corrigé : orange → rouge")

# ============================================
# 2. RÉDUIRE LE PAGE HEADER
# ============================================
def fix_page_header():
    css_file = BASE_DIR / "assets" / "css" / "style.css"
    content = css_file.read_text(encoding='utf-8')

    # Chercher la section .page-header et modifier le padding
    content = re.sub(
        r'(\.page-header\s*\{[^}]*padding:\s*)8rem([^;]*;)',
        r'\g<1>3rem\g<2>',
        content
    )

    css_file.write_text(content, encoding='utf-8')
    print("✅ Page header réduit (8rem → 3rem)")

# ============================================
# 3. AJOUTER MENU BURGER MOBILE
# ============================================
def add_mobile_menu():
    css_file = BASE_DIR / "assets" / "css" / "style.css"
    content = css_file.read_text(encoding='utf-8')

    # Vérifier si le burger existe déjà
    if '.burger-menu' in content:
        print("⚠️ Menu burger déjà présent")
        return

    # Ajouter le CSS du burger menu avant les media queries
    burger_css = """

/* ============================================
   MENU BURGER MOBILE
============================================ */

.burger-menu {
    display: none;
    flex-direction: column;
    gap: 4px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
    z-index: 1001;
}

.burger-menu span {
    width: 25px;
    height: 3px;
    background: var(--text-primary);
    border-radius: 2px;
    transition: all 0.3s ease;
}

.burger-menu.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
}

.burger-menu.active span:nth-child(2) {
    opacity: 0;
}

.burger-menu.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -6px);
}

@media (max-width: 768px) {
    .burger-menu {
        display: flex;
    }

    .nav-menu {
        position: fixed;
        top: 70px;
        left: 0;
        right: 0;
        background: var(--bg-primary);
        flex-direction: column;
        padding: 2rem;
        gap: 1rem;
        transform: translateX(-100%);
        transition: transform 0.3s ease;
        box-shadow: var(--shadow-lg);
        z-index: 1000;
    }

    .nav-menu.active {
        transform: translateX(0);
    }

    .nav-link::after {
        display: none;
    }
}
"""

    # Insérer avant @media (max-width: 640px)
    if '@media (max-width: 640px)' in content:
        content = content.replace('@media (max-width: 640px)', burger_css + '\n@media (max-width: 640px)')
    else:
        content += burger_css

    css_file.write_text(content, encoding='utf-8')
    print("✅ CSS menu burger ajouté")

# ============================================
# 4. AJOUTER BURGER DANS HTML
# ============================================
def add_burger_to_html():
    html_files = [
        'index.html',
        'offres.html',
        'methode.html',
        'power-bi.html',
        'a-propos.html',
        'contact.html'
    ]

    for filename in html_files:
        html_file = BASE_DIR / filename

        if not html_file.exists():
            print(f"⚠️ Fichier introuvable : {filename}")
            continue

        content = html_file.read_text(encoding='utf-8')

        # Vérifier si le burger existe déjà
        if 'burger-menu' in content:
            continue

        # Ajouter le burger après .nav-actions
        burger_html = '''
            <button class="burger-menu" id="burger-menu" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>'''

        # Chercher </div> après .nav-actions et insérer avant
        content = re.sub(
            r'(</div>\s*</div>\s*</nav>)',
            burger_html + r'\n        \1',
            content,
            count=1
        )

        html_file.write_text(content, encoding='utf-8')
        print(f"✅ Burger ajouté dans {filename}")

# ============================================
# 5. AJOUTER JS BURGER
# ============================================
def add_burger_js():
    js_file = BASE_DIR / "assets" / "js" / "theme.js"

    if not js_file.exists():
        print(f"❌ Fichier introuvable : {js_file}")
        return

    content = js_file.read_text(encoding='utf-8')

    # Vérifier si le code existe déjà
    if 'burger-menu' in content:
        print("⚠️ JS burger déjà présent")
        return

    burger_js = """

// ============================================
// MENU BURGER MOBILE
// ============================================

const burgerMenu = document.getElementById('burger-menu');
const navMenu = document.querySelector('.nav-menu');

if (burgerMenu && navMenu) {
    burgerMenu.addEventListener('click', () => {
        burgerMenu.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Fermer le menu au clic sur un lien
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            burgerMenu.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Fermer le menu au clic en dehors
    document.addEventListener('click', (e) => {
        if (!burgerMenu.contains(e.target) && !navMenu.contains(e.target)) {
            burgerMenu.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
}
"""

    content += burger_js
    js_file.write_text(content, encoding='utf-8')
    print("✅ JS menu burger ajouté")

# ============================================
# 6. CORRIGER L'ANIMATION CODE M
# ============================================
def fix_code_m():
    js_file = BASE_DIR / "assets" / "js" / "theme.js"
    content = js_file.read_text(encoding='utf-8')

    code_m = """

// ============================================
// ANIMATION CODE M
// ============================================

function typeCode() {
    const codeM = `let
    Source = Excel.Workbook(
        File.Contents("C:\\\\Data\\\\ventes.xlsx")
    ),
    Table = Source{[Name="Données"]}[Data],
    Transform = Table.TransformColumnTypes(
        Table,
        {{"Date", type date}, {"CA", type number}}
    )
in
    Transform`;

    const element = document.getElementById('typing-code');
    if (!element) return;

    let index = 0;
    element.textContent = '';

    function type() {
        if (index < codeM.length) {
            element.textContent += codeM[index];
            index++;
            setTimeout(type, 30);
        }
    }

    setTimeout(type, 1000);
}

// Lancer l'animation
if (document.getElementById('typing-code')) {
    typeCode();
}
"""

    # Remplacer ou ajouter
    if 'function typeCode()' in content:
        content = re.sub(
            r'function typeCode\(\).*?^}',
            code_m.strip(),
            content,
            flags=re.DOTALL | re.MULTILINE
        )
    else:
        content += code_m

    js_file.write_text(content, encoding='utf-8')
    print("✅ Animation code M corrigée")

# ============================================
# EXÉCUTION
# ============================================

try:
    fix_css()
    fix_page_header()
    add_mobile_menu()
    add_burger_to_html()
    add_burger_js()
    fix_code_m()

    print("\n" + "=" * 50)
    print("🎉 CORRECTIONS TERMINÉES")
    print("=" * 50)
    print("\n📋 Résumé des modifications:")
    print("  ✅ Orange → Rouge (#ef4444)")
    print("  ✅ Page header réduit (3rem)")
    print("  ✅ Menu burger mobile ajouté")
    print("  ✅ Animation code M corrigée")

except Exception as e:
    print(f"\n❌ ERREUR : {e}")

print("\n🦉 Script terminé")
