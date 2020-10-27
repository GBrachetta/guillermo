// Try

$.backstretch([
    "../../../../static/images/bg1-sm.jpeg",
    "../../../../static/images/bg2-sm.jpg",
    "../../../../static/images/bg3-sm.jpg",
    "../../../../static/images/bg4-sm.jpg"
]);

// End

gsap.to(".first-overlay", {
    opacity: 1,
    scrollTrigger: {
        trigger: ".first-overlay",
        start: "top top",
        end: "bottom top",
        scrub: true,
    },
});

gsap.from(".second-overlay", {
    opacity: 1,
    scrollTrigger: {
        trigger: ".second-overlay",
        start: "top top",
        end: "bottom top",
        scrub: true,
    },
});

gsap.from(".third-overlay", {
    opacity: 1,
    scrollTrigger: {
        trigger: ".third-overlay",
        start: "top top",
        end: "bottom top",
        scrub: true,
    },
});

gsap.to(".fourth-overlay", {
    opacity: 1,
    scrollTrigger: {
        trigger: ".third-overlay",
        start: "bottom bottom+=200",
        end: "bottom",
        scrub: true,
    },
});

gsap.to("#first-section-content", {
    opacity: 0,
    y: "350",
    scrollTrigger: {
        trigger: ".first-overlay",
        start: "top top",
        end: "bottom center",
        scrub: true,
    },
});

gsap.to("#second-section-content", {
    opacity: 1,
    y: "500px",
    scrollTrigger: {
        trigger: ".first-overlay",
        start: "+=50%",
        end: "+=600",
        scrub: true,
    },
});

gsap.to("#third-section-content", {
    opacity: 1,
    y: "300px",
    scrollTrigger: {
        trigger: ".first-overlay",
        start: "+=150%",
        end: "+=600",
        scrub: true,
    },
});

gsap.to("#fourth-section-content", {
    opacity: 1,
    y: "300px",
    scrollTrigger: {
        trigger: ".first-overlay",
        start: "+=225%",
        end: "+=600",
        scrub: true,
    },
});

gsap.utils.toArray("section").forEach((section, i) => {
    section.bg = section.querySelector(".bg");

    // Do the parallax effect on each section
    if (i) {
        section.bg.style.backgroundPosition = `50% ${innerHeight / 2}px`;

        gsap.to(section.bg, {
            backgroundPosition: `50% ${-innerHeight / 2}px`,
            ease: "none",
            scrollTrigger: {
                trigger: section,
                scrub: true,
            },
        });
    }

    // the first image should be positioned against the top. Use px on the animating part to work with GSAP.
    else {
        section.bg.style.backgroundPosition = "50% 0px";

        gsap.to(section.bg, {
            backgroundPosition: `50% ${-innerHeight / 2}px`,
            ease: "none",
            scrollTrigger: {
                trigger: section,
                start: "top top",
                end: "bottom top",
                scrub: true,
            },
        });
    }
});
