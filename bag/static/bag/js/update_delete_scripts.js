/*
This script (and all modal scripts for forloops in the app) receives the itemId
passed through anchor's class "remove_{{ itemId }}", splits it and selects
the value needed and assigns it to the variable used to effectively delete
the required itemId.
*/
$(".remove-button").on("click", function (e) {
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let itemId = $(this).attr("class").split("remove_")[1];
    let url = `/bag/remove/${itemId}/`;
    let data = {
        csrfmiddlewaretoken: csrfToken,
    };

    $.post(url, data).done(function () {
        location.reload();
    });
});

/*
A similar script as the one above, taking the data from the dataset.
Then checks if the form is valid: if it is, it submits it, otherwise
it removes the 'd-none' class from the error message, displaying it.
*/
$(".update-link").on("click", function () {
    let number = this.dataset.number;
    let cartForm = document.querySelector(`#cart-form-${number}`);
    let cartFormValid = cartForm.checkValidity();
    if (cartFormValid) {
        let form = $(this).prev(".update-form");
        form.submit();
    } else {
        $(this).prev().children(".error-message").removeClass("d-none");
    }
});

/*
Same as above, needed as that one would not work on a template where a grid
with d-none was present.
This particular one applies to "d-block d-md-none".
*/
$(".update-link-sm").on("click", function () {
    let number = this.dataset.number;
    let cartForm = document.querySelector(`#cart-form-sm-${number}`);
    let cartFormValid = cartForm.checkValidity();
    if (cartFormValid) {
        let form = $(this).prev(".update-form-sm");
        form.submit();
    } else {
        $(this).prev().children(".error-message").removeClass("d-none");
    }
});
