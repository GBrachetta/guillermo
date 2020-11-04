$(".remove-button").on("click", function (e) {
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let itemId = $(this).attr("class").split("remove_")[1];
    let url = `/album/delete_media/${itemId}/`;
    let data = {
        csrfmiddlewaretoken: csrfToken,
    };

    $.post(url, data).done(function () {
        location.reload();
    });
});
