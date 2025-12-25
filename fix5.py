#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_theme_buttons.py
Supprime les boutons theme en double
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 CORRECTION BOUTONS THEME")
print("=" * 60)

# ============================================
# NETTOYER LES BOUTONS THEME
# ============================================
def fix_theme_buttons():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print("❌ index.html introuvable")
        return False

    content = html_file.read_text(encoding='utf-8')

    # Pattern pour détecter TOUS les boutons theme
    patterns = [
        r'<button[^>]*id=["\']theme-toggle["\'][^>]*>.*?</button>',
        r'<button[^>]*class=["\'][^"\']*theme-toggle[^"\']*["\'][^>]*>.*?</button>',
    ]

    print("🔍 Recherche des boutons theme...")

    all_buttons = []
    for pattern in patterns:
        buttons = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
        all_buttons.extend(buttons)

    print(f"   → {len(all_buttons)} bouton(s) trouvé(s)")

    if len(all_buttons) == 0:
        print("❌ Aucun bouton trouvé")
        return False

    # Afficher les boutons trouvés
    print("\n📋 Boutons détectés :")
    for i, btn in enumerate(all_buttons, 1):
        preview = btn[:80].replace('\n', ' ')
        print(f"   {i}. {preview}...")

    # Supprimer TOUS les boutons theme
    print("\n🧹 Suppression de tous les boutons...")
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)

    # Le bouton theme correct (celui dans le header)
    correct_button = """<button id="theme-toggle" class="theme-toggle" aria-label="Changer de thème">
                <span class="sun">☀️</span>
                <span class="moon">🌙</span>
            </button>"""

    # Trouver la nav-container dans le header
    nav_pattern = r'(<nav class="nav-container">.*?<ul class="nav-links desktop-nav">.*?</ul>)'
    nav_match = re.search(nav_pattern, content, re.DOTALL)

    if nav_match:
        # Insérer le bouton après la nav desktop
        insert_pos = nav_match.end()
        content = content[:insert_pos] + '\n            \n            ' + correct_button + '\n            ' + content[insert_pos:]
        print("✅ Bouton theme unique ajouté dans le header")
    else:
        print("❌ Navigation desktop introuvable")
        return False

    # Sauvegarder
    html_file.write_text(content, encoding='utf-8')
    print("✅ HTML sauvegardé")

    return True

# ============================================
# VÉRIFICATION FINALE
# ============================================
def verify_final():
    html_file = BASE_DIR / "index.html"
    content = html_file.read_text(encoding='utf-8')

    # Compter les éléments
    counts = {
        "Headers": len(re.findall(r'<header[^>]*>', content, re.IGNORECASE)),
        "Boutons theme (id)": len(re.findall(r'id=["\']theme-toggle["\']', content, re.IGNORECASE)),
        "Boutons theme (class)": content.count('theme-toggle'),
        "Boutons burger": content.count('mobile-menu-toggle'),
        "Nav mobile": content.count('mobile-nav'),
        "Overlay": content.count('mobile-overlay')
    }

    print("\n📊 VÉRIFICATION FINALE :")
    print("-" * 60)

    for item, count in counts.items():
        if "theme" in item.lower():
            status = "✅" if count == 1 else "⚠️ " if count > 1 else "❌"
        else:
            status = "✅" if count >= 1 else "❌"
        print(f"{status} {item}: {count}")

    # Vérifier la structure du header
    header_match = re.search(r'<header>(.*?)</header>', content, re.DOTALL)
    if header_match:
        header_content = header_match.group(1)
        print("\n📋 Contenu du header :")
        print(f"   → Logo: {'✅' if 'logo' in header_content else '❌'}")
        print(f"   → Nav desktop: {'✅' if 'desktop-nav' in header_content else '❌'}")
        print(f"   → Theme toggle: {'✅' if 'theme-toggle' in header_content else '❌'}")
        print(f"   → Burger: {'✅' if 'mobile-menu-toggle' in header_content else '❌'}")
        print(f"   → Nav mobile: {'✅' if 'mobile-nav' in header_content else '❌'}")
        print(f"   → Overlay: {'✅' if 'mobile-overlay' in header_content else '❌'}")

# ============================================
# EXÉCUTION
# ============================================
if fix_theme_buttons():
    verify_final()

    print("\n" + "=" * 60)
    print("✅ CORRECTION TERMINÉE")
    print("=" * 60)
    print("\n📋 Prochaine étape :")
    print("   python force_push_hibwho.py")
else:
    print("\n❌ Échec de la correction")
