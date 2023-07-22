from django import forms
from .models import *
# from admin_control.models import Appointment
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_Name', 'Company_Name', 'Product_Image', 'Product_Price']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'contact_number', 'location']

        
class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all().order_by('name'))  # Dropdown field for selecting a doctor
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Date field with HTML input type 'date'
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  # Time field with HTML input type 'time'
    
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time']  # Fields included in the form
   


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['doctor', 'product', 'quantity_ordered']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.all()
        self.fields['product'].queryset = Product.objects.all()

        