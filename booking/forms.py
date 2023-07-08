# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from crispy_forms.helper import FormHelper
from datetime import date
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import TableBooking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# The contact form for the user to send a message to the business


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    def clean_day(self):
        day = self.cleaned_data['day']
        if day <= date.today():
            raise forms.ValidationError("Please select a future date.")
        return day

    class Meta:
        model = TableBooking
        fields = (
            'email',
            'phone',
            'day',
            'time',
            'service'
            )
        widgets = {
            'day': forms.TextInput(attrs={'type': 'date'}),
        }
