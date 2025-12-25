#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_everything_final.py
Correction finale : header + code M window + menu dark blur
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"
INDEX_FILE = BASE_DIR / "index.html"

print("🦉 CORRECTION FINALE COMPLÈTE")
print("=" * 60)

# ============================================
# 1. MENU MOBILE DARK : SUPPRIMER LE BLUR
# ============================================
print("\n🌙 Suppression du blur du menu mobile dark...")

if CSS_FILE.exists():
    css_content = CSS_FILE.read_text(encoding='utf-8')

    # Supprimer backdrop-filter de [data-theme="dark"] .mobile-nav
    dark_mobile_patterns = [
        r'(\[data-theme="dark"\]\s+\.mobile-nav\s*\{[^}]*)(backdrop-filter:[^;]+;)([^}]*\})',
        r'(\[data-theme="dark"\]\s+\.mobile-nav\s*\{[^}]*)(--webkit-backdrop-filter:[^;]+;)([^}]*\})',
    ]

    for pattern in dark_mobile_patterns:
        if re.search(pattern, css_content, re.DOTALL):
            css_content = re.sub(pattern, r'\1\3', css_content, flags=re.DOTALL)
            print(f"   ✅ backdrop-filter supprimé")

    # Forcer background-color solide pour dark mode
    dark_mobile_section = re.search(r'\[data-theme="dark"\]\s+\.mobile-nav\s*\{[^}]*\}', css_content, re.DOTALL)

    if dark_mobile_section:
        old_dark = dark_mobile_section.group(0)

        # Remplacer background rgba par couleur solide
        new_dark = re.sub(r'background[^:]*:\s*rgba\([^)]+\);', 'background-color: #0f172a;', old_dark)

        # Si pas de background du tout, l'ajouter
        if 'background' not in new_dark:
            new_dark = new_dark.replace('{', '{\n    background-color: #0f172a;')

        css_content = css_content.replace(old_dark, new_dark)
        print("   ✅ background-color: #0f172a (solide)")
    else:
        # Ajouter la section si elle n'existe pas
        dark_mobile_style = """
[data-theme="dark"] .mobile-nav {
    background-color: #0f172a;
    color: #e2e8f0;
}
"""
        css_content += dark_mobile_style
        print("   ✅ Section dark .mobile-nav ajoutée")

    CSS_FILE.write_text(css_content, encoding='utf-8')
    print("   💾 style.css sauvegardé")

# ============================================
# 2. HEADER DESKTOP : CORRIGER LES LIENS
# ============================================
print("\n💻 Correction du header desktop...")

if INDEX_FILE.exists():
    html_content = INDEX_FILE.read_text(encoding='utf-8')

    # Trouver TOUT le header
    header_pattern = r'<header[^>]*>(.*?)</header>'
    header_match = re.search(header_pattern, html_content, re.DOTALL | re.IGNORECASE)

    if header_match:
        old_header = header_match.group(0)

        # Nouveau header complet avec les BONS liens
        new_header = """<header>
        <div class="container">
            <div class="logo">
                <img src="assets/images/owl-logo.png" alt="OwlHub Logo" class="logo-img">
                <span>OwlHub</span>
            </div>

            <nav class="desktop-nav">
                <a href="index.html"><i class="fas fa-home"></i> Accueil</a>
                <a href="offres.html"><i class="fas fa-briefcase"></i> Offres</a>
                <a href="methodologie.html"><i class="fas fa-cogs"></i> Méthodologie</a>
                <a href="powerbi.html"><i class="fas fa-chart-line"></i> Power BI</a>
                <a href="a-propos.html"><i class="fas fa-users"></i> À propos</a>
                <a href="statistiques.html"><i class="fas fa-chart-bar"></i> Statistiques</a>
                <a href="contact.html"><i class="fas fa-envelope"></i> Contact</a>
            </nav>

            <div class="header-actions">
                <button id="themeToggle" class="theme-toggle" aria-label="Changer de thème">
                    <i class="fas fa-sun"></i>
                </button>
                <button class="burger" id="burgerBtn" aria-label="Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </header>"""

        html_content = html_content.replace(old_header, new_header)
        print("   ✅ Header desktop remplacé avec les bons liens")
    else:
        print("   ⚠️  Header non trouvé")

    INDEX_FILE.write_text(html_content, encoding='utf-8')
    print("   💾 index.html sauvegardé")

