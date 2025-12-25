#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_final_menu_header.py
Correction DÉFINITIVE du menu mobile + header desktop
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"

print("🦉 CORRECTION FINALE MENU + HEADER")
print("=" * 60)

if not CSS_FILE.exists():
    print(f"❌ Fichier non trouvé : {CSS_FILE}")
    exit(1)

content = CSS_FILE.read_text(encoding='utf-8')

# ============================================
# 1. SUPPRIMER TOUS LES STYLES MOBILE-NAV
# ============================================
print("\n🗑️  Suppression de tous les anciens styles .mobile-nav...")

# Supprimer toutes les occurrences de .mobile-nav et dérivés
patterns_to_remove = [
    r'\.mobile-nav\s*\{[^}]*\}',
    r'\.mobile-nav\.active\s*\{[^}]*\}',
    r'\.mobile-nav\s+a\s*\{[^}]*\}',
    r'\.mobile-nav\s+a:hover\s*\{[^}]*\}',
    r'\.mobile-nav\s+a\s+i\s*\{[^}]*\}',
]

for pattern in patterns_to_remove:
    matches = list(re.finditer(pattern, content, re.DOTALL))
    for match in reversed(matches):
        content = content[:match.start()] + content[match.end():]
        print(f"   ✅ Supprimé : {pattern[:30]}...")

# ============================================
# 2. AJOUTER LES NOUVEAUX STYLES PROPRES
# ============================================
print("\n✨ Ajout des nouveaux styles...")

new_mobile_styles = """
/* ============================================
   MOBILE NAVIGATION - CLEAN & READABLE
   ============================================ */

.mobile-nav {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background-color: #ffffff;
    padding: 6rem 2rem 2rem;
    transition: right 0.3s ease;
    z-index: 999;
    box-shadow: -2px 0 20px rgba(0, 0, 0, 0.15);
    overflow-y: auto;
}

.mobile-nav.active {
    right: 0;
}

.mobile-nav a {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    color: #1e293b;
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.2s ease;
    font-size: 1.05rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.mobile-nav a:hover {
    background-color: #f1f5f9;
    transform: translateX(-4px);
}

.mobile-nav a i {
    font-size: 1.25rem;
    width: 24px;
    text-align: center;
}

/* Dark mode pour mobile-nav */
[data-theme="dark"] .mobile-nav {
    background-color: #0f172a;
}

[data-theme="dark"] .mobile-nav a {
    color: #e2e8f0;
}

[data-theme="dark"] .mobile-nav a:hover {
    background-color: #1e293b;
}
"""

# Insérer avant les @media queries
media_pos = content.find('@media')
if media_pos > 0:
    content = content[:media_pos] + new_mobile_styles + "\n" + content[media_pos:]
    print("   ✅ Styles mobile-nav ajoutés")
else:
    content += new_mobile_styles
    print("   ✅ Styles mobile-nav ajoutés à la fin")

# ============================================
# 3. CORRIGER LE HEADER DESKTOP
# ============================================
print("\n💻 Correction du header desktop...")

# Supprimer les anciens styles header
header_patterns = [
    r'header\s*\{[^}]*\}',
    r'\.header-content\s*\{[^}]*\}',
]

for pattern in header_patterns:
    matches = list(re.finditer(pattern, content, re.DOTALL))
    for match in reversed(matches):
        content = content[:match.start()] + content[match.end():]

# Ajouter le nouveau header propre
new_header_styles = """
/* ============================================
   HEADER DESKTOP - CLEAN & PROFESSIONAL
   ============================================ */

header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: var(--bg-primary);
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    padding: 0;
}

.header-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0.75rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--accent-primary);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-shrink: 0;
}

.desktop-nav {
    display: none;
}

@media (min-width: 768px) {
    .desktop-nav {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        flex: 1;
        justify-content: center;
    }

    .desktop-nav a {
        padding: 0.5rem 1rem;
        color: var(--text-primary);
        text-decoration: none;
        border-radius: 8px;
        transition: all 0.2s ease;
        font-weight: 500;
        font-size: 0.95rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .desktop-nav a:hover {
        background: var(--bg-secondary);
        color: var(--accent-primary);
    }

    .menu-toggle {
        display: none !important;
    }
}
"""

# Insérer avant @media
media_pos = content.find('@media')
if media_pos > 0:
    content = content[:media_pos] + new_header_styles + "\n" + content[media_pos:]
    print("   ✅ Styles header ajoutés")
else:
    content += new_header_styles
    print("   ✅ Styles header ajoutés à la fin")

# ============================================
# 4. VÉRIFIER LES VARIABLES CSS
# ============================================
print("\n🎨 Vérification des variables CSS...")

# Vérifier :root
root_pattern = r':root\s*\{([^}]+)\}'
root_match = re.search(root_pattern, content, re.DOTALL)

if root_match:
    root_vars = root_match.group(1)
    required_vars = {
        '--bg-primary': '#ffffff',
        '--bg-secondary': '#f8fafc',
        '--text-primary': '#1e293b',
        '--accent-primary': '#3b82f6',
    }

    for var_name, var_value in required_vars.items():
        if var_name not in root_vars:
            print(f"   ➕ Ajout de {var_name}")
            old_root = root_match.group(0)
            new_root = old_root.replace('{', f'{{\n    {var_name}: {var_value};')
            content = content.replace(old_root, new_root)
            root_match = re.search(root_pattern, content, re.DOTALL)

print("   ✅ Variables :root vérifiées")

# Vérifier [data-theme="dark"]
dark_pattern = r'\[data-theme="dark"\]\s*\{([^}]+)\}'
dark_match = re.search(dark_pattern, content, re.DOTALL)

if dark_match:
    dark_vars = dark_match.group(1)
    required_dark_vars = {
        '--bg-primary': '#0f172a',
        '--bg-secondary': '#1e293b',
        '--text-primary': '#e2e8f0',
        '--accent-primary': '#60a5fa',
    }

    for var_name, var_value in required_dark_vars.items():
        if var_name not in dark_vars:
            print(f"   ➕ Ajout de {var_name} en dark")
            old_dark = dark_match.group(0)
            new_dark = old_dark.replace('{', f'{{\n    {var_name}: {var_value};')
            content = content.replace(old_dark, new_dark)
            dark_match = re.search(dark_pattern, content, re.DOTALL)

print("   ✅ Variables dark vérifiées")

# ============================================
# SAUVEGARDER
# ============================================
CSS_FILE.write_text(content, encoding='utf-8')

print("\n" + "=" * 60)
print("✅ CORRECTIONS FINALES APPLIQUÉES")
print("=" * 60)
print("""
🔧 Modifications :

📱 MOBILE :
   • backdrop-filter SUPPRIMÉ ❌
   • background-color: #ffffff (light) / #0f172a (dark) ✅
   • font-weight: 600 pour lisibilité ✅
   • Pas de flou, fond SOLIDE ✅

💻 DESKTOP :
   • Header compact (padding: 0.75rem) ✅
   • Navigation horizontale centrée ✅
   • Logo + nav + theme toggle alignés ✅
   • Pas de burger visible ✅

🎨 VARIABLES :
   • :root vérifié ✅
   • [data-theme="dark"] vérifié ✅
""")

print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
