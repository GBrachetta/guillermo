from django import forms
from .models import Event
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    # In order to display a date and time pickers in the form
    date = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=DatePickerInput(
            options={
                "format": "DD/MM/YYYY",  # moment date-time format
                "showClose": True,
                "showClear": True,
                "showTodayButton": True,
                "viewMode": 'months',
            }
        ),
    )
    time = forms.TimeField(widget=TimePickerInput(options={"stepping": 15}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
