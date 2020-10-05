from django.forms import ModelForm
from .models import Repair,Service
from django import forms
from django.conf import settings


class RepairForm(ModelForm):
    class Meta:
        model = Repair
        fields = '__all__'

        widgets = {
            'fix_date': forms.DateInput(attrs={'pattern':"\d{4}-\d{2}-\d{2}"})
        }

class PartServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

        SERVICE = (
            ('USŁUGA', 'USŁUGA'), ('CZĘŚĆ', 'CZĘŚĆ')
        )
        widgets = {

        'what_provided':forms.Select(choices=SERVICE,attrs={'onchange': "myFunction()"})
        }




