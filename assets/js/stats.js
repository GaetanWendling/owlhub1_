/**
 * stats.js
 * Gestion des statistiques
 */

document.addEventListener('DOMContentLoaded', () => {

    const stats = {
        pageViews: 0,
        uniqueVisitors: 0,

        init() {
            this.loadFromStorage();
            this.trackPageView();
            this.updateDisplay();
        },

        loadFromStorage() {
            const stored = localStorage.getItem('owlhub_stats');
            if (stored) {
                const data = JSON.parse(stored);
                this.pageViews = data.pageViews || 0;
                this.uniqueVisitors = data.uniqueVisitors || 0;
            }
        },

        saveToStorage() {
            localStorage.setItem('owlhub_stats', JSON.stringify({
                pageViews: this.pageViews,
                uniqueVisitors: this.uniqueVisitors
            }));
        },

        trackPageView() {
            this.pageViews++;
            if (!sessionStorage.getItem('owlhub_visitor')) {
                this.uniqueVisitors++;
                sessionStorage.setItem('owlhub_visitor', 'true');
            }
            this.saveToStorage();
        },

        updateDisplay() {
            const pvEl = document.getElementById('stat-pageviews');
            const vEl = document.getElementById('stat-visitors');

            if (pvEl) pvEl.textContent = this.pageViews;
            if (vEl) vEl.textContent = this.uniqueVisitors;
        }
    };

    stats.init();
    console.log('✅ Stats module chargé');
});
