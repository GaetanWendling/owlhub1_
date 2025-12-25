#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_blur_menu.py
Enlève le blur du menu mobile
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"

print("🦉 CORRECTION DU BLUR DU MENU MOBILE")
print("=" * 60)

if not CSS_FILE.exists():
    print(f"❌ Fichier non trouvé : {CSS_FILE}")
    exit(1)

content = CSS_FILE.read_text(encoding='utf-8')

# ============================================
# ENLEVER LE BACKDROP-FILTER DU MOBILE-NAV
# ============================================
print("\n🔧 Suppression du backdrop-filter...")

# Trouver .mobile-nav
mobile_nav_pattern = r'(\.mobile-nav\s*\{[^}]*\})'
mobile_nav_match = re.search(mobile_nav_pattern, content, re.DOTALL)

if mobile_nav_match:
    old_mobile_nav = mobile_nav_match.group(0)

    # Remplacer backdrop-filter par un fond solide opaque
    new_mobile_nav = """.mobile-nav {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background: var(--bg-primary);
    padding: 6rem 2rem 2rem;
    transition: right 0.3s ease;
    z-index: 999;
    box-shadow: -2px 0 20px rgba(0, 0, 0, 0.3);
    overflow-y: auto;
}"""

    content = content.replace(old_mobile_nav, new_mobile_nav)
    print("   ✅ backdrop-filter supprimé")
    print("   ✅ background: var(--bg-primary) opaque ajouté")
else:
    print("   ❌ .mobile-nav non trouvé")

# ============================================
# AMÉLIORER LE CONTRASTE DES LIENS
# ============================================
print("\n🎨 Amélioration du contraste...")

mobile_nav_a_pattern = r'(\.mobile-nav\s+a\s*\{[^}]*\})'
mobile_nav_a_match = re.search(mobile_nav_a_pattern, content, re.DOTALL)

if mobile_nav_a_match:
    old_mobile_nav_a = mobile_nav_a_match.group(0)

    new_mobile_nav_a = """.mobile-nav a {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    color: var(--text-primary);
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.2s ease;
    font-size: 1.1rem;
    font-weight: 500;
}"""

    content = content.replace(old_mobile_nav_a, new_mobile_nav_a)
    print("   ✅ font-weight: 500 ajouté pour plus de lisibilité")
else:
    print("   ⚠️  .mobile-nav a non trouvé")

# Ajouter le hover si absent
mobile_nav_a_hover_pattern = r'\.mobile-nav\s+a:hover\s*\{[^}]*\}'
mobile_nav_a_hover_match = re.search(mobile_nav_a_hover_pattern, content, re.DOTALL)

if not mobile_nav_a_hover_match:
    print("\n   ➕ Ajout du style :hover...")

    # Trouver où insérer (après .mobile-nav a)
    mobile_nav_a_pos = content.find('.mobile-nav a {')
    if mobile_nav_a_pos > 0:
        # Trouver la fin du bloc
        bracket_count = 0
        pos = mobile_nav_a_pos
        while pos < len(content):
            if content[pos] == '{':
                bracket_count += 1
            elif content[pos] == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    hover_style = """

.mobile-nav a:hover {
    background: rgba(102, 126, 234, 0.1);
    transform: translateX(-5px);
}"""
                    content = content[:pos+1] + hover_style + content[pos+1:]
                    print("   ✅ :hover ajouté")
                    break
            pos += 1

# ============================================
# VÉRIFIER QUE --bg-primary EST OPAQUE EN DARK
# ============================================
print("\n🌙 Vérification du mode dark...")

dark_theme_pattern = r'\[data-theme="dark"\]\s*\{([^}]+)\}'
dark_theme_match = re.search(dark_theme_pattern, content, re.DOTALL)

if dark_theme_match:
    dark_vars = dark_theme_match.group(1)

    # Vérifier --bg-primary
    bg_primary_pattern = r'--bg-primary:\s*([^;]+);'
    bg_primary_match = re.search(bg_primary_pattern, dark_vars)

    if bg_primary_match:
        bg_value = bg_primary_match.group(1).strip()
        print(f"   ℹ️  --bg-primary en dark: {bg_value}")

        # Si c'est rgba avec alpha < 1, le rendre opaque
        if 'rgba' in bg_value and ', 0.' in bg_value:
            print("   ⚠️  Background semi-transparent détecté, correction...")

            old_dark = dark_theme_match.group(0)
            new_dark = old_dark.replace(bg_value, '#0a0e27')
            content = content.replace(old_dark, new_dark)
            print("   ✅ Background opaque: #0a0e27")
        else:
            print("   ✅ Background déjà opaque")
    else:
        print("   ❌ --bg-primary non trouvé, ajout...")
        old_dark = dark_theme_match.group(0)
        new_dark = old_dark.replace('{', '{\n    --bg-primary: #0a0e27;')
        content = content.replace(old_dark, new_dark)
        print("   ✅ --bg-primary: #0a0e27 ajouté")

# ============================================
# SAUVEGARDER
# ============================================
CSS_FILE.write_text(content, encoding='utf-8')

print("\n" + "=" * 60)
print("✅ CORRECTIONS APPLIQUÉES")
print("=" * 60)
print("""
🔧 Modifications :
   • backdrop-filter: blur(10px) ❌ SUPPRIMÉ
   • background: var(--bg-primary) ✅ OPAQUE
   • font-weight: 500 ✅ AJOUTÉ
   • :hover effect ✅ VÉRIFIÉ
   • --bg-primary en dark ✅ OPAQUE

📱 Résultat attendu :
   • Menu net et lisible
   • Contraste optimal dark/light
   • Transitions fluides
""")

print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
