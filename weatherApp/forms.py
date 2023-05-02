from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm, forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password...'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}))

    class Meta:
        model = User
        fields = ('username', 'password')