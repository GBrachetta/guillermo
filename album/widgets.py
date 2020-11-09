from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Displays a checkbox to remove current image attached to the item.
    """

    initial_text = _("Current Image")
    input_text = _("")
    template_name = (
        "album/custom_widget_templates/custom_clearable_file_input.html"
    )
