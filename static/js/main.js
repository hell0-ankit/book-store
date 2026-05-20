    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.getElementById('menu-icon');
    const menuOverlay = document.getElementById('menu-overlay');

    function toggleMenu() {
        mobileMenu.classList.toggle('translate-x-full');
        if (mobileMenu.classList.contains('translate-x-full')) {
            menuOverlay.classList.add('opacity-0');
            setTimeout(() => menuOverlay.classList.add('hidden'), 300);
            menuIcon.classList.remove('fa-xmark', 'rotate-90');
            menuIcon.classList.add('fa-bars');
        } else {
            menuOverlay.classList.remove('hidden');
            setTimeout(() => menuOverlay.classList.remove('opacity-0'), 10);
            menuIcon.classList.remove('fa-bars');
            menuIcon.classList.add('fa-xmark', 'rotate-90');
        }
    }

    menuToggle.addEventListener('click', toggleMenu);
    menuOverlay.addEventListener('click', toggleMenu);
