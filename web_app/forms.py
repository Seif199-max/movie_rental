from django import forms
from django.forms import ModelForm
from .models import Rentals,Returns

class RentalsForm(ModelForm):
    class Meta:
        model = Rentals
        fields = '__all__'
        widgets = {
            'return_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ReturnsForm(ModelForm):
    class Meta:
        model = Returns
        fields = ['return_date','rental']
        widgets = {
            'return_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }