// GESTION DU THÈME
const themeToggle = document.querySelector('.theme-toggle');
const htmlElement = document.documentElement;
const owlImage = document.querySelector('.owl-container img');

const savedTheme = localStorage.getItem('theme') || 'dark';
htmlElement.setAttribute('data-theme', savedTheme);
updateThemeButton(savedTheme);
updateOwlImage(savedTheme);

console.log(`🎨 Thème actif:  $ {savedTheme}`);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeButton(newTheme);
        updateOwlImage(newTheme);

        console.log(`🔄 Thème changé:  $ {newTheme}`);

        if (typeof updateParticles === 'function') {
            updateParticles(newTheme);
        }
    });
    console.log('✅ Bouton thème initialisé');
}

function updateThemeButton(theme) {
    if (!themeToggle) return;
    themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
}

function updateOwlImage(theme) {
    if (!owlImage) return;
    owlImage.src = theme === 'dark'
        ? 'assets/images/owl_dark.png'
        : 'assets/images/owl_light.png';
}
