gsap.registerPlugin(ScrollSmoother) 

gsap.registerPlugin(ScrollTrigger);



// =========================
// FADE LEFT
// =========================

gsap.utils.toArray(".fade-left").forEach((element) => {

  gsap.from(element, {

    scrollTrigger: {
      trigger: element,
      start: "top 85%",
     
    },

    x: -100,
    opacity: 0,
    duration: 1.2,
    ease: "power3.out"

  });

});



// =========================
// FADE RIGHT
// =========================

gsap.utils.toArray(".fade-right").forEach((element) => {

  gsap.from(element, {

    scrollTrigger: {
      trigger: element,
      start: "top 85%",
    },

    x: 100,
    opacity: 0,
    duration: 1.2,
    ease: "power3.out"

  });

});



// =========================
// FADE UP
// =========================

gsap.utils.toArray(".fade-up").forEach((element) => {

  gsap.from(element, {

    scrollTrigger: {
      trigger: element,
      start: "top 85%",
    },

    y: 80,
    opacity: 0,
    duration: 1,
    ease: "power3.out"

  });

});



// =========================
// SLIDE LEFT
// =========================

gsap.utils.toArray(".slide-left").forEach((element) => {

  gsap.from(element, {

    scrollTrigger: {
      trigger: element,
      start: "top 85%",
       toggleActions: "play reset play reset",
    },

    x: -200,
    duration: 1.2,
    ease: "expo.out"

  });

});



// =========================
// SLIDE RIGHT
// =========================

gsap.utils.toArray(".slide-right").forEach((element) => {

  gsap.from(element, {

    scrollTrigger: {
      trigger: element,
      start: "top 85%",
       toggleActions: "play reset play reset",
    },

    x: 200,
    duration: 1.2,
    ease: "expo.out"

  });

});



// =========================
// ZOOM IN
// =========================

gsap.utils.toArray(".zoom-in").forEach((element) => {

  gsap.from(element, {

    scrollTrigger: {
      trigger: element,
      start: "top 85%",
      toggleActions: "play reset play reset",
    },

    scale: 0.7,
    opacity: 0,
    duration: 1,
    ease: "back.out(1.7)"

  });

});


// =========================
// For Product Section
//  =========================
gsap.utils.toArray(".stagger-wrapper").forEach((wrapper) => {

  const items = wrapper.querySelectorAll(".stagger-item");

  gsap.from(items, {

    scrollTrigger: {
      trigger: wrapper,
      start: "top 85%",
      toggleActions: "play reset play reset",
    },

    y: 80,
    opacity: 0,

    stagger: 0.15,

    duration: 1,

    ease: "power3.out"

  });

});



document.querySelectorAll(".brand-card").forEach((card) => {

  card.addEventListener("mouseenter", () => {

    gsap.to(card, {
      y: -8,
      scale: 1.03,
      duration: 0.3
    });

  });

  card.addEventListener("mouseleave", () => {

    gsap.to(card, {
      y: 0,
      scale: 1,
      duration: 0.3
    });

  });

});

gsap.utils.toArray(".gsap-stagger").forEach((wrapper) => {

  gsap.from(wrapper.querySelectorAll(".gsap-item"), {

    scrollTrigger: {
      trigger: wrapper,
      start: "top 85%", 
      toggleActions: "play reset play reset",
    },

    y: -50,
    opacity: 0,

    stagger: 0.1,

    duration: 0.8,

    ease: "power3.out"

  });

});

gsap.utils.toArray(".gsap-stagger-zoomin").forEach((wrapper) => {
  gsap.from(wrapper.querySelectorAll(".zoomin-item"), {
    scrollTrigger: {
      trigger: wrapper,
      start: "top 85%",
      toggleActions: "play reset play reset",
    },

    scale: 0.7,
    opacity: 0,

    stagger: 0.12,

    duration: 0.8,

    ease: "back.out(1.7)"

  });

});