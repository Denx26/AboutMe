if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

document.addEventListener('DOMContentLoaded', () => {

    window.scrollTo(0, 0);



    const toggleBtn = document.getElementById('language-toggle');
    let currentLang = 'ro';

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            currentLang = currentLang === 'ro' ? 'en' : 'ro';
            const translatableElements = document.querySelectorAll('[data-en]');
            translatableElements.forEach(el => {
                el.innerText = el.getAttribute(`data-${currentLang}`);
            });       
    });
}

const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav a');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;

        if (pageYOffset >= sectionTop - 150) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('text-blue-500');

        if (current && link.getAttribute('href').includes(current)) {
            link.classList.add('text-blue-500');
        }
    });
});


});
