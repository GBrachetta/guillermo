$(".update-link").on("click", function () {
    let form = $(this).prev(".update-form");
    form.submit();
});


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
