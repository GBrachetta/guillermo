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

// Calculates height of parent container to position section content
yTo = $(".parent-container").innerHeight() / 2;

// Reloads screen on orientation change so new yTo value can be applied
window.onorientationchange = () => {
    window.location.reload();
};

gsap.to("#first-section-content", 3, {
    opacity: 0,
    y: yTo,
    scrollTrigger: {
        trigger: ".first-overlay",
        start: "top top",
        end: "bottom center",
        scrub: true,
    },
});

gsap.to("#second-section-content", 3, {
    y: (yTo += 10),
    opacity: 1,
    scrollTrigger: {
        trigger: ".first-overlay",
        start: "+=60%",
        end: "+=220",
        scrub: true,
    },
});

gsap.to("#third-section-content", {
    opacity: 1,
    y: (yTo -= 80),
    scrollTrigger: {
        trigger: ".second-overlay",
        start: "+=60%",
        end: "+=220",
        scrub: true,
    },
});

gsap.to("#fourth-section-content", {
    opacity: 1,
    y: (yTo += 80),
    scrollTrigger: {
        trigger: ".third-overlay",
        start: "+=60%",
        end: "+=200",
        scrub: true,
    },
});

$(function () {
    $(".bg1").parallax({
        imageSrc: "https://res.cloudinary.com/gbrachetta/image/upload/v1604230951/bg1.jpg",
    });
    $(".bg2").parallax({
        imageSrc: "https://res.cloudinary.com/gbrachetta/image/upload/v1604230958/bg2.jpg",
    });
    $(".bg3").parallax({
        imageSrc: "https://res.cloudinary.com/gbrachetta/image/upload/v1604230952/bg3.jpg",
    });
    $(".bg4").parallax({
        imageSrc: "https://res.cloudinary.com/gbrachetta/image/upload/v1604230950/bg4c.jpg",
    });
});
