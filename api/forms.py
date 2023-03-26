from django import forms
from .models import HelpRequest, Location
from leaflet.forms.widgets import LeafletWidget

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
    location = forms.CharField(widget=LeafletWidget(attrs={'map_height': '800px'}))
    class Meta:
        model = Location
        fields = ('location',)

       


       