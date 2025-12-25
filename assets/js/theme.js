// theme.js - Gestion du thème clair/sombre
class ThemeManager {
    constructor() {
        this.themeToggle = document.getElementById('theme-toggle');
        this.currentTheme = localStorage.getItem('theme') || 'dark';

        this.init();
    }

    init() {
        // Appliquer le thème sauvegardé
        this.applyTheme(this.currentTheme);

        // Event listener sur le bouton
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', () => this.toggleTheme());
        }
    }

    applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        this.currentTheme = theme;

        // Changer l'image du hibou si présente
        this.updateOwlImage(theme);
    }

    toggleTheme() {
        const newTheme = this.currentTheme === 'dark' ? 'light' : 'dark';
        this.applyTheme(newTheme);

        // Animation du bouton
        this.themeToggle.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            this.themeToggle.style.transform = 'rotate(0deg)';
        }, 300);
    }

    updateOwlImage(theme) {
        const owlImages = document.querySelectorAll('.hero-owl, .page-owl, #page-owl');
        owlImages.forEach(img => {
            if (theme === 'dark') {
                img.src = img.src.replace('owl_light.png', 'owl_dark.png');
            } else {
                img.src = img.src.replace('owl_dark.png', 'owl_light.png');
            }
        });
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    new ThemeManager();
});

// ============================================
// MENU BURGER MOBILE
// ============================================

const burgerMenu = document.getElementById('burger-menu');
const navMenu = document.querySelector('.nav-menu');

if (burgerMenu && navMenu) {
    burgerMenu.addEventListener('click', () => {
        burgerMenu.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Fermer le menu au clic sur un lien
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            burgerMenu.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Fermer le menu au clic en dehors
    document.addEventListener('click', (e) => {
        if (!burgerMenu.contains(e.target) && !navMenu.contains(e.target)) {
            burgerMenu.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
}


// ============================================
// ANIMATION CODE M
// ============================================

function typeCode() {
    const codeM = `let
    Source = Excel.Workbook(
        File.Contents("C:\\Data\\ventes.xlsx")
    ),
    Table = Source{[Name="Données"]}[Data],
    Transform = Table.TransformColumnTypes(
        Table,
        {{"Date", type date}, {"CA", type number}}
    )
in
    Transform`;

    const element = document.getElementById('typing-code');
    if (!element) return;

    let index = 0;
    element.textContent = '';

    function type() {
        if (index < codeM.length) {
            element.textContent += codeM[index];
            index++;
            setTimeout(type, 30);
        }
    }

    setTimeout(type, 1000);
}

// Lancer l'animation
if (document.getElementById('typing-code')) {
    typeCode();
}
