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