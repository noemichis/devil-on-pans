from datetime import date
from django import forms
from catering.models import Allergen
from .models import HireRequest


class HireForm(forms.ModelForm):
    """ Form to send hire request info to database """
    class Meta:
        model = HireRequest
        exclude = ('replied',)

    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergen.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'nr_of_guests': 'Number of guests expected',
            'comments': 'Add your enquiries here...',
        }

        for field in self.fields:
            if field != 'allergies':
                self.fields[field].label = False
            if field not in ['hire_package', 'date', 'time', 'allergies']:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

        self.fields['date'] = forms.DateField(
            widget=forms.DateInput(
                attrs={'type': 'date', 'min': date.today()}))
        self.fields['time'] = forms.TimeField(
            widget=forms.TimeInput(
                attrs={'type': 'time', 'min': '08:00', 'max': '20:00'}))
