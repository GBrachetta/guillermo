// var elem = document.querySelector(".grid");
// var msnry = new Masonry(elem, {
//     // options
//     itemSelector: ".grid-item",
//     columnWidth: 200,
// });

// // element argument can be a selector string
// //   for an individual element
// var msnry = new Masonry(".grid", {
//     // options
// });

// lightbox.option({
//     wrapAround: true,
//     showImageNumberLabel: false,
// });


// ESTO HASTA COLCADE
// var grid = document.querySelector(".grid");

// var msnry = new Masonry(grid, {
//     itemSelector: ".grid-item",
//     columnWidth: ".grid-sizer",
//     percentPosition: true,
// });

// imagesLoaded(grid).on("progress", function () {
//     // layout Masonry after each image loads
//     msnry.layout();
// });


// COLCADE
var colc = new Colcade(".grid", {
    columns: ".grid-col",
    items: ".grid-item",
});