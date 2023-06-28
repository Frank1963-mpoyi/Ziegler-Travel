from django import forms

from .models import DriverLogsheet


class DriverLogsheetForm(forms.ModelForm):
    driver_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={"Name": "Full name", "name":"Name", "id":"name", "class": "form-control", "placeholder": "Full name"}),required=False)
    vehicule_type = forms.CharField(label='Vehicle Type', widget=forms.TextInput(attrs={"Vehicle Type": "Vehicle Type", "name":"Name", "vehicle type":"name", "class": "form-control", "placeholder": "Vehicle Type"}),required=False)
    
    class Meta:
        model = DriverLogsheet
        fields = ['driver_name', 'vehicule_type', 'time_in', 'time_out', 'km_in', 'km_out', 'destination', 'voucher_number', 'cost', 'note']

    def clean(self):
        cleaned_data = super().clean()
        time_in = cleaned_data.get('time_in')
        time_out = cleaned_data.get('time_out')
        driver_name = cleaned_data.get('driver_name')

        if driver_name == None:
            self.add_error('vehicule_type', 'Please put vehicle type!')
            
        # Custom validation: Ensure time_out is greater than time_in
        if time_in and time_out and time_out <= time_in:
            self.add_error('time_out', 'Time out must be greater than time in.')

        return cleaned_data