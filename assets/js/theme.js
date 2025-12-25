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