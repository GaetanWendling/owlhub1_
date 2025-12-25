#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
remove_div_nav.py
Supprime le <div class="nav-container"> en ligne 64
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 SUPPRESSION DU DIV NAV-CONTAINER")
print("=" * 60)

html_file = BASE_DIR / "index.html"
content = html_file.read_text(encoding='utf-8')

# ============================================
# TROUVER TOUS LES nav-container
# ============================================
print("\n🔍 Recherche...")

# Trouver les <nav> avec nav-container
nav_pattern = r'<nav[^>]*class="[^"]*nav-container[^"]*"[^>]*>.*?</nav>'
nav_matches = list(re.finditer(nav_pattern, content, re.DOTALL))

# Trouver les <div> avec nav-container
div_pattern = r'<div[^>]*class="[^"]*nav-container[^"]*"[^>]*>.*?</div>'
div_matches = list(re.finditer(div_pattern, content, re.DOTALL))

print(f"   → <nav> nav-container: {len(nav_matches)}")
print(f"   → <div> nav-container: {len(div_matches)}")

if len(nav_matches) == 0:
    print("\n❌ ERREUR : Aucun <nav> nav-container trouvé !")
    exit(1)

if len(div_matches) == 0:
    print("\n✅ Aucun <div> à supprimer")
    exit(0)

# ============================================
# SUPPRIMER LES <div> nav-container
# ============================================
print("\n🗑️  Suppression des <div> nav-container...")

new_content = content

for i, div_match in enumerate(div_matches, 1):
    div_text = div_match.group(0)

    # Position
    start = div_match.start()
    end = div_match.end()
    line_num = content[:start].count('\n') + 1

    # Aperçu
    preview = div_text[:100].replace('\n', ' ')

    print(f"\n   📦 Div #{i}")
    print(f"      Ligne: {line_num}")
    print(f"      Taille: {end - start} caractères")
    print(f"      Aperçu: {preview}...")

    # Supprimer du contenu
    new_content = new_content.replace(div_text, '', 1)
    print(f"      ✅ Supprimé")

# ============================================
# SAUVEGARDER
# ============================================
html_file.write_text(new_content, encoding='utf-8')
print("\n✅ Fichier sauvegardé")

# ============================================
# VÉRIFICATION
# ============================================
print("\n📊 VÉRIFICATION FINALE :")
print("-" * 60)

checks = {
    "Headers <header>": new_content.count('<header>'),
    "Nav <nav> nav-container": len(re.findall(r'<nav[^>]*nav-container', new_content)),
    "Div <div> nav-container": len(re.findall(r'<div[^>]*nav-container', new_content)),
    "Total nav-container": new_content.count('class="nav-container"'),
    "Desktop-nav": new_content.count('desktop-nav'),
    "Mobile-nav": new_content.count('mobile-nav'),
    "Burger": new_content.count('mobile-menu-toggle'),
    "Theme-toggle": new_content.count('id="theme-toggle"'),
}

all_ok = True
for item, count in checks.items():
    if "Div" in item:
        # Pour les div, on veut 0
        if count == 0:
            print(f"✅ {item}: {count}")
        else:
            print(f"❌ {item}: {count}")
            all_ok = False
    else:
        # Pour les autres, on veut 1
        if count == 1:
            print(f"✅ {item}: {count}")
        else:
            print(f"⚠️  {item}: {count}")
            all_ok = False

print("\n" + "=" * 60)
if all_ok:
    print("✅ STRUCTURE PARFAITE")
    print("=" * 60)
    print("\n📋 Prochaine étape :")
    print("   python force_push_hibwho.py")
else:
    print("⚠️  VÉRIFICATION ÉCHOUÉE")
    print("=" * 60)
