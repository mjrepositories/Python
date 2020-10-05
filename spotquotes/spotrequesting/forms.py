from django.forms import ModelForm
from .models import Spot,Offer
from django import forms

class SpotForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SpotForm, self).__init__(*args, **kwargs)
        self.fields['gross_weight'].widget = forms.NumberInput(attrs={'min':0})
        self.fields['volume'].widget = forms.NumberInput(attrs={'min': 0})

    class Meta:
        model = Spot
        fields = [
            'gross_weight','volume','origin_country','origin_port',
            'dest_country','dest_port','ship_week','requestor'
                  ]


class OfferForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['currency'].widget = forms.TextInput(attrs={'oninput':"this.value = this.value.toUpperCase()", 'maxlength':"3"})

    class Meta:
        model = Offer
        fields = [
            'currency','pickup','origin_cust','origin_hand','airfreight','dest_cust','dest_hand',
            'delivery','screening','dgfee'
        ]



class OfferFilteredForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(OfferFilteredForm, self).__init__(*args, **kwargs)
    #     self.fields['offer_status'].widget = forms.CheckboxInput()
    #     self.fields['offer_status'].label = ''

    class Meta:
        model = Offer
        fields = [
            'offer_status'
            ]
        CHOICES= (
        ('Rejected','Rejected'),
        ('Accepted','Accepted')
    )
        widgets = {
            'offer_status': forms.Select(choices=CHOICES, attrs={'class': 'form-control'}),
        }
