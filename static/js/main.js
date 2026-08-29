document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById('menu-toggle');
    const menuClose = document.getElementById('menu-close');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuOverlay = document.getElementById('menu-overlay');

    if (!menuToggle || !mobileMenu || !menuOverlay) return;

    function openMenu() {
        menuOverlay.classList.remove('hidden');
        requestAnimationFrame(() => {
            menuOverlay.classList.remove('opacity-0');
            mobileMenu.classList.remove('translate-x-full');
        });
        document.documentElement.classList.add('overflow-hidden');
    }

    function closeMenu() {
        mobileMenu.classList.add('translate-x-full');
        menuOverlay.classList.add('opacity-0');
        setTimeout(() => {
            menuOverlay.classList.add('hidden');
        }, 300);
        document.documentElement.classList.remove('overflow-hidden');
    }

    menuToggle.addEventListener('click', openMenu);
    if (menuClose) menuClose.addEventListener('click', closeMenu);
    menuOverlay.addEventListener('click', closeMenu);

    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });
});

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


// increse quntity real time
document.addEventListener("DOMContentLoaded", function () {
    const quantityInput = document.getElementById("quantity-input");
    const increaseBtn = document.getElementById("increase-btn");
    const decreaseBtn = document.getElementById("decrease-btn");

    increaseBtn.addEventListener("click", function () {
        quantityInput.value = parseInt(quantityInput.value) + 1;
    });

    decreaseBtn.addEventListener("click", function () {
        if (parseInt(quantityInput.value) > 1) {
            quantityInput.value = parseInt(quantityInput.value) - 1;
        }
    });
});
