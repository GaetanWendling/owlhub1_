document.addEventListener('DOMContentLoaded', function() {
    const burger = document.querySelector('.burger-menu');
    const navLinks = document.querySelector('.nav-links');

    if (!burger || !navLinks) return;

    burger.addEventListener('click', function(e) {
        e.stopPropagation();
        navLinks.classList.toggle('active');
        burger.classList.toggle('active');
        document.body.classList.toggle('menu-open');
    });

    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            burger.classList.remove('active');
            document.body.classList.remove('menu-open');
        });
    });

    document.addEventListener('click', (e) => {
        if (!burger.contains(e.target) && !navLinks.contains(e.target)) {
            navLinks.classList.remove('active');
            burger.classList.remove('active');
            document.body.classList.remove('menu-open');
        }
    });
});
