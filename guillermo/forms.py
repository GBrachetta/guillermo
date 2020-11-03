from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="")
    email = forms.EmailField(label="")
    message = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 8,
            }
        ),
    )

    class Meta:
        fields = ["name", "email", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"

        placeholders = {
            "name": "Name *",
            "email": "Email *",
            "message": "Message *",
        }
        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
        self.fields[field].label = False
