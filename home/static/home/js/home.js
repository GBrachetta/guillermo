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
    y: "+=450",
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
        start: "+=60%",
        end: "+=600",
        scrub: true,
    },
});

gsap.to("#third-section-content", {
    opacity: 1,
    y: "300px",
    scrollTrigger: {
        trigger: ".second-overlay",
        start: "+=60%",
        end: "+=600",
        scrub: true,
    },
});

gsap.to("#fourth-section-content", {
    opacity: 1,
    y: "500px",
    scrollTrigger: {
        trigger: ".third-overlay",
        start: "+=60%",
        end: "+=600",
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
