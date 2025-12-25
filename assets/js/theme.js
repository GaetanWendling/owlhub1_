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

    // ============================================
    // NAVIGATION MOBILE BURGER
    // ============================================
    const initMobileNav = () => {
        const burger = document.querySelector('.mobile-menu-toggle');
        const mobileNav = document.querySelector('.mobile-nav');
        const overlay = document.querySelector('.mobile-overlay');

        if (!burger || !mobileNav) {
            console.warn('⚠️ Éléments burger manquants');
            return;
        }

        // Toggle menu
        const toggleMenu = () => {
            const isOpen = burger.classList.contains('active');

            burger.classList.toggle('active');
            mobileNav.classList.toggle('active');
            if (overlay) overlay.classList.toggle('active');
            document.body.style.overflow = isOpen ? '' : 'hidden';

            console.log('🍔 Menu burger:', isOpen ? 'fermé' : 'ouvert');
        };

        // Event listeners
        burger.addEventListener('click', toggleMenu);

        if (overlay) {
            overlay.addEventListener('click', toggleMenu);
        }

        // Fermer au clic sur un lien
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', toggleMenu);
        });

        // Fermer avec Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && burger.classList.contains('active')) {
                toggleMenu();
            }
        });

        console.log('📱 Navigation mobile initialisée');
    };

    document.addEventListener('DOMContentLoaded', () => {
    new ThemeManager();
});



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

// ============================================
// MENU BURGER MOBILE
// ============================================


    // ============================================
    // NAVIGATION MOBILE BURGER
    // ============================================
    const initMobileNav = () => {
        const burger = document.querySelector('.mobile-menu-toggle');
        const mobileNav = document.querySelector('.mobile-nav');
        const overlay = document.querySelector('.mobile-overlay');

        if (!burger || !mobileNav) {
            console.warn('⚠️ Éléments burger manquants');
            return;
        }

        // Toggle menu
        const toggleMenu = () => {
            const isOpen = burger.classList.contains('active');

            burger.classList.toggle('active');
            mobileNav.classList.toggle('active');
            if (overlay) overlay.classList.toggle('active');
            document.body.style.overflow = isOpen ? '' : 'hidden';

            console.log('🍔 Menu burger:', isOpen ? 'fermé' : 'ouvert');
        };

        // Event listeners
        burger.addEventListener('click', toggleMenu);

        if (overlay) {
            overlay.addEventListener('click', toggleMenu);
        }

        // Fermer au clic sur un lien
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', toggleMenu);
        });

        // Fermer avec Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && burger.classList.contains('active')) {
                toggleMenu();
            }
        });

        console.log('📱 Navigation mobile initialisée');
    };

    document.addEventListener('DOMContentLoaded', () => {
    const burgerBtn = document.getElementById('burger-menu');
    const nav = document.querySelector('.nav-links');

    if (burgerBtn && nav) {
        // Clic sur le burger
        burgerBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();

            const isOpen = burgerBtn.classList.contains('active');

            if (isOpen) {
                // Fermer le menu
                burgerBtn.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            } else {
                // Ouvrir le menu
                burgerBtn.classList.add('active');
                nav.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        });

        // Fermer le menu en cliquant sur un lien
        const navLinks = nav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                burgerBtn.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Fermer le menu en cliquant en dehors
        document.addEventListener('click', (e) => {
            if (!nav.contains(e.target) && !burgerBtn.contains(e.target)) {
                burgerBtn.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }
});

