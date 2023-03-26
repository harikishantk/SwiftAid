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
        fields = ['user', 'status', 'description', 'type', 'image', 'picture']
        widgets = {'type': forms.CheckboxSelectMultiple(choices=TYPES_CHOICES)}

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['user','latitude','longitude']




class CombinedForm(forms.Form):

    field1= LocationForm.base_fields['user']

    
    field2 = LocationForm.base_fields['latitude']
    field3 = LocationForm.base_fields['longitude']

    field4 = HelpRequestForm.base_fields['user']


    field5 = HelpRequestForm.base_fields['status']
    field6 = HelpRequestForm.base_fields['description']

    field7 = HelpRequestForm.base_fields['type']
    field8 = HelpRequestForm.base_fields['image']
    field9 = HelpRequestForm.base_fields['picture']



    def save(self):
        data = self.cleaned_data
        Location_data = {
            'user' : data['field1'],
            'latitude': data['field2'],
            'longitude': data['field3']
        }

        HelpRequest_data = {
            'user': data['field4'],
            'status': data['field5'],
            'description': data['field6'],
            'type': data['field7'],
            'image': data['field8'],
            'picture': data['field9']
        }

        print(Location_data)

        print(HelpRequest_data)
        Location.objects.create(**Location_data)
        HelpRequest.objects.create(**HelpRequest_data)