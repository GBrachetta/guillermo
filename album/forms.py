from django import forms
from .widgets import CustomClearableFileInput
from .models import Photo


class MediaForm(forms.ModelForm):
    """
    Form to add/edit media for the gallery.
    The field thumbnail takes the same value as image and it's hidden.
    "Image" uploads the file directly, while the other generates the thumbnail
    from the same image, saving it with a different random name.
    """

    class Meta:
        model = Photo
        fields = ("name", "caption", "image_url", "image")

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    thumbnail = image.hidden_widget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
