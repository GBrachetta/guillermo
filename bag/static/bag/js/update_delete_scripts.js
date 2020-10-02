$(".update-link").on("click", function () {
    let form = $(this).prev(".update-form");
    form.submit();
});

$(".remove-item").on("click", function () {
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let itemId = $(this).attr("id").split("remove_")[1];
    let url = `/bag/remove/${itemId}/`;
    let data = {
        csrfmiddlewaretoken: csrfToken,
    };

    $.post(url, data).done(function () {
        location.reload();
    });
});
