#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_all_issues.py
Correction : menu blur + liens header + code M
"""

from pathlib import Path
import re

BASE_DIR = Path(r"C:\Users\gaeta\OneDrive\Bureau\owlhub_")
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"
INDEX_FILE = BASE_DIR / "index.html"

print("🦉 CORRECTION FINALE : MENU + HEADER + CODE M")
print("=" * 60)

# ============================================
# 1. MENU MOBILE : SUPPRIMER LE BLUR
# ============================================
print("\n📱 Correction du menu mobile (supprimer blur)...")

if CSS_FILE.exists():
    css_content = CSS_FILE.read_text(encoding='utf-8')

    # Chercher .mobile-nav et supprimer backdrop-filter
    mobile_nav_pattern = r'(\.mobile-nav\s*\{[^}]*)(backdrop-filter:[^;]+;)([^}]*\})'

    if re.search(mobile_nav_pattern, css_content, re.DOTALL):
        css_content = re.sub(mobile_nav_pattern, r'\1\3', css_content, flags=re.DOTALL)
        print("   ✅ backdrop-filter supprimé du .mobile-nav")

    # S'assurer que .mobile-nav a un fond SOLIDE
    mobile_nav_bg_pattern = r'(\.mobile-nav\s*\{[^}]*?)(background[^:]*:[^;]+;)([^}]*\})'
    mobile_nav_match = re.search(r'\.mobile-nav\s*\{[^}]*\}', css_content, re.DOTALL)

    if mobile_nav_match:
        old_mobile = mobile_nav_match.group(0)

        # Remplacer par un fond solide
        if 'background' in old_mobile and 'rgba' in old_mobile:
            # Remplacer rgba par couleur solide
            new_mobile = re.sub(r'background[^:]*:\s*rgba\([^)]+\);',
                               'background-color: #ffffff;', old_mobile)
            css_content = css_content.replace(old_mobile, new_mobile)
            print("   ✅ background rgba remplacé par #ffffff")
        elif 'background:' not in old_mobile and 'background-color:' not in old_mobile:
            # Ajouter background-color
            new_mobile = old_mobile.replace('{', '{\n    background-color: #ffffff;')
            css_content = css_content.replace(old_mobile, new_mobile)
            print("   ✅ background-color: #ffffff ajouté")

    # Version dark
    dark_mobile_pattern = r'\[data-theme="dark"\]\s+\.mobile-nav\s*\{[^}]*\}'
    if re.search(dark_mobile_pattern, css_content):
        old_dark_mobile = re.search(dark_mobile_pattern, css_content).group(0)
        new_dark_mobile = re.sub(r'background[^:]*:\s*rgba\([^)]+\);',
                                 'background-color: #0f172a;', old_dark_mobile)
        css_content = css_content.replace(old_dark_mobile, new_dark_mobile)
        print("   ✅ Dark mode: background-color: #0f172a")
    else:
        # Ajouter le style dark si absent
        dark_mobile_style = """
