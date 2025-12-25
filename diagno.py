#!/usr/bin/env python3
from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
html_file = BASE_DIR / "index.html"
content = html_file.read_text(encoding='utf-8')

print("🔍 DIAGNOSTIC index.html")
print("=" * 60)

# Vérifier les éléments critiques
checks = {
    "Headers <header>": content.count('<header>'),
    "Footers <footer>": content.count('<footer>'),
    "Nav .nav-container": content.count('class="nav-container"'),
    "Nav desktop-nav": content.count('desktop-nav'),
    "Nav mobile-nav": content.count('mobile-nav'),
    "Bouton theme-toggle": content.count('theme-toggle'),
    "Bouton burger": content.count('mobile-menu-toggle'),
}

for item, count in checks.items():
    status = "✅" if count == 1 else "⚠️ " if count > 1 else "❌"
    print(f"{status} {item}: {count}")

# Chercher les footers positionnés en fixed
css_file = BASE_DIR / "assets" / "css" / "style.css"
if css_file.exists():
    css = css_file.read_text(encoding='utf-8')

    print("\n🎨 CSS du footer:")
    footer_css = re.search(r'footer\s*{([^}]+)}', css, re.DOTALL)
    if footer_css:
        print(footer_css.group(1)[:200])
