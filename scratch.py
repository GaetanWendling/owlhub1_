#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rebuild_from_scratch.py
Reconstruction complète du header depuis zéro
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")

print("🦉 RECONSTRUCTION COMPLÈTE DU HEADER")
print("=" * 60)

# ============================================
# RECONSTRUIRE COMPLÈTEMENT LE HEADER
# ============================================
def rebuild_header_completely():
    html_file = BASE_DIR / "index.html"

    if not html_file.exists():
        print("❌ index.html introuvable")
        return False

    content = html_file.read_text(encoding='utf-8')

    print("🔍 Analyse du fichier...")

    # Trouver le <body>
    body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
    if not body_match:
        print("❌ Balise <body> introuvable")
        return False

    body_start = body_match.end()

    # Trouver la première <section> ou <main>
    section_match = re.search(r'<(section|main)[^>]*>', content[body_start:], re.IGNORECASE)
    if not section_match:
        print("❌ Première section introuvable")
        return False

    section_start = body_start + section_match.start()

    print(f"✅ Body commence à : {body_start}")
    print(f"✅ Première section à : {section_start}")

    # Supprimer TOUT ce qui est entre <body> et la première <section>
    before_body = content[:body_start]
    after_section = content[section_start:]

    # Le SEUL header correct
    clean_header = """
    <header>
        <nav class="nav-container">
            <a href="#home" class="logo">
                🦉 <span class="gradient-text">OwlHub</span>
            </a>

            <ul class="nav-links desktop-nav">
                <li><a href="#home">Accueil</a></li>
                <li><a href="#features">Fonctionnalités</a></li>
                <li><a href="#about">À propos</a></li>
                <li><a href="#stats">Statistiques</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>

            <button id="theme-toggle" class="theme-toggle" aria-label="Changer de thème">
                <span class="sun">☀️</span>
                <span class="moon">🌙</span>
            </button>

            <button class="mobile-menu-toggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </nav>

        <nav class="mobile-nav">
            <ul>
                <li><a href="#home">🏠 Accueil</a></li>
                <li><a href="#features">✨ Fonctionnalités</a></li>
                <li><a href="#about">📖 À propos</a></li>
                <li><a href="#stats">📊 Statistiques</a></li>
                <li><a href="#contact">🎯 Contact</a></li>
            </ul>
        </nav>

        <div class="mobile-overlay"></div>
    </header>
"""

    # Reconstruire le fichier
    new_content = before_body + clean_header + "\n    " + after_section

    # Sauvegarder
    html_file.write_text(new_content, encoding='utf-8')
    print("✅ Header reconstruit")

    return True

# ============================================
# VÉRIFICATION ULTRA DÉTAILLÉE
# ============================================
def detailed_verification():
    html_file = BASE_DIR / "index.html"
    content = html_file.read_text(encoding='utf-8')

    print("\n📊 VÉRIFICATION DÉTAILLÉE :")
    print("-" * 60)

    # Compter TOUT
    elements = {
        "<header>": content.count('<header>'),
        "</header>": content.count('</header>'),
        "class=\"logo\"": content.count('class="logo"'),
        "desktop-nav": content.count('desktop-nav'),
        "id=\"theme-toggle\"": content.count('id="theme-toggle"'),
        "class=\"theme-toggle\"": content.count('class="theme-toggle"'),
        "mobile-menu-toggle": content.count('mobile-menu-toggle'),
        "class=\"mobile-nav\"": content.count('class="mobile-nav"'),
        "mobile-overlay": content.count('mobile-overlay'),
    }

    all_ok = True
    for element, count in elements.items():
        if count == 1:
            print(f"✅ {element}: {count}")
        elif count == 0:
            print(f"❌ {element}: {count} (MANQUANT)")
            all_ok = False
        else:
            print(f"⚠️  {element}: {count} (DOUBLON)")
            all_ok = False

    # Extraire et afficher le header complet
    header_match = re.search(r'<header>(.*?)</header>', content, re.DOTALL)
    if header_match:
        header = header_match.group(0)
        lines = [line.strip() for line in header.split('\n') if line.strip()]

        print("\n📄 Contenu du header ({} lignes) :".format(len(lines)))
        for i, line in enumerate(lines[:15], 1):  # Afficher les 15 premières lignes
            preview = line[:70]
            print(f"   {i:2d}. {preview}...")

        if len(lines) > 15:
            print(f"   ... ({len(lines) - 15} lignes supplémentaires)")

    return all_ok

# ============================================
# EXÉCUTION
# ============================================
if rebuild_header_completely():
    if detailed_verification():
        print("\n" + "=" * 60)
        print("✅ RECONSTRUCTION RÉUSSIE - STRUCTURE PROPRE")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("⚠️  RECONSTRUCTION TERMINÉE MAIS DOUBLONS DÉTECTÉS")
        print("=" * 60)

    print("\n📋 Prochaine étape :")
    print("   python force_push_hibwho.py")
else:
    print("\n❌ ÉCHEC DE LA RECONSTRUCTION")