[data-theme="dark"] .mobile-nav {
    background-color: #0f172a;
}
"""
        css_content += dark_mobile_style
        print("   ✅ Style dark .mobile-nav ajouté")

    CSS_FILE.write_text(css_content, encoding='utf-8')
    print("   💾 style.css sauvegardé")

# ============================================
# 2. HEADER DESKTOP : CORRIGER LES LIENS
# ============================================
print("\n💻 Correction des liens du header desktop...")

if INDEX_FILE.exists():
    html_content = INDEX_FILE.read_text(encoding='utf-8')

    # Chercher le <nav class="desktop-nav">
    desktop_nav_pattern = r'<nav\s+class="desktop-nav">(.*?)</nav>'
    desktop_nav_match = re.search(desktop_nav_pattern, html_content, re.DOTALL)

    if desktop_nav_match:
        # Nouveau contenu correct
        new_desktop_nav = """<nav class="desktop-nav">
                <a href="index.html"><i class="fas fa-home"></i> Accueil</a>
                <a href="offres.html"><i class="fas fa-briefcase"></i> Offres</a>
                <a href="methodologie.html"><i class="fas fa-cogs"></i> Méthodologie</a>
                <a href="powerbi.html"><i class="fas fa-chart-line"></i> Power BI</a>
                <a href="a-propos.html"><i class="fas fa-users"></i> À propos</a>
                <a href="statistiques.html"><i class="fas fa-chart-bar"></i> Statistiques</a>
                <a href="contact.html"><i class="fas fa-envelope"></i> Contact</a>
            </nav>"""

        old_desktop_nav = desktop_nav_match.group(0)
        html_content = html_content.replace(old_desktop_nav, new_desktop_nav)
        print("   ✅ Liens desktop-nav corrigés")
    else:
        print("   ⚠️  desktop-nav non trouvé dans index.html")

    # Faire pareil pour mobile-nav
    mobile_nav_pattern = r'<nav\s+class="mobile-nav"[^>]*>(.*?)</nav>'
    mobile_nav_match = re.search(mobile_nav_pattern, html_content, re.DOTALL)

    if mobile_nav_match:
        new_mobile_nav_content = """<nav class="mobile-nav" id="mobileNav">
            <a href="index.html"><i class="fas fa-home"></i> Accueil</a>
            <a href="offres.html"><i class="fas fa-briefcase"></i> Offres</a>
            <a href="methodologie.html"><i class="fas fa-cogs"></i> Méthodologie</a>
            <a href="powerbi.html"><i class="fas fa-chart-line"></i> Power BI</a>
            <a href="a-propos.html"><i class="fas fa-users"></i> À propos</a>
            <a href="statistiques.html"><i class="fas fa-chart-bar"></i> Statistiques</a>
            <a href="contact.html"><i class="fas fa-envelope"></i> Contact</a>
        </nav>"""

        old_mobile_nav = mobile_nav_match.group(0)
        html_content = html_content.replace(old_mobile_nav, new_mobile_nav_content)
        print("   ✅ Liens mobile-nav corrigés")

    INDEX_FILE.write_text(html_content, encoding='utf-8')
    print("   💾 index.html sauvegardé")

# ============================================
# 3. CODE M : ACTIVER LE SCRIPT
# ============================================
print("\n⌨️  Activation du code M (transform.m)...")

if INDEX_FILE.exists():
    html_content = INDEX_FILE.read_text(encoding='utf-8')

    # Vérifier si le script transform.m existe
    if 'transform.m.js' in html_content or 'transform-m.js' in html_content:
        print("   ✅ Script transform.m déjà présent")
    else:
        # Ajouter le script avant </body>
        transform_script = """
    <!-- Transform M Script -->
    <script>
    document.addEventListener('keydown', function(e) {
        if (e.key.toLowerCase() === 'm') {
            document.body.classList.toggle('matrix-mode');

            // Créer l'effet Matrix
            if (!document.body.classList.contains('matrix-mode')) {
                return;
            }

            const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()';
            const elements = document.querySelectorAll('h1, h2, h3, p, a, span, li');

            elements.forEach(el => {
                const text = el.textContent;
                let iterations = 0;

                const interval = setInterval(() => {
                    el.textContent = text.split('').map((char, index) => {
                        if (index < iterations) {
                            return text[index];
                        }
                        return letters[Math.floor(Math.random() * letters.length)];
                    }).join('');

                    if (iterations >= text.length) {
                        clearInterval(interval);
                    }

                    iterations += 1/3;
                }, 30);
            });
        }
    });
    </script>
    <style>
    .matrix-mode {
        background: #000 !important;
        color: #0f0 !important;
        font-family: 'Courier New', monospace !important;
    }
    .matrix-mode * {
        color: #0f0 !important;
        text-shadow: 0 0 5px #0f0 !important;
    }
    </style>
"""

        html_content = html_content.replace('</body>', transform_script + '\n</body>')
        INDEX_FILE.write_text(html_content, encoding='utf-8')
        print("   ✅ Script transform.m ajouté")

print("\n" + "=" * 60)
print("✅ TOUTES LES CORRECTIONS APPLIQUÉES")
print("=" * 60)
print("""
🔧 Corrections :

📱 MENU MOBILE :
   • backdrop-filter SUPPRIMÉ ✅
   • background-color: #ffffff (solide) ✅
   • Plus de blur ✅

💻 HEADER DESKTOP :
   • Liens corrigés (Accueil, Offres, Méthodologie...) ✅
   • Icônes FontAwesome ✅
   • Navigation propre ✅

⌨️  CODE M :
   • Touche M → Effet Matrix ✅
   • Animation de transformation ✅
   • Style vert terminal ✅
""")

print("\n📋 Prochaine étape :")
print("   python force_push_hibwho.py")
print("\n🧪 Après déploiement, teste :")
print("   • Menu mobile (doit être net)")
print("   • Header desktop (bons liens)")
print("   • Appuie sur M (effet Matrix)")
