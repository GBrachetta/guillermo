// Adds 'https://' on blur if there's content in the input, validating it,
// avoiding needing to enter it manually.
//https://stackoverflow.com/questions/17946960/with-html5-url-input-validation-assume-url-starts-with-http
$(function () {
    $('input[type="url"]').on("blur", function () {
        var string = $(this).val();
        if (!string.match(/^https?:/) && string.length) {
            string = "https://" + string;
            $(this).val(string);
        }
    });
});
