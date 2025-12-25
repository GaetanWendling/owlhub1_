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

document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
    } else if (prefersDark) {
        document.body.setAttribute('data-theme', 'dark');
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.body.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            document.body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    // Initialiser les particules si disponible
    if (typeof particlesJS !== 'undefined') {
        const theme = document.body.getAttribute('data-theme') || 'light';
        const color = theme === 'dark' ? '#ff0000' : '#0066cc';

        particlesJS('particles-js', {
            particles: {
                number: { value: 80 },
                color: { value: color },
                opacity: { value: 0.5 },
                size: { value: 3 },
                move: { enable: true, speed: 2 }
            }
        });
    }
});
