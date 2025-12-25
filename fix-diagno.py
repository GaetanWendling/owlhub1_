#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_duplicates.py
Supprime les doublons de nav-container et theme-toggle
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 SUPPRESSION DES DOUBLONS")
print("=" * 60)

def fix_duplicates():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print("❌ index.html introuvable")
        return False

    content = html_file.read_text(encoding='utf-8')

    # ============================================
    # TROUVER TOUS LES NAV-CONTAINER
    # ============================================
    print("\n🔍 Recherche des nav-container...")

    nav_pattern = r'<nav[^>]*class="nav-container"[^>]*>.*?</nav>'
    navs = list(re.finditer(nav_pattern, content, re.DOTALL))

    print(f"   → {len(navs)} nav-container trouvé(s)")

    if len(navs) == 0:
        print("❌ Aucun nav-container trouvé")
        return False

    # Afficher chaque nav trouvé
    for i, nav_match in enumerate(navs, 1):
        nav_content = nav_match.group(0)
        preview = nav_content[:150].replace('\n', ' ')

        # Compter les éléments dans ce nav
        has_logo = 'class="logo"' in nav_content
        has_desktop = 'desktop-nav' in nav_content
        has_mobile = 'mobile-nav' in nav_content
        has_burger = 'mobile-menu-toggle' in nav_content
        has_theme = 'theme-toggle' in nav_content

        print(f"\n   📦 Nav #{i} :")
        print(f"      Position: caractère {nav_match.start()}")
        print(f"      Logo: {'✅' if has_logo else '❌'}")
        print(f"      Desktop-nav: {'✅' if has_desktop else '❌'}")
        print(f"      Mobile-nav: {'✅' if has_mobile else '❌'}")
        print(f"      Burger: {'✅' if has_burger else '❌'}")
        print(f"      Theme: {'✅' if has_theme else '❌'}")
        print(f"      Aperçu: {preview}...")

    # ============================================
    # IDENTIFIER LE BON NAV (celui qui a TOUT)
    # ============================================
    print("\n🎯 Identification du nav complet...")

    complete_nav = None
    complete_nav_index = -1

    for i, nav_match in enumerate(navs):
        nav_content = nav_match.group(0)

        has_all = all([
            'class="logo"' in nav_content,
            'desktop-nav' in nav_content,
            'mobile-nav' in nav_content,
            'mobile-menu-toggle' in nav_content,
            'theme-toggle' in nav_content
        ])

        if has_all:
            complete_nav = nav_match
            complete_nav_index = i
            print(f"   ✅ Nav #{i} est complet (garde celui-ci)")
            break

    if complete_nav is None:
        print("   ⚠️  Aucun nav complet trouvé, on garde le premier")
        complete_nav = navs[0]
        complete_nav_index = 1

    # ============================================
    # SUPPRIMER LES AUTRES NAV
    # ============================================
    print("\n🧹 Suppression des doublons...")

    # Construire le nouveau contenu
    new_content = content

    # Supprimer tous les navs sauf le complet (en commençant par la fin)
    for i, nav_match in reversed(list(enumerate(navs, 1))):
        if i != complete_nav_index:
            print(f"   ❌ Suppression Nav #{i}")
            new_content = new_content[:nav_match.start()] + new_content[nav_match.end():]

    # ============================================
    # TROUVER ET SUPPRIMER LES THEME-TOGGLE EN DOUBLE
    # ============================================
    print("\n🔍 Recherche des theme-toggle...")

    # Chercher dans le nav restant
    nav_match = re.search(nav_pattern, new_content, re.DOTALL)
    if nav_match:
        nav_content = nav_match.group(0)

        # Compter les theme-toggle dans ce nav
        theme_pattern = r'<button[^>]*(?:id="theme-toggle"|class="[^"]*theme-toggle[^"]*")[^>]*>.*?</button>'
        themes = list(re.finditer(theme_pattern, nav_content, re.DOTALL))

        print(f"   → {len(themes)} theme-toggle dans le nav")

        if len(themes) > 1:
            print("   🧹 Suppression des doublons theme...")

            # Garder le premier, supprimer les autres
            themes_to_remove = themes[1:]

            for theme_match in reversed(themes_to_remove):
                # Position relative au début du nav
                theme_start_in_nav = theme_match.start()
                theme_end_in_nav = theme_match.end()

                # Position absolue dans le document
                theme_start = nav_match.start() + theme_start_in_nav
                theme_end = nav_match.start() + theme_end_in_nav

                print(f"      ❌ Suppression theme à position {theme_start}")
                new_content = new_content[:theme_start] + new_content[theme_end:]

    # ============================================
    # SAUVEGARDER
    # ============================================
    html_file.write_text(new_content, encoding='utf-8')
    print("\n✅ Fichier sauvegardé")

    return True

def verify_after_fix():
    html_file = BASE_DIR / "index.html"
    content = html_file.read_text(encoding='utf-8')

    print("\n📊 VÉRIFICATION FINALE :")
    print("-" * 60)

    checks = {
        "Headers <header>": content.count('<header>'),
        "Nav .nav-container": content.count('class="nav-container"'),
        "Nav desktop-nav": content.count('desktop-nav'),
        "Nav mobile-nav": content.count('mobile-nav'),
        "Bouton theme-toggle (id)": content.count('id="theme-toggle"'),
        "Bouton theme-toggle (class)": content.count('class="theme-toggle"'),
        "Bouton burger": content.count('mobile-menu-toggle'),
    }

    all_ok = True
    for item, count in checks.items():
        if count == 1:
            print(f"✅ {item}: {count}")
        else:
            print(f"⚠️  {item}: {count}")
            all_ok = False

    return all_ok

# ============================================
# EXÉCUTION
# ============================================
if fix_duplicates():
    if verify_after_fix():
        print("\n" + "=" * 60)
        print("✅ CORRECTION RÉUSSIE - STRUCTURE PROPRE")
        print("=" * 60)
        print("\n📋 Prochaine étape :")
        print("   python force_push_hibwho.py")
    else:
        print("\n" + "=" * 60)
        print("⚠️  CORRECTION TERMINÉE MAIS VÉRIFICATION ÉCHOUÉE")
        print("=" * 60)
else:
    print("\n❌ ÉCHEC DE LA CORRECTION")
