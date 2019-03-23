#Sergio González Muriel
from django import forms

class SimpleForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)