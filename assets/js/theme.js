// ============================================
// GESTION DU THÈME JOUR/NUIT
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;

    // Récupérer le thème sauvegardé (défaut: light)
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);

    console.log('🎨 Thème initial:', savedTheme);

    // Toggle theme
    themeToggle.addEventListener('click', function() {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';

        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        console.log('🔄 Thème changé:', newTheme);

        // Les particules se mettront à jour automatiquement via MutationObserver
    });
});
