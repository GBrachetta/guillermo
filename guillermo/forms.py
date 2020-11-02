from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full Name")
    email = forms.EmailField(label="Email")
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={
                "rows": 8,
            }
        ),
    )

    class Meta:
        fields = ["full_name", "email", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