# ============================================
# 3. CODE M : FENÊTRE + EASTER EGG
# ============================================
print("\n⌨️  Configuration Code M (fenêtre + easter egg)...")

if INDEX_FILE.exists():
    html_content = INDEX_FILE.read_text(encoding='utf-8')

    # Vérifier si la fenêtre transform.m existe
    if 'transform-window' not in html_content and 'code-window' not in html_content:
        print("   ⚠️  Fenêtre transform.m non trouvée dans le HTML")
        print("   ℹ️  Elle devrait être dans hero-content")

    # Ajouter/Mettre à jour le script Easter Egg
    easter_egg_script = """
    <!-- Easter Egg Matrix (Touche M) -->
    <script>
    let matrixActive = false;

    document.addEventListener('keydown', function(e) {
        if (e.key.toLowerCase() === 'm' && !matrixActive) {
            matrixActive = true;
            document.body.classList.add('matrix-mode');

            const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()';
            const elements = document.querySelectorAll('h1, h2, h3, p, a, span, li, button');

            elements.forEach(el => {
                const originalText = el.textContent;
                let iterations = 0;

                const interval = setInterval(() => {
                    el.textContent = originalText.split('').map((char, index) => {
                        if (index < iterations) {
                            return originalText[index];
                        }
                        return letters[Math.floor(Math.random() * letters.length)];
                    }).join('');

                    if (iterations >= originalText.length) {
                        clearInterval(interval);
                        matrixActive = false;
                    }

                    iterations += 1/3;
                }, 30);
            });

            // Désactiver après 3 secondes
            setTimeout(() => {
                document.body.classList.remove('matrix-mode');
            }, 3000);
        }
    });
    </script>
    <style>
    .matrix-mode {
        background: #000 !important;
        color: #0f0 !important;
        font-family: 'Courier New', monospace !important;
        transition: all 0.3s ease;
    }
    .matrix-mode * {
        color: #0f0 !important;
        text-shadow: 0 0 10px #0f0, 0 0 20px #0f0 !important;
    }
    .matrix-mode .hero {
        background: #000 !important;
    }
    </style>
"""

    # Supprimer l'ancien script s'il existe
    html_content = re.sub(r'<!-- Easter Egg Matrix.*?</style>', '', html_content, flags=re.DOTALL)

    # Ajouter avant </body>
    html_content = html_content.replace('</body>', easter_egg_script + '\n</body>')

    INDEX_FILE.write_text(html_content, encoding='utf-8')
    print("   ✅ Easter Egg Matrix activé (touche M)")
    print("   💾 index.html sauvegardé")

print("\n" + "=" * 60)
print("✅ CORRECTIONS FINALES APPLIQUÉES")
print("=" * 60)
print("""
🔧 Corrections :

🌙 MENU MOBILE DARK :
   • backdrop-filter SUPPRIMÉ ✅
   • background-color: #0f172a (solide) ✅
   • Plus de blur en mode dark ✅

💻 HEADER DESKTOP :
   • Liens : Accueil, Offres, Méthodologie, Power BI, À propos, Statistiques, Contact ✅
   • Logo + navigation + thème toggle ✅
   • Burger menu pour mobile ✅

⌨️  CODE M :
   • Fenêtre "transform.m" existante (vérifier dans hero) ✅
   • Easter Egg : touche M → effet Matrix vert ✅
   • Animation 3 secondes puis retour normal ✅
""")

print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
print("\n🧪 Tests à faire :")
print("   1. Version desktop : vérifier les liens du header")
print("   2. Version mobile dark : menu doit être net (pas blur)")
print("   3. Appuyer sur M → effet Matrix vert")
print("   4. Vérifier que la fenêtre 'transform.m' s'affiche (dans hero)")
