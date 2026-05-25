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


// category-slider

new Swiper(".category-slider", {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    navigation: {
      nextEl: ".swiper-nav-next",
      prevEl: ".swiper-nav-prev",
    },
    breakpoints: {
      480: { slidesPerView: 2 },
      768: { slidesPerView: 3 },
      1024: { slidesPerView: 4, spaceBetween: 24 },
      1280: { slidesPerView: 5, spaceBetween: 30 }
    }
  });


 new Swiper(".product-slider", {
    slidesPerView: 1,
    loop: true,
    spaceBetween: 20,
    navigation: {
      nextEl: ".prod-next",
      prevEl: ".prod-prev",
    },
    breakpoints: {
      480: { slidesPerView: 2 },
      768: { slidesPerView: 3 },
      1024: { slidesPerView: 4 }
    }
  });


// toggleTab Product details page... 
 function toggleTab(tabId, buttonElement) {
        document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
        document.getElementById(tabId).classList.remove('hidden');

        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('text-[var(--pink)]', 'border-b-2', 'border-[var(--pink)]');
            btn.classList.add('text-gray-400');
        });
        buttonElement.classList.add('text-[var(--pink)]', 'border-b-2', 'border-[var(--pink)]');
        buttonElement.classList.remove('text-gray-400');
    }