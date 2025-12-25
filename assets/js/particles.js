// particles.js - Animation de particules interactive
class ParticlesAnimation {
    constructor() {
        this.canvas = document.getElementById('particles-canvas');
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mousePosition = { x: null, y: null };
        this.numberOfParticles = 80;

        this.init();
    }

    init() {
        this.resizeCanvas();
        this.createParticles();
        this.animate();

        // Event listeners
        window.addEventListener('resize', () => this.resizeCanvas());
        window.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        window.addEventListener('mouseout', () => this.handleMouseOut());
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    createParticles() {
        this.particles = [];
        for (let i = 0; i < this.numberOfParticles; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                radius: Math.random() * 2 + 1,
                opacity: Math.random() * 0.5 + 0.2
            });
        }
    }

    handleMouseMove(e) {
        this.mousePosition.x = e.clientX;
        this.mousePosition.y = e.clientY;
    }

    handleMouseOut() {
        this.mousePosition.x = null;
        this.mousePosition.y = null;
    }

    drawParticle(particle) {
        this.ctx.beginPath();
        this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);

        // Couleur adaptée au thème
        const theme = document.documentElement.getAttribute('data-theme');
        const color = theme === 'dark' ? '59, 130, 246' : '239, 68, 68'; // blue ou red

        this.ctx.fillStyle = `rgba(${color}, ${particle.opacity})`;
        this.ctx.fill();
    }

    connectParticles(p1, p2, distance) {
        const maxDistance = 150;
        const opacity = (1 - distance / maxDistance) * 0.3;

        this.ctx.beginPath();
        this.ctx.moveTo(p1.x, p1.y);
        this.ctx.lineTo(p2.x, p2.y);

        const theme = document.documentElement.getAttribute('data-theme');
        const color = theme === 'dark' ? '59, 130, 246' : '239, 68, 68';

        this.ctx.strokeStyle = `rgba(${color}, ${opacity})`;
        this.ctx.lineWidth = 1;
        this.ctx.stroke();
    }

    updateParticle(particle) {
        // Déplacement
        particle.x += particle.vx;
        particle.y += particle.vy;

        // Rebond sur les bords
        if (particle.x < 0 || particle.x > this.canvas.width) {
            particle.vx *= -1;
        }
        if (particle.y < 0 || particle.y > this.canvas.height) {
            particle.vy *= -1;
        }

        // Interaction avec la souris
        if (this.mousePosition.x !== null && this.mousePosition.y !== null) {
            const dx = this.mousePosition.x - particle.x;
            const dy = this.mousePosition.y - particle.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 120) {
                const force = (120 - distance) / 120;
                particle.x -= (dx / distance) * force * 2;
                particle.y -= (dy / distance) * force * 2;
            }
        }
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Mise à jour et dessin des particules
        this.particles.forEach(particle => {
            this.updateParticle(particle);
            this.drawParticle(particle);
        });

        // Connexions entre particules proches
        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 150) {
                    this.connectParticles(this.particles[i], this.particles[j], distance);
                }
            }
        }

        requestAnimationFrame(() => this.animate());
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    new ParticlesAnimation();
});