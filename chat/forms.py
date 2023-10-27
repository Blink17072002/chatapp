from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(max_length=256, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'Enter your password', 'data-toggle': 'password'}))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}))
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        

