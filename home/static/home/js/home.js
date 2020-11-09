/**
 * Landing page scripts
 */

// Used to determine height of element containers
const selector = $(".parent-container");

/**
 * Loops through the overlays, uses a function to dynamically return a new value
 * Loops through the overlays, uses a function to dynamically return a new value
 * based on current size.
 * First overlay is different as it starts with 0 opacity and animates to 1.
 */
for (let i = 1; i <= 4; i++) {
    if (i === 1) {
        gsap.to(`.overlay-${i}`, {
            opacity: 1,
            scrollTrigger: {
                trigger: `.overlay-${i}`,
                start: "top top",
                end: "bottom top",
                scrub: true,
                invalidateOnRefresh: true,
            },
        });
    } else {
        gsap.to(`.overlay-${i}`, {
            opacity: 1,
            scrollTrigger: {
                trigger: `.overlay-${i - 1}`,
                start: () => {
                    return `bottom ` + selector.innerHeight() / 2.5;
                },
                end: "bottom top",
                scrub: true,
                invalidateOnRefresh: true,
            },
        });
    }
}

/**
 * Loops through the content to translate and animate text content.
 * First content is the title and uses a different animation.
 * The value of 'y' (vertical translation) is dynamically calculated and returned,
 * using the constant above.
 * The key 'invalidateOnRefresh' ensures that new values are injected on 
 * screen resize.
 * The key 'scrub' permits to reverse the animation on scroll up.
 */
for (let y = 1; y < 5; y++) {
    if (y === 1) {
        gsap.to(`#section-content-${y}`, 3, {
            opacity: 0,
            y: () => {
                return selector.innerHeight() / 2;
            },
            scrollTrigger: {
                trigger: `.overlay-${y}`,
                start: "top top",
                end: "bottom center",
                scrub: true,
                invalidateOnRefresh: true,
            },
        });
    } else {
        gsap.to(`#section-content-${y}`, 3, {
            y: () => {
                return selector.innerHeight() / 2 - selector.innerHeight() / 10;
            },
            opacity: 1,
            scrollTrigger: {
                trigger: `.overlay-${y - 1}`,
                start: "+=60%",
                end: "+=220",
                scrub: true,
                invalidateOnRefresh: true,
            },
        });
    }
}

/**
 * Loops through a pool of 4 img backgrounds and assigns each one of the to the 
 * four containers on the homepage.
 */
$(function () {
    for (let z = 1; z < 5; z++) {
        $(`.bg${z}`).parallax({
            imageSrc: `https://res.cloudinary.com/gbrachetta/image/upload/bgms4/bg-${z}.jpg`,
        });
    }
});
