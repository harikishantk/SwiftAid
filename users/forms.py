from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

CHOICES = [
    ('VICTIM','VICTIM'),
    ('VOLUNTEER','VOLUNTEER')
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    option = forms.CharField(label="Register as: ", widget=forms.Select(choices=CHOICES))

    class Meta:
        model = User 
        fields = ['username', 'option', 'email','password1','password2']


class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    option = forms.CharField(label="Login as: ", widget=forms.Select(choices=CHOICES))


    class Meta:
        model = User
        fields = ('email', 'password', 'option')
        
