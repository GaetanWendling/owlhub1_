// ============================================
// OWLHUB - FICHIER PRINCIPAL
// Gestion centralisée des fonctionnalités
// ============================================

console.log('🦉 OwlHub Main.js chargé');

// ============================================
// 1. ANIMATION DES COMPTEURS
// ============================================
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');

    if (counters.length === 0) {
        console.log('⚠️ Aucun compteur trouvé');
        return;
    }

    console.log(`📊 ${counters.length} compteurs détectés`);

    counters.forEach((counter, index) => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000; // 2 secondes
        const increment = target / (duration / 16); // 60 FPS
        let current = 0;

        console.log(`Compteur ${index + 1}: cible = ${target}`);

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
                console.log(`✅ Compteur ${index + 1} terminé: ${target}`);
            }
        };

        updateCounter();
    });
}

// Observer pour démarrer l'animation quand la section est visible
function observeStats() {
    const statsSection = document.querySelector('.stats-grid');

    if (!statsSection) {
        console.log('⚠️ Section stats-grid non trouvée');
        return;
    }

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log('👁️ Stats visibles, démarrage animation');
                animateCounters();
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    statsObserver.observe(statsSection);
    console.log('✅ Observer des stats activé');
}

// ============================================
// 2. SMOOTH SCROLL POUR LA NAVIGATION
// ============================================
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Ignorer les liens vides ou "#"
            if (href === '#' || href === '') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    console.log('✅ Smooth scroll initialisé');
}

// ============================================
// 3. GESTION DU HEADER AU SCROLL
// ============================================
function initHeaderScroll() {
    const header = document.querySelector('header');
    if (!header) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll <= 0) {
            header.style.boxShadow = '0 1px 3px rgba(0,0,0,0.12)';
        } else {
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
        }

        lastScroll = currentScroll;
    });

    console.log('✅ Header scroll initialisé');
}

// ============================================
// 4. GESTION DES CARTES INTERACTIVES
// ============================================
function initCardHover() {
    const cards = document.querySelectorAll('.stat-card, .feature-card, .service-card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    if (cards.length > 0) {
        console.log(`✅ ${cards.length} cartes interactives initialisées`);
    }
}

// ============================================
// 5. FORMULAIRE DE CONTACT
// ============================================
function initContactForm() {
    const form = document.querySelector('.contact-form');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Récupérer les valeurs
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);

        console.log('📧 Formulaire soumis:', data);

        // Afficher un message de confirmation
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;

        submitBtn.textContent = '✅ Message envoyé !';
        submitBtn.style.background = '#28a745';

        setTimeout(() => {
            submitBtn.textContent = originalText;
            submitBtn.style.background = '';
            this.reset();
        }, 3000);
    });

    console.log('✅ Formulaire de contact initialisé');
}

// ============================================
// 6. LAZY LOADING DES IMAGES
// ============================================
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');

    if (images.length === 0) return;

    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
    console.log(`✅ Lazy loading activé pour ${images.length} images`);
}

// ============================================
// 7. ANIMATION D'APPARITION AU SCROLL
// ============================================
function initScrollAnimations() {
    const elements = document.querySelectorAll('.fade-in, .slide-in');

    if (elements.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(el => observer.observe(el));
    console.log(`✅ Animations au scroll activées pour ${elements.length} éléments`);
}

// ============================================
// 8. DÉTECTION MOBILE
// ============================================
function isMobile() {
    return window.innerWidth <= 768;
}

// ============================================
// INITIALISATION GLOBALE
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Initialisation OwlHub...');

    // Initialiser toutes les fonctionnalités
    observeStats();
    initSmoothScroll();
    initHeaderScroll();
    initCardHover();
    initContactForm();
    initLazyLoading();
    initScrollAnimations();

    // Log final
    console.log('✅ OwlHub complètement initialisé');
    console.log(`📱 Mode: ${isMobile() ? 'Mobile' : 'Desktop'}`);
});

// ============================================
// GESTION DU RESIZE
// ============================================
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        console.log(`🔄 Resize détecté: ${window.innerWidth}x${window.innerHeight}`);
    }, 250);
});

// ============================================
// EXPORTS POUR UTILISATION EXTERNE
// ============================================
window.OwlHub = {
    animateCounters,
    isMobile,
    version: '1.0.0'
};

console.log('🦉 OwlHub API disponible via window.OwlHub');
