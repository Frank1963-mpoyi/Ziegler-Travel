from django import forms

from .models import DriverLogsheet

class DriverLogsheetForm(forms.ModelForm):
    class Meta:
        model = DriverLogsheet
        fields = '__all__'