#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
find_all_navs.py
Trouve TOUS les éléments avec class="nav-container"
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 RECHERCHE EXHAUSTIVE DES NAV-CONTAINER")
print("=" * 60)

html_file = BASE_DIR / "index.html"
content = html_file.read_text(encoding='utf-8')

# ============================================
# CHERCHER TOUS LES ÉLÉMENTS AVEC nav-container
# ============================================
print("\n🔍 Recherche de TOUS les éléments avec class=\"nav-container\"...")

# Pattern plus large : n'importe quelle balise avec cette classe
pattern = r'<(\w+)[^>]*class="[^"]*nav-container[^"]*"[^>]*>.*?</\1>'

matches = list(re.finditer(pattern, content, re.DOTALL))

print(f"\n   → {len(matches)} élément(s) trouvé(s)")

for i, match in enumerate(matches, 1):
    element = match.group(0)
    tag = match.group(1)

    # Position dans le fichier
    start = match.start()
    end = match.end()

    # Calculer le numéro de ligne
    lines_before = content[:start].count('\n')
    line_num = lines_before + 1

    # Aperçu du contenu
    preview = element[:200].replace('\n', ' ').replace('  ', ' ')

    # Compter les sous-éléments
    has_logo = 'class="logo"' in element
    has_desktop = 'desktop-nav' in element
    has_mobile_nav = 'mobile-nav' in element
    has_burger = 'mobile-menu-toggle' in element
    has_theme = 'theme-toggle' in element

    print(f"\n   {'='*56}")
    print(f"   📦 ÉLÉMENT #{i}")
    print(f"   {'='*56}")
    print(f"   Balise: <{tag}>")
    print(f"   Ligne: {line_num}")
    print(f"   Position: {start} → {end}")
    print(f"   Taille: {end - start} caractères")
    print(f"\n   Contenu:")
    print(f"      Logo: {'✅' if has_logo else '❌'}")
    print(f"      Desktop-nav: {'✅' if has_desktop else '❌'}")
    print(f"      Mobile-nav: {'✅' if has_mobile_nav else '❌'}")
    print(f"      Burger: {'✅' if has_burger else '❌'}")
    print(f"      Theme: {'✅' if has_theme else '❌'}")
    print(f"\n   Aperçu:")
    print(f"      {preview}...")

# ============================================
# CHERCHER AUSSI LES CLASSES INCOMPLÈTES
# ============================================
print("\n" + "=" * 60)
print("🔍 Recherche des classes partielles 'nav'...")
print("=" * 60)

partial_patterns = [
    (r'class="nav[^"]*"', "class=\"nav...\""),
    (r'class="[^"]*-nav[^"]*"', "class=\"...-nav...\""),
]

for pattern, description in partial_patterns:
    matches = re.findall(pattern, content)
    if matches:
        print(f"\n   {description} : {len(matches)} occurrence(s)")
        for match in set(matches)[:10]:  # Max 10 exemples
            print(f"      → {match}")

# ============================================
# VÉRIFICATION FINALE DES COMPTAGES
# ============================================
print("\n" + "=" * 60)
print("📊 COMPTAGE SIMPLE")
print("=" * 60)

simple_counts = {
    'class="nav-container"': content.count('class="nav-container"'),
    'desktop-nav': content.count('desktop-nav'),
    'mobile-nav': content.count('mobile-nav'),
    'mobile-menu-toggle': content.count('mobile-menu-toggle'),
}

for item, count in simple_counts.items():
    status = "✅" if count == 1 else "⚠️ " if count > 1 else "❌"
    print(f"{status} {item}: {count}")

print("\n" + "=" * 60)
