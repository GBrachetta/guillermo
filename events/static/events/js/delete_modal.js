$(".remove-button").on("click", function (e) {
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let itemId = $(this).attr("class").split("remove_")[1];
    let url = `/events/delete_event/`;
    let data = {
        csrfmiddlewaretoken: csrfToken,
    };

    $.post(`${url}${itemId}/`, data).done(function () {
        location.reload();
    });
});
