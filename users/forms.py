from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

CHOICES = [
    ('VICTIM','VICTIM'),
    ('VOLUNTEER','VOLUNTEER')
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'email','password1','password2']
        widgets = {
            'first_name': forms.Select(choices=CHOICES)
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Register as"


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name')
        
   