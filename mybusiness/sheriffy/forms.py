from django.forms import ModelForm
# from .models import
from django import forms
from time import timezone


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[A-Za-z ]+'}))