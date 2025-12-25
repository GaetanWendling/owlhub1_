// ============================================
// OWLHUB - CONFIGURATION PARTICULES
// Système adaptatif jour/nuit avec étoiles/bulles
// ============================================

class OwlParticlesSystem {
    constructor() {
        this.canvas = null;
        this.ctx = null;
        this.particles = [];
        this.particleCount = 100;
        this.connectionDistance = 150;
        this.mouse = { x: null, y: null, radius: 100 };

        this.init();
    }

    init() {
        // Créer le canvas
        this.createCanvas();

        // Générer les particules
        this.generateParticles();

        // Démarrer l'animation
        this.animate();

        // Event listeners
        this.setupEventListeners();

        console.log('✅ Système de particules initialisé');
    }

    createCanvas() {
        // Vérifier si le canvas existe déjà
        let existingCanvas = document.getElementById('particles-canvas');
        if (existingCanvas) {
            existingCanvas.remove();
        }

        // Créer nouveau canvas
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'particles-canvas';
        this.canvas.style.cssText = `
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    z-index: 0 !important; /* ✅ Au-dessus du background mais sous le contenu */
    pointer-events: none !important;
`;

        document.body.prepend(this.canvas);
        this.ctx = this.canvas.getContext('2d');

        // Dimensionner le canvas
        this.resizeCanvas();
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    generateParticles() {
        this.particles = [];
        const isDark = this.isDarkTheme();

        for (let i = 0; i < this.particleCount; i++) {
            this.particles.push(this.createParticle(isDark));
        }
    }

    createParticle(isDark) {
        return {
            x: Math.random() * this.canvas.width,
            y: Math.random() * this.canvas.height,
            size: Math.random() * 3 + 1,
            baseSize: Math.random() * 3 + 1,
            speedX: (Math.random() - 0.5) * 0.5,
            speedY: isDark ?
                Math.random() * 0.3 + 0.1 :  // NEIGE (monte)
                (Math.random() - 0.5) * 0.5,  // BULLES (flottent)
            opacity: Math.random() * 0.5 + 0.3,
            baseOpacity: Math.random() * 0.5 + 0.3,
            twinkle: 0,
            twinkleSpeed: Math.random() * 0.05 + 0.02,
            hue: isDark ? 0 : Math.random() * 60 // Nuance blanc/jaune pour étoiles
        };
    }

    isDarkTheme() {
        return document.documentElement.getAttribute('data-theme') === 'dark';
    }

    drawParticles() {
        const isDark = this.isDarkTheme();

        this.particles.forEach(particle => {
            this.ctx.save();

            if (isDark) {
                // ===== MODE DARK : ÉTOILES SCINTILLANTES =====

                // Effet de scintillement
                const twinkleIntensity = Math.sin(particle.twinkle) * 0.3 + 0.7;
                particle.size = particle.baseSize * twinkleIntensity;
                particle.opacity = particle.baseOpacity * twinkleIntensity;

                // Dessiner l'étoile
                this.ctx.beginPath();
                this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);

                // Couleur blanche avec légère teinte dorée
                const hue = 50 + particle.hue;
                this.ctx.fillStyle = `hsla(${hue}, 100%, 95%, ${particle.opacity})`;

                // Glow effect
                this.ctx.shadowBlur = 15;
                this.ctx.shadowColor = `hsla(${hue}, 100%, 90%, ${particle.opacity})`;

                this.ctx.fill();

                // Ajouter un point brillant au centre
                if (particle.size > 2) {
                    this.ctx.beginPath();
                    this.ctx.arc(particle.x, particle.y, particle.size * 0.3, 0, Math.PI * 2);
                    this.ctx.fillStyle = `rgba(255, 255, 255, ${particle.opacity * 1.5})`;
                    this.ctx.shadowBlur = 20;
                    this.ctx.fill();
                }

            } else {
                // ===== MODE LIGHT : BULLES DOUCES =====

                // Légère pulsation
                const pulse = Math.sin(particle.twinkle * 0.5) * 0.2 + 0.8;
                particle.size = particle.baseSize * pulse;

                // Dessiner la bulle
                this.ctx.beginPath();
                this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);

                // Couleur grise douce
                this.ctx.fillStyle = `rgba(100, 100, 100, ${particle.opacity * 0.3})`;

                // Bordure subtile
                this.ctx.strokeStyle = `rgba(150, 150, 150, ${particle.opacity * 0.5})`;
                this.ctx.lineWidth = 0.5;

                this.ctx.fill();
                this.ctx.stroke();

                // Reflet de bulle (highlight)
                const gradient = this.ctx.createRadialGradient(
                    particle.x - particle.size * 0.3,
                    particle.y - particle.size * 0.3,
                    0,
                    particle.x,
                    particle.y,
                    particle.size
                );
                gradient.addColorStop(0, `rgba(255, 255, 255, ${particle.opacity * 0.8})`);
                gradient.addColorStop(0.4, `rgba(255, 255, 255, ${particle.opacity * 0.2})`);
                gradient.addColorStop(1, 'rgba(255, 255, 255, 0)');

                this.ctx.fillStyle = gradient;
                this.ctx.fill();
            }

            this.ctx.restore();
        });
    }

    connectParticles() {
        const isDark = this.isDarkTheme();

        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.connectionDistance) {
                    const opacity = (1 - distance / this.connectionDistance) * 0.3;

                    this.ctx.beginPath();
                    this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
                    this.ctx.lineTo(this.particles[j].x, this.particles[j].y);

                    if (isDark) {
                        // Lignes dorées pour dark mode
                        this.ctx.strokeStyle = `rgba(255, 215, 100, ${opacity})`;
                    } else {
                        // Lignes grises pour light mode
                        this.ctx.strokeStyle = `rgba(100, 100, 100, ${opacity * 0.5})`;
                    }

                    this.ctx.lineWidth = 0.5;
                    this.ctx.stroke();
                }
            }
        }
    }

    moveParticles() {
        const isDark = this.isDarkTheme();

        this.particles.forEach(particle => {
            // Mouvement horizontal
            particle.x += particle.speedX;

            // Mouvement vertical selon le thème
            if (isDark) {
                // NEIGE : monte doucement
                particle.y -= Math.abs(particle.speedY);
            } else {
                // BULLES : flotte dans toutes les directions
                particle.y += particle.speedY;
            }

            // Scintillement/Pulsation
            particle.twinkle += particle.twinkleSpeed;

            // Interaction avec la souris
            const dx = this.mouse.x - particle.x;
            const dy = this.mouse.y - particle.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < this.mouse.radius && this.mouse.x !== null) {
                const force = (this.mouse.radius - distance) / this.mouse.radius;
                const directionX = dx / distance;
                const directionY = dy / distance;

                particle.x -= directionX * force * 2;
                particle.y -= directionY * force * 2;
            }

            // Rebonds sur les bords
            if (particle.x < 0 || particle.x > this.canvas.width) {
                particle.speedX *= -1;
                particle.x = Math.max(0, Math.min(this.canvas.width, particle.x));
            }

            if (isDark) {
                // Réapparaître en bas si sort en haut
                if (particle.y < 0) {
                    particle.y = this.canvas.height;
                    particle.x = Math.random() * this.canvas.width;
                }
            } else {
                // Rebond vertical pour les bulles
                if (particle.y < 0 || particle.y > this.canvas.height) {
                    particle.speedY *= -1;
                    particle.y = Math.max(0, Math.min(this.canvas.height, particle.y));
                }
            }
        });
    }

    animate() {
        // Couleur de fond selon le thème
        const bgColor = this.isDarkTheme() ? '#0a0a0a' : '#ffffff';
        this.ctx.fillStyle = bgColor;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Dessiner et animer
        this.drawParticles();
        this.connectParticles();
        this.moveParticles();

        // Boucle d'animation
        requestAnimationFrame(() => this.animate());
    }

    setupEventListeners() {
        // Redimensionnement
        window.addEventListener('resize', () => {
            this.resizeCanvas();
            this.generateParticles();
        });

        // Suivi de la souris
        window.addEventListener('mousemove', (e) => {
            this.mouse.x = e.x;
            this.mouse.y = e.y;
        });

        window.addEventListener('mouseout', () => {
            this.mouse.x = null;
            this.mouse.y = null;
        });

        // Changement de thème
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.attributeName === 'data-theme') {
                    console.log('🎨 Thème changé, régénération des particules');
                    this.generateParticles();
                }
            });
        });

        observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ['data-theme']
        });
    }

    // Méthode publique pour régénérer les particules
    refresh() {
        this.generateParticles();
    }
}

// ============================================
// INITIALISATION
// ============================================

let particlesSystem = null;

document.addEventListener('DOMContentLoaded', () => {
    // Vérifier la préférence d'animation
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!prefersReducedMotion) {
        particlesSystem = new OwlParticlesSystem();

        // Rendre accessible globalement
        window.owlParticles = particlesSystem;

        console.log('🦉 OwlHub Particles System activé');
    } else {
        console.log('⚠️ Particules désactivées (prefers-reduced-motion)');
    }
});

// Export pour utilisation externe
if (typeof module !== 'undefined' && module.exports) {
    module.exports = OwlParticlesSystem;
}
