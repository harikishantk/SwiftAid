from django import forms
from .models import HelpRequest, Location

TYPES_CHOICES = [
        ('FOOD', 'FOOD'),
        ('MEDICINE', 'MEDICINE'),
        ('CLOTHES', 'CLOTHES'),
        ('SHELTER', 'SHELTER'),
        ('RESCUE', 'RESCUE'),
        ('MISSING', 'MISSING'),
        ('OTHER', 'OTHER'),

]

class HelpRequestForm(forms.ModelForm):
    
    class Meta:
        model = HelpRequest
        fields = ['status', 'description', 'type', 'image', 'picture']
        widgets = {'type': forms.CheckboxSelectMultiple(choices=TYPES_CHOICES)}

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location']
