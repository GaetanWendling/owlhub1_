// typing.js - Animation de texte qui s'écrit
class TypingAnimation {
    constructor(element, words, typingSpeed = 100, deletingSpeed = 50, delayBetweenWords = 2000) {
        this.element = element;
        this.words = words;
        this.typingSpeed = typingSpeed;
        this.deletingSpeed = deletingSpeed;
        this.delayBetweenWords = delayBetweenWords;
        this.wordIndex = 0;
        this.charIndex = 0;
        this.isDeleting = false;

        this.type();
    }

    type() {
        const currentWord = this.words[this.wordIndex];

        if (this.isDeleting) {
            // Effacer
            this.element.textContent = currentWord.substring(0, this.charIndex - 1);
            this.charIndex--;

            if (this.charIndex === 0) {
                this.isDeleting = false;
                this.wordIndex = (this.wordIndex + 1) % this.words.length;
                setTimeout(() => this.type(), 500);
                return;
            }
        } else {
            // Écrire
            this.element.textContent = currentWord.substring(0, this.charIndex + 1);
            this.charIndex++;

            if (this.charIndex === currentWord.length) {
                this.isDeleting = true;
                setTimeout(() => this.type(), this.delayBetweenWords);
                return;
            }
        }

        const speed = this.isDeleting ? this.deletingSpeed : this.typingSpeed;
        setTimeout(() => this.type(), speed);
    }
}

// Initialisation pour la page d'accueil
document.addEventListener('DOMContentLoaded', () => {
    const animatedWord = document.querySelector('.animated-word');
    if (animatedWord) {
        const words = ['Données', 'KPIs', 'Insights', 'Décisions'];
        new TypingAnimation(animatedWord, words);
    }
});