#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clean_duplicates.py
Supprime les doublons dans index.html
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 NETTOYAGE DES DOUBLONS")
print("=" * 60)

# ============================================
# NETTOYER index.html
# ============================================
def clean_html():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print("❌ index.html introuvable")
        return False

    content = html_file.read_text(encoding='utf-8')

    print("📄 Analyse de index.html...")

    # Compter les headers
    headers = re.findall(r'<header[^>]*>.*?</header>', content, re.DOTALL | re.IGNORECASE)
    print(f"   → {len(headers)} header(s) trouvé(s)")

    if len(headers) > 1:
        print("⚠️  Plusieurs headers détectés, suppression...")

        # Supprimer TOUS les headers
        content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL | re.IGNORECASE)

        # Recréer UN SEUL header propre
        new_header = """<header>
        <nav class="nav-container">
            <a href="#home" class="logo">
                🦉 <span class="gradient-text">OwlHub</span>
            </a>

            <!-- Navigation Desktop -->
            <ul class="nav-links desktop-nav">
                <li><a href="#home">Accueil</a></li>
                <li><a href="#features">Fonctionnalités</a></li>
                <li><a href="#about">À propos</a></li>
                <li><a href="#stats">Statistiques</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>

            <!-- Bouton Theme -->
            <button id="theme-toggle" class="theme-toggle" aria-label="Changer de thème">
                <span class="sun">☀️</span>
                <span class="moon">🌙</span>
            </button>

            <!-- Bouton Burger Mobile -->
            <button class="mobile-menu-toggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </nav>

        <!-- Navigation Mobile -->
        <nav class="mobile-nav">
            <ul>
                <li><a href="#home">🏠 Accueil</a></li>
                <li><a href="#features">✨ Fonctionnalités</a></li>
                <li><a href="#about">📖 À propos</a></li>
                <li><a href="#stats">📊 Statistiques</a></li>
                <li><a href="#contact">📧 Contact</a></li>
            </ul>
        </nav>

        <!-- Overlay -->
        <div class="mobile-overlay"></div>
    </header>"""

        # Insérer après <body>
        body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + new_header + '\n' + content[insert_pos:]
            print("✅ Header unique recréé")
        else:
            print("❌ <body> introuvable")
            return False

    # Vérifier les scripts en double
    script_theme = content.count('theme.js')
    script_stats = content.count('stats.js')

    print(f"\n📦 Scripts détectés :")
    print(f"   → theme.js : {script_theme}x")
    print(f"   → stats.js : {script_stats}x")

    if script_theme > 1:
        print("⚠️  theme.js en double, nettoyage...")
        # Garder seulement le dernier
        parts = content.rsplit('<script src="assets/js/theme.js"></script>', script_theme)
        content = ''.join(parts[:-1]) + '<script src="assets/js/theme.js"></script>' + parts[-1]

    if script_stats > 1:
        print("⚠️  stats.js en double, nettoyage...")
        parts = content.rsplit('<script src="assets/js/stats.js"></script>', script_stats)
        content = ''.join(parts[:-1]) + '<script src="assets/js/stats.js"></script>' + parts[-1]

    # Sauvegarder
    html_file.write_text(content, encoding='utf-8')
    print("\n✅ HTML nettoyé")
    return True

# ============================================
# VÉRIFIER LE CSS
# ============================================
def check_css():
    css_file = BASE_DIR / "assets" / "css" / "style.css"

    if not css_file.exists():
        print("❌ style.css introuvable")
        return False

    content = css_file.read_text(encoding='utf-8')

    # Vérifier si les styles mobile sont présents
    mobile_checks = {
        ".mobile-menu-toggle": ".mobile-menu-toggle" in content,
        ".mobile-nav": ".mobile-nav" in content,
        ".mobile-overlay": ".mobile-overlay" in content,
        "Media queries": "@media" in content and "768px" in content
    }

    print("\n🎨 Vérification CSS :")
    all_ok = True
    for check, result in mobile_checks.items():
        status = "✅" if result else "❌"
        print(f"   {status} {check}")
        if not result:
            all_ok = False

    return all_ok

# ============================================
# AFFICHER LA STRUCTURE FINALE
# ============================================
def show_structure():
    html_file = BASE_DIR / "index.html"
    content = html_file.read_text(encoding='utf-8')

    print("\n📊 STRUCTURE FINALE :")
    print("-" * 60)

    checks = {
        "Headers": len(re.findall(r'<header[^>]*>', content, re.IGNORECASE)),
        "Boutons theme": content.count('theme-toggle'),
        "Boutons burger": content.count('mobile-menu-toggle'),
        "Scripts theme.js": content.count('theme.js'),
        "Scripts stats.js": content.count('stats.js')
    }

    for item, count in checks.items():
        status = "✅" if count == 1 else "⚠️ " if count > 1 else "❌"
        print(f"{status} {item}: {count}")

# ============================================
# EXÉCUTION
# ============================================
clean_html()
check_css()
show_structure()

print("\n" + "=" * 60)
print("✅ NETTOYAGE TERMINÉ")
print("=" * 60)
print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
