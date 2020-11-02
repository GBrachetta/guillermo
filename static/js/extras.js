// Toasts
$(".toast").toast("show");

// Smooth opening navbar dropdown
$(".dropdown").on("show.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideDown(300);
});

$(".dropdown").on("hide.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideUp(300);
});

$(document).ready(function () {
    $(document).click(function (event) {
        const click = $(event.target);
        const _open = $(".navbar-collapse").hasClass("show");
        if (_open === true && !click.hasClass("navbar-toggler")) {
            $(".navbar-toggler").click();
        }
    });
});