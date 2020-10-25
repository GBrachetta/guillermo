gsap.registerPlugin(ScrollTrigger);

ScrollTrigger.create({
    trigger: "#second-section",
    start: "top +=250px",
    end: "bottom bottom-=150px",
    pin: "#second-section-content",
    endTrigger: "#second-section",
    // markers: true
});

ScrollTrigger.create({
    trigger: "#third-section",
    start: " center",
    end: "+=250", // 200px past the start
    pin: "#third-section-content",
});

// ScrollTrigger.create({
//   trigger: "#fourth-section",
//   start: " center",
//   end: "+=250", // 200px past the start
//   pin: "#fourth-section-content"
// });

gsap.to("#overlay-first-section", {
    opacity: 1,
    scrollTrigger: {
        trigger: "#overlay-first-section",
        start: "top top",
        end: "bottom top",
        scrub: true,
    },
});

gsap.from("#overlay-second-section", {
    opacity: 1,
    scrollTrigger: {
        trigger: "#overlay-second-section",
        start: "top top",
        end: "bottom top",
        scrub: true,
    },
});

gsap.from("#overlay-third-section", {
    opacity: 1,
    scrollTrigger: {
        trigger: "#overlay-third-section",
        start: "top top",
        end: "bottom top",
        scrub: true,
    },
});

gsap.to("#overlay-fourth-section", {
    opacity: 1,
    scrollTrigger: {
        trigger: "#overlay-third-section",
        start: "bottom bottom+=200",
        end: "bottom",
        scrub: true,
    },
});

gsap.to("#first-section-content", {
    opacity: 0,
    y: "300",
    scrollTrigger: {
        trigger: "#first-section",
        start: "top top",
        end: "+=800",
        scrub: true,
    },
});

gsap.to("#second-section-content", {
    opacity: 1,
    x: "30%",
    scrollTrigger: {
        trigger: "#first-section",
        start: "center",
        end: "+=600",
        scrub: true,
    },
});

gsap.to("#third-section-content", {
    opacity: 1,
    x: "-20%",
    scrollTrigger: {
        trigger: "#second-section",
        start: "center",
        end: "+=600",
        scrub: true,
    },
});

gsap.to("#fourth-section-content", {
    opacity: 1,
    y: "500px",
    scrollTrigger: {
        trigger: "#third-section",
        start: "center",
        end: "+=600",
        scrub: true,
        // markers: true,
    },
});
