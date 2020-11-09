/**
 * Styles the selected/unselected country field in checkout form to match design.
 */
let countrySelected = $("#id_default_country").val();
if (!countrySelected) {
    $("#id_default_country").css("color", "#aab7c4");
}
$("#id_default_country").change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css("color", "#aab7c4");
    } else {
        $(this).css("color", "#000");
    }
});
