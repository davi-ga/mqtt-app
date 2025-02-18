from django import forms


class SubscribeForm(forms.Form):
    OPTIONS = [
        ("illumination", "Illumination"),
        ("humidity", "Humidity"),
        ("water_level", "Water Level"),
        ("sound", "Sound"),
    ]
    name = forms.CharField(label="Nickname")
    select_field = forms.MultipleChoiceField(
        choices=OPTIONS, widget=forms.CheckboxSelectMultiple, label="Select an option"
    )
