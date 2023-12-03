from django import forms
from .models import HireRequest

class HireForm(forms.ModelForm):
    """ Form to send hire request info to database """
    class Meta:
        model = HireRequest
        fields = (
            'hire_package', 'name', 'email',
            'date', 'time', 'nr_of_guests', 'allergies',
            'comments'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'] = forms.DateField(widget=forms.SelectDateWidget)
        self.fields['time'] = forms.TimeField(widget=forms.TimeInput)

