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
                const newContent = el.getAttribute(`data-${currentLang}`);
                if (newContent) {
                    el.innerHTML = newContent;
                }
            });
        });
        AOS.refresh();
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

    const chatBtn = document.getElementById("chatBtn");
    const chatPopup = document.getElementById("chatPopup");
    const closeChat = document.getElementById("closeChat");

    chatBtn.addEventListener("click", () => chatPopup.classList.toggle("hidden"));
    closeChat.addEventListener("click", () => chatPopup.classList.add("hidden"));

    const sendBtn = document.getElementById("sendBtn")


    
    sendBtn.addEventListener("click", async () => {
        const inputField = document.getElementById("userInput");
        const display = document.getElementById("chatDisplay");
        const message = inputField.value.trim();

        if (!message) return;

        sendBtn.diasbled=true;
        sendBtn.classList.add('opacity-50', 'cursor-not-allowed');

        setTimeout(function() {
            sendBtn.diasbled=false;
            sendBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        }, 10000);

        display.innerHTML += `<div class="bg-blue-900/50 p-2 rounded-lg self-end max-w-[80%]">${message}</div>`;
        inputField.value = "";
        display.scrollTop = display.scrollHeight;

        try {
            const response = await fetch("http://127.0.0.1:8001/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();

            display.innerHTML += `<div class="bg-slate-700 p-2 rounded-lg self-start max-w-[80%]">${data.response}</div>`;
            display.scrollTop = display.scrollHeight;
        } catch (error) {
            console.error("Eroare Chat:", error);
            display.innerHTML += `<div class="text-red-400 text-xs text-center italic">Eroare de conexiune la server.</div>`;
        }
    });
});


