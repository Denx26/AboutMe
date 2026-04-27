  if('scrollRestoration' in history){
        history.scrollRestoration = 'manual';
    }

document.addEventListener('DOMContentLoaded', () => {
    window.scrollTo(0, 0);
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

            if (curent && link.getAttribute('href').includes(current)) {
                link.classList.add('text-blue-500');
            }
        });
    });
});
