from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class AddCityForm(forms.ModelForm):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'City name...', 'class': 'text'}))
    class Meta:
        model = City
        fields = ['name']

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=100,  widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']