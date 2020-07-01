// $(document).ready(function () {
// Init ScrollMagic
const controller = new ScrollMagic.Controller();

// Scene intro - pin the intro section

const tween = TweenMax.to(".background-container", 1, {
    scale: 2,
    opacity: 0,
    // ease: Linear.easeNone,
    ease: Power2.easeOut,
});

// const tweenImg02 = TweenMax.to(".img-02", 1, {
//     scale: 2,
//     opacity: 0,
//     ease: Linear.easeNone,
// });

const pinSceneIntro = new ScrollMagic.Scene({
    triggerElement: "#intro",
    triggerHook: 0,
    duration: "200%",
})
    .setTween(tween)
    .setPin("#intro .background-container")
    .addIndicators()
    .addTo(controller);

// Scene 1 - pin the second section
var pinScene01 = new ScrollMagic.Scene({
    triggerElement: "#slide01",
    triggerHook: 0,
    duration: "100%",
})
    .setPin("#slide01 .pin-wrapper")
    .addIndicators()
    .addTo(controller);
// Scene 2 - pin the third section
var pinScene02 = new ScrollMagic.Scene({
    triggerElement: "#slide01",
    triggerHook: 0,
    duration: "200%",
})
    .addIndicators()
    .setPin("#slide02 .pin-wrapper")
    .addTo(controller);
