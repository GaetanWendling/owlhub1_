#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diagnose_site.py
Diagnostic complet du site avant correction
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 DIAGNOSTIC COMPLET")
print("=" * 60)

# ============================================
# 1. VÉRIFIER LA STRUCTURE HTML
# ============================================
def check_html():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print("❌ index.html introuvable")
        return

    content = html_file.read_text(encoding='utf-8')

    print("\n📄 ANALYSE index.html")
    print("-" * 60)

    checks = {
        "Viewport": '<meta name="viewport"' in content,
        "Burger HTML": 'mobile-menu-toggle' in content,
        "Mobile nav": 'mobile-nav' in content,
        "Overlay": 'mobile-overlay' in content,
        "Script theme.js": 'theme.js' in content,
        "Script stats.js": 'stats.js' in content,
        "Script particles": 'particles' in content,
    }

    for check, result in checks.items():
        status = "✅" if result else "❌"
        print(f"{status} {check}")

    # Afficher le header
    header_match = re.search(r'<header[^>]*>.*?</header>', content, re.DOTALL)
    if header_match:
        print("\n📌 CONTENU DU HEADER :")
        print(header_match.group(0)[:500])

# ============================================
# 2. VÉRIFIER LES FICHIERS JS
# ============================================
def check_js_files():
    js_dir = BASE_DIR / "assets" / "js"

    print("\n\n📦 FICHIERS JAVASCRIPT")
    print("-" * 60)

    required_files = [
        "theme.js",
        "stats.js",
        "particles-config.js",
        "text-animation.js"
    ]

    for filename in required_files:
        file_path = js_dir / filename
        exists = file_path.exists()
        status = "✅" if exists else "❌"

        if exists:
            size = file_path.stat().st_size
            print(f"{status} {filename} ({size} bytes)")

            # Vérifier le contenu
            content = file_path.read_text(encoding='utf-8')
            if filename == "theme.js":
                has_burger = 'mobile-menu-toggle' in content
                has_init = 'initMobileNav' in content
                print(f"   └─ Burger code: {'✅' if has_burger else '❌'}")
                print(f"   └─ Init function: {'✅' if has_init else '❌'}")

            if filename == "stats.js":
                has_stats_obj = 'const stats = {' in content or 'const stats={' in content
                print(f"   └─ Stats object: {'✅' if has_stats_obj else '❌'}")
        else:
            print(f"{status} {filename} - MANQUANT")

# ============================================
# 3. VÉRIFIER LES CSS
# ============================================
def check_css():
    css_files = [
        BASE_DIR / "assets" / "css" / "style.css",
        BASE_DIR / "assets" / "css" / "theme.css"
    ]

    print("\n\n🎨 FICHIERS CSS")
    print("-" * 60)

    for css_file in css_files:
        if css_file.exists():
            content = css_file.read_text(encoding='utf-8')
            has_burger = 'mobile-menu-toggle' in content
            has_mobile_nav = 'mobile-nav' in content
            has_media = '@media' in content

            print(f"\n✅ {css_file.name}")
            print(f"   └─ Burger styles: {'✅' if has_burger else '❌'}")
            print(f"   └─ Mobile nav: {'✅' if has_mobile_nav else '❌'}")
            print(f"   └─ Media queries: {'✅' if has_media else '❌'}")
        else:
            print(f"❌ {css_file.name} - MANQUANT")

# ============================================
# EXÉCUTION
# ============================================
check_html()
check_js_files()
check_css()

print("\n" + "=" * 60)
print("📊 DIAGNOSTIC TERMINÉ")
print("=" * 60)
