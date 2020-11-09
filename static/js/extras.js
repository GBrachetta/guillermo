// Shows message toasts
$(".toast").toast("show");

/**
 * Allows for smooth opening and closing of navbar dropdown.
 */
$(".dropdown").on("show.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideDown(300);
});

$(".dropdown").on("hide.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideUp(300);
});

/**
 * Allows for closing collapsed navbar by clicking outside of the menu.
 */
$(function () {
    $(document).on("click", function (event) {
        const click = $(event.target);
        const _open = $(".navbar-collapse").hasClass("show");
        if (_open === true && !click.hasClass("navbar-toggler")) {
            $(".navbar-toggler").click();
        }
    });
});

/**
 * Loads the form present in the contact view and renders it in the modal.
 */
$(function () {
    $("#trigger-contact").on("click", () => {
        $("#form-modal").load("/contact", () => {
            $("#contact").modal("show");
        });
    });
});
