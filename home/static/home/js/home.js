gsap.to(".red", {
    opacity: 0,
    // zoom: 1.2,
    scrollTrigger: {
        trigger: ".red",
        start: "top top",
        end: "bottom top",
        scrub: true,
        // markers: true,
    },
});

gsap.to(".orange", {
    opacity: 0,
    scrollTrigger: {
        trigger: ".orange",
        start: "top bottom-=600",
        end: "bottom bottom-=1400",
        scrub: true,
        // markers: true,
    },
});

gsap.to(".purple", {
    opacity: 0.3,
    scrollTrigger: {
        trigger: ".purple",
        start: "top bottom-=600",
        end: "bottom bottom",
        scrub: true,
        // markers: true,
    },
});

// gsap.utils.toArray(".panel").forEach((panel) => {
//     ScrollTrigger.create({
//         trigger: panel,
//         start: "top top-=300",
//         pin: true,
//         pinSpacing: false,
//     });
// });

// ScrollTrigger.create({
//     snap: 1 / 2, // snap whole page to the closest section!
// });
