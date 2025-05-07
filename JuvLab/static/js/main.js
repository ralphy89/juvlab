/* Add JavaScript functionality for the scroll-to-top button */
document.addEventListener('DOMContentLoaded', function() {
    const scrollUpBtn = document.getElementById('scroll-up');

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollUpBtn.classList.add('show');
        } else {
            scrollUpBtn.classList.remove('show');
        }
    });

    scrollUpBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});