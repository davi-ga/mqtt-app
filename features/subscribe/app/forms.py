from django import forms


class SubscribeForm(forms.Form):
    OPTIONS = [
        ("illumination_1", "Illumination 1"),
        ("illumination_2", "Illumination 2"),
        ("illumination_3", "Illumination 3"),
        ("humidity", "Humidity"),
        ("temperature", "Temperature"),
        ("presence", "Presence"),
        ("water_level_1", "Water Level 1"),
        ("water_level_2", "Water Level 2"),
    ]
    name = forms.CharField(label="Nickname")
    select_field = forms.MultipleChoiceField(
        choices=OPTIONS, widget=forms.CheckboxSelectMultiple, label="Select an option"
    )
