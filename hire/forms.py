from django import forms
from .models import HireRequest
from catering.models import Allergen


class HireForm(forms.ModelForm):
    """ Form to send hire request info to database """
    class Meta:
        model = HireRequest
        fields = (
            'hire_package', 'name', 'email',
            'date', 'time', 'nr_of_guests', 'allergies',
            'comments'
        )

    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergen.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'hire_package': 'Package name',
            'name': 'Full Name',
            'email': 'Email Address',
            'nr_of_guests': 'Number of guests expected',
            'comments': 'Add your enquiries here...',
        }
        for field in self.fields:
            if field != 'date' and field != 'time' and field != 'allergies':
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields['date'] = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}))
        self.fields['time'] = forms.TimeField(
            widget=forms.TimeInput(attrs={'type': 'time'}))

