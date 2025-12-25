// OWLHUB - FICHIER PRINCIPAL
console.log('🦉 OwlHub Main.js chargé');

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    if (counters.length === 0) return;

    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };

        updateCounter();
    });
}

function initStatsObserver() {
    const statsSection = document.querySelector('.stats-section');
    if (!statsSection) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log('👁️ Stats visibles, démarrage animation');
                animateCounters();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    observer.observe(statsSection);
    console.log('✅ Observer des stats activé');
}

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    console.log('✅ Smooth scroll initialisé');
}

function initHeaderScroll() {
    const header = document.querySelector('header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    console.log('✅ Header scroll initialisé');
}

function initCardAnimations() {
    const cards = document.querySelectorAll('.stat-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = ` $ {index * 0.1}s`;
    });
    console.log(`✅  $ {cards.length} cartes interactives initialisées`);
}

function init() {
    console.log('🚀 Initialisation OwlHub...');
    initStatsObserver();
    initSmoothScroll();
    initHeaderScroll();
    initCardAnimations();
    console.log('✅ OwlHub complètement initialisé');
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

window.OwlHub = {
    version: '1.0.0',
    animateCounters,
    init
};

console.log('🦉 OwlHub API disponible via window.OwlHub');
