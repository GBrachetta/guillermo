gsap.registerPlugin(ScrollTrigger);

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
    y: "500",
    scrollTrigger: {
        trigger: "#first-section",
        start: "top top",
        end: "+=800",
        scrub: true,
    },
});

gsap.to("#second-section-content", {
    opacity: 1,
    x: "15%",
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
    },
});

// PARALLAX

gsap.utils.toArray("section").forEach((section, i) => {
    section.panel = section.querySelector(".panel");

    // Do the parallax effect on each section
    if (i) {
        section.panel.style.backgroundPosition = `50% ${innerHeight / 2}px`;

        gsap.to(section.panel, {
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
        section.panel.style.backgroundPosition = "50% 0px";

        gsap.to(section.panel, {
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

// Snap sections

// function goToSection(i, anim) {
//     gsap.to(window, {
//         scrollTo: { y: i * innerHeight, autoKill: false },
//         duration: 2,
//     });

//     if (anim) {
//         anim.restart();
//     }
// }

// gsap.utils.toArray(".panel").forEach((panel, i) => {
//     ScrollTrigger.create({
//         trigger: panel,
//         onEnter: () => goToSection(i),
//     });

//     ScrollTrigger.create({
//         trigger: panel,
//         start: "bottom bottom",
//         onEnterBack: () => goToSection(i),
//     });
// });