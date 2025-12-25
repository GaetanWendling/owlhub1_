// theme.js - Gestion du thème + Particles.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎨 Theme.js chargé');

    // ============================================
    // GESTION DU THÈME SOMBRE/CLAIR
    // ============================================
    const themeToggle = document.getElementById('theme-toggle');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('theme');

    // Appliquer le thème sauvegardé ou préférence système
    if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
    } else if (prefersDark) {
        document.body.setAttribute('data-theme', 'dark');
    }

    // Toggle du thème
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.body.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            document.body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);

            // Réinitialiser les particules avec la nouvelle couleur
            if (typeof particlesJS !== 'undefined') {
                initParticles();
            }
        });
    }

    // ============================================
    // INITIALISATION PARTICLES.JS
    // ============================================
    function initParticles() {
        // VÉRIFICATION 1 : La bibliothèque est chargée ?
        if (typeof particlesJS === 'undefined') {
            console.error('❌ particles.js non chargé depuis le CDN');
            return;
        }

        // VÉRIFICATION 2 : Le conteneur existe ?
        const container = document.getElementById('particles-js');
        if (!container) {
            console.error('❌ #particles-js introuvable dans le DOM');
            return;
        }

        console.log('✅ Initialisation de particles.js...');

        // Couleur selon le thème
        const theme = document.body.getAttribute('data-theme') || 'light';
        const particleColor = theme === 'dark' ? '#ff0000' : '#0066cc';

        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 80,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": particleColor
                },
                "shape": {
                    "type": "circle"
                },
                "opacity": {
                    "value": 0.5,
                    "random": false,
                    "anim": {
                        "enable": false,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 3,
                    "random": true,
                    "anim": {
                        "enable": false,
                        "speed": 40,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": particleColor,
                    "opacity": 0.4,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 2,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "repulse"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "repulse": {
                        "distance": 100,
                        "duration": 0.4
                    },
                    "push": {
                        "particles_nb": 4
                    }
                }
            },
            "retina_detect": true
        });

        console.log('✅ Particles.js initialisé avec succès');
    }

    // Lancer les particules après un court délai pour être sûr
    setTimeout(initParticles, 100);
});
