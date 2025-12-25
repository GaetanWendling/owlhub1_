// animated-word.js - Animation du mot changeant
document.addEventListener('DOMContentLoaded', function() {
    console.log('🔄 Animated-word.js chargé');

    const wordElement = document.getElementById('animated-word');

    if (!wordElement) {
        console.error('❌ #animated-word introuvable');
        return;
    }

    const words = ['insights', 'décisions', 'KPI', 'stratégies'];
    let currentIndex = 0;

    function changeWord() {
        // Fade out
        wordElement.style.opacity = '0';
        wordElement.style.transform = 'translateY(-10px)';

        setTimeout(() => {
            // Changer le texte
            currentIndex = (currentIndex + 1) % words.length;
            wordElement.textContent = words[currentIndex];

            // Fade in
            wordElement.style.opacity = '1';
            wordElement.style.transform = 'translateY(0)';
        }, 300); // Durée du fade out
    }

    // Changer toutes les 3 secondes
    setInterval(changeWord, 3000);

    console.log('✅ Animation du mot démarrée');
});
