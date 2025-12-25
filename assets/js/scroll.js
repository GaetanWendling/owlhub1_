// scroll.js - Animations au défilement
class ScrollAnimations {
    constructor() {
        this.elements = document.querySelectorAll('.feature-card, .pricing-card, .method-phase, .value-card, .stat-card');
        this.navbar = document.querySelector('.navbar');

        this.init();
    }

    init() {
        this.observeElements();
        this.handleNavbarScroll();
        window.addEventListener('scroll', () => this.handleNavbarScroll());
    }

    observeElements() {
        const options = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, options);

        this.elements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(20px)';
            element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(element);
        });
    }

    handleNavbarScroll() {
        if (window.scrollY > 50) {
            this.navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
            this.navbar.style.backgroundColor = 'rgba(15, 23, 42, 0.95)';
        } else {
            this.navbar.style.boxShadow = 'none';
            this.navbar.style.backgroundColor = 'rgba(15, 23, 42, 0.8)';
        }
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    new ScrollAnimations();
});