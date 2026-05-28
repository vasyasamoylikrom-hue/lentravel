from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('title', 'district', 'description', 'image')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")