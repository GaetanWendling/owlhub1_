/**
 * theme.js - Gestion du thème et du menu mobile
 */

// ============================================
// GESTION DU THÈME
// ============================================
const themeToggle = {
    button: null,

    init() {
        this.button = document.getElementById('theme-toggle');
        if (!this.button) return;

        // Charger le thème sauvegardé
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);

        // Listener
        this.button.addEventListener('click', () => this.toggle());

        console.log('✅ Theme toggle initialisé');
    },

    toggle() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        // Animation du bouton
        this.button.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            this.button.style.transform = 'rotate(0deg)';
        }, 300);
    }
};

// ============================================
// MENU MOBILE
// ============================================
const mobileNav = {
    burger: null,
    nav: null,
    overlay: null,
    isOpen: false,

    init() {
        // Sélectionner les éléments
        this.burger = document.querySelector('.mobile-menu-toggle');
        this.nav = document.querySelector('.mobile-nav');
        this.overlay = document.querySelector('.mobile-overlay');

        if (!this.burger || !this.nav || !this.overlay) {
            console.warn('⚠️ Éléments mobile manquants');
            return;
        }

        // Listeners
        this.burger.addEventListener('click', () => this.toggle());
        this.overlay.addEventListener('click', () => this.close());

        // Fermer au clic sur un lien
        this.nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                setTimeout(() => this.close(), 300);
            });
        });

        console.log('✅ Menu mobile initialisé');
    },

    toggle() {
        this.isOpen ? this.close() : this.open();
    },

    open() {
        this.isOpen = true;
        this.burger.classList.add('active');
        this.nav.classList.add('active');
        this.overlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // Bloquer le scroll
        console.log('📱 Menu ouvert');
    },

    close() {
        this.isOpen = false;
        this.burger.classList.remove('active');
        this.nav.classList.remove('active');
        this.overlay.classList.remove('active');
        document.body.style.overflow = ''; // Restaurer le scroll
        console.log('📱 Menu fermé');
    }
};

// ============================================
// INITIALISATION AU CHARGEMENT
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    console.log('🦉 Initialisation theme.js');

    themeToggle.init();
    mobileNav.init();

    console.log('✅ theme.js chargé');
});

// Export pour debug
window.mobileNav = mobileNav;
window.themeToggle = themeToggle;
