#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_mobile_dark.py
Corrige le menu mobile dark + header desktop
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"

print("🦉 CORRECTION MENU MOBILE DARK + HEADER")
print("=" * 60)

# Vérifier que le fichier existe
if not CSS_FILE.exists():
    print(f"❌ Fichier non trouvé : {CSS_FILE}")
    exit(1)

content = CSS_FILE.read_text(encoding='utf-8')

# ============================================
# 1. CORRIGER LE MENU MOBILE DARK
# ============================================
print("\n🌙 Correction du menu mobile dark...")

# Trouver la section .mobile-nav
mobile_nav_pattern = r'\.mobile-nav\s*\{[^}]*\}'
mobile_nav_match = re.search(mobile_nav_pattern, content, re.DOTALL)

if mobile_nav_match:
    old_mobile_nav = mobile_nav_match.group(0)

    # Nouveau style avec background qui change selon le thème
    new_mobile_nav = """.mobile-nav {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background: var(--bg-primary);
    backdrop-filter: blur(10px);
    padding: 6rem 2rem 2rem;
    transition: right 0.3s ease;
    z-index: 999;
    box-shadow: -2px 0 20px rgba(0, 0, 0, 0.1);
}"""

    content = content.replace(old_mobile_nav, new_mobile_nav)
    print("   ✅ .mobile-nav corrigé")
else:
    print("   ⚠️  .mobile-nav non trouvé, ajout...")
    # Ajouter avant @media queries
    media_pos = content.find('@media')
    if media_pos > 0:
        new_mobile_nav = """
.mobile-nav {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background: var(--bg-primary);
    backdrop-filter: blur(10px);
    padding: 6rem 2rem 2rem;
    transition: right 0.3s ease;
    z-index: 999;
    box-shadow: -2px 0 20px rgba(0, 0, 0, 0.1);
}

"""
        content = content[:media_pos] + new_mobile_nav + content[media_pos:]
        print("   ✅ .mobile-nav ajouté")

# Corriger aussi les liens du mobile-nav
mobile_nav_a_pattern = r'\.mobile-nav\s+a\s*\{[^}]*\}'
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
}"""

    content = content.replace(old_mobile_nav_a, new_mobile_nav_a)
    print("   ✅ .mobile-nav a corrigé")
else:
    print("   ⚠️  .mobile-nav a non trouvé, ajout...")
    # Ajouter après .mobile-nav
    mobile_nav_pos = content.find('.mobile-nav {')
    if mobile_nav_pos > 0:
        # Trouver la fin du bloc .mobile-nav
        bracket_count = 0
        pos = mobile_nav_pos
        while pos < len(content):
            if content[pos] == '{':
                bracket_count += 1
            elif content[pos] == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    new_mobile_nav_a = """

.mobile-nav a {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    color: var(--text-primary);
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.2s ease;
    font-size: 1.1rem;
}"""
                    content = content[:pos+1] + new_mobile_nav_a + content[pos+1:]
                    print("   ✅ .mobile-nav a ajouté")
                    break
            pos += 1

# ============================================
# 2. CORRIGER LE HEADER DESKTOP
# ============================================
print("\n💻 Correction du header desktop...")

# Trouver le header
header_pattern = r'header\s*\{[^}]*\}'
header_match = re.search(header_pattern, content, re.DOTALL)

if header_match:
    old_header = header_match.group(0)

    # Nouveau style : plus compact
    new_header = """header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: var(--bg-primary);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    z-index: 1000;
    padding: 0;
}"""

    content = content.replace(old_header, new_header)
    print("   ✅ header corrigé")
else:
    print("   ⚠️  header non trouvé")

# Corriger le nav-container
nav_container_pattern = r'\.nav-container\s*\{[^}]*\}'
nav_container_match = re.search(nav_container_pattern, content, re.DOTALL)

if nav_container_match:
    old_nav_container = nav_container_match.group(0)

    new_nav_container = """.nav-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}"""

    content = content.replace(old_nav_container, new_nav_container)
    print("   ✅ .nav-container corrigé")
else:
    print("   ⚠️  .nav-container non trouvé")

# ============================================
# 3. VÉRIFIER LES VARIABLES CSS DARK
# ============================================
print("\n🎨 Vérification des variables dark...")

# Chercher [data-theme="dark"]
dark_theme_pattern = r'\[data-theme="dark"\]\s*\{([^}]+)\}'
dark_theme_match = re.search(dark_theme_pattern, content, re.DOTALL)

if dark_theme_match:
    dark_vars = dark_theme_match.group(1)

    # Vérifier si --bg-primary est bien défini en dark
    if '--bg-primary' in dark_vars:
        print("   ✅ --bg-primary présent en dark")
    else:
        print("   ❌ --bg-primary MANQUANT en dark")

        # Ajouter la variable manquante
        old_dark_section = dark_theme_match.group(0)
        new_dark_section = old_dark_section.replace(
            '{',
            '{\n    --bg-primary: #0a0e27;'
        )
        content = content.replace(old_dark_section, new_dark_section)
        print("   ✅ --bg-primary ajouté")
else:
    print("   ⚠️  [data-theme=\"dark\"] non trouvé")

# ============================================
# SAUVEGARDER
# ============================================
CSS_FILE.write_text(content, encoding='utf-8')
print("\n✅ style.css sauvegardé")

# ============================================
# RÉSUMÉ
# ============================================
print("\n" + "=" * 60)
print("✅ CORRECTIONS APPLIQUÉES")
print("=" * 60)
print("""
📱 Menu mobile dark :
   • Background: var(--bg-primary) au lieu de blanc fixe
   • Texte: var(--text-primary) pour s'adapter au thème

💻 Header desktop :
   • Padding réduit: 1rem au lieu de 1.5rem
   • Plus compact et professionnel

🎨 Variables CSS :
   • --bg-primary vérifié en mode dark
""")

print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
