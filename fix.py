#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_final_site.py
Corrections finales :
- Orange → Rouge (#ef4444)
- Fenêtre code M fonctionnelle
- Page header réduite (padding: 6rem → 3rem)
- Menu burger visible mobile
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\site version claude")

print("🦉 CORRECTIONS FINALES")
print("=" * 50)

# ============================================
# 1. CORRECTION CSS : Orange → Rouge
# ============================================
def fix_css():
    css_file = BASE_DIR / "assets" / "css" / "style.css"
    content = css_file.read_text(encoding='utf-8')

    # Remplacer TOUTES les occurrences d'orange
    replacements = [
        ('#f97316', '#ef4444'),  # Orange → Rouge
        ('#fb923c', '#ef4444'),  # Orange clair → Rouge
        ('orange', 'red'),       # Mot clé
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
        r'\.page-header\s*\{[^}]*padding:\s*8rem[^;]*;',
        '.page-header {\n    padding: 3rem 0 2rem;',
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

    # Ajouter le CSS du burger menu avant le dernier }
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
    padding: 8px;
}

.burger-menu span {
    width: 24px;
    height: 2px;
    background: var(--text-primary);
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
        background: var(--bg-secondary);
        flex-direction: column;
        padding: 1rem;
        gap: 0;
        transform: translateY(-100%);
        opacity: 0;
        transition: all 0.3s ease;
        border-bottom: 1px solid var(--border);
        box-shadow: var(--shadow-lg);
    }

    .nav-menu.active {
        transform: translateY(0);
        opacity: 1;
    }

    .nav-menu li {
        width: 100%;
        border-bottom: 1px solid var(--border);
    }

    .nav-menu li:last-child {
        border-bottom: none;
    }

    .nav-link {
        display: block;
        padding: 1rem;
    }
}
"""

    content += burger_css
    css_file.write_text(content, encoding='utf-8')
    print("✅ CSS burger menu ajouté")

# ============================================
# 4. AJOUTER BOUTON BURGER DANS HTML
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
        filepath = BASE_DIR / filename
        if not filepath.exists():
            continue

        content = filepath.read_text(encoding='utf-8')

        # Chercher la fermeture de nav-menu et ajouter le burger après
        if '<button class="burger-menu"' not in content:
            content = content.replace(
                '</ul>',
                '''</ul>
                <button class="burger-menu" aria-label="Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>''',
                1  # Remplacer uniquement la première occurrence
            )

            filepath.write_text(content, encoding='utf-8')
            print(f"✅ Burger ajouté à {filename}")

# ============================================
# 5. SCRIPT JS POUR MENU BURGER
# ============================================
def add_burger_js():
    js_file = BASE_DIR / "assets" / "js" / "theme.js"
    content = js_file.read_text(encoding='utf-8')

    # Ajouter le code du burger menu
    burger_js = """

// ============================================
// MENU BURGER MOBILE
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger-menu');
    const navMenu = document.querySelector('.nav-menu');

    if (burger && navMenu) {
        burger.addEventListener('click', () => {
            burger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Fermer le menu si on clique sur un lien
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                burger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // Fermer le menu si on clique en dehors
        document.addEventListener('click', (e) => {
            if (!burger.contains(e.target) && !navMenu.contains(e.target)) {
                burger.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
});
"""

    content += burger_js
    js_file.write_text(content, encoding='utf-8')
    print("✅ JS burger menu ajouté")

# ============================================
# 6. CORRIGER LE CODE M (Animation typing)
# ============================================
def fix_code_m():
    js_file = BASE_DIR / "assets" / "js" / "theme.js"
    content = js_file.read_text(encoding='utf-8')

    # Remplacer le code d'animation existant
    code_m = """

// ============================================
// ANIMATION CODE M
// ============================================

const codeM = `let
    Source = Excel.CurrentWorkbook(){[Name="Data"]}[Content],
    #"Type modifié" = Table.TransformColumnTypes(Source,{
        {"Date", type date},
        {"Montant", type number},
        {"Catégorie", type text}
    }),
    #"Ajout mois" = Table.AddColumn(#"Type modifié", "Mois",
        each Date.Month([Date]), Int64.Type),
    #"Groupé" = Table.Group(#"Ajout mois", {"Mois"}, {
        {"CA", each List.Sum([Montant]), type nullable number}
    })
in
    #"Groupé"`;

function typeCode() {
    const element = document.getElementById('typing-code');
    if (!element) return;

    let index = 0;
    element.textContent = '';

    function type() {
        if (index < codeM.length) {
            element.textContent += codeM[index];
            index++;
            setTimeout(type, 30); // 30ms par caractère
        }
    }

    // Démarrer après 1 seconde
    setTimeout(type, 1000);
}

// Lancer l'animation au chargement de la page
if (document.getElementById('typing-code')) {
    typeCode();
}
"""

    # Remplacer l'ancienne fonction ou l'ajouter
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
print("\n🚀 Commandes de déploiement:")
print("  cd C:\\Users\\gaeta\\OneDrive\\Bureau\\site version claude")
print("  git add .")
print('  git commit -m "Fix: rouge + header + burger + code M"')
print("  git push origin main")
