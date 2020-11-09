/*
This script (and all modal scripts for forloops in the app) receives the itemId
passed through anchor's class "remove_{{ itemId }}", splits it and selects
the value needed and assigns it to the variable used to effectively delete
the required itemId.
*/
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
