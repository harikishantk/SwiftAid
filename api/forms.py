from django import forms
from .models import HelpRequest

TYPES_CHOICES = (
        ('FOOD', 'FOOD'),
        ('MEDICINE', 'MEDICINE'),
        ('CLOTHES', 'CLOTHES'),
        ('SHELTER', 'SHELTER'),
        ('RESCUE', 'RESCUE'),
        ('MISSING', 'MISSING'),
        ('OTHER', 'OTHER'),

    )

class HelpRequestForm(forms.ModelForm):
    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=TYPES_CHOICES)
    class Meta:
        model = HelpRequest
        fields = ['status', 'description', 'type', 'image', 'picture']
