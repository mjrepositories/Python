from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import home_bill,gas_bill,energy_bill,internet_bill,tv_bill
from django.contrib.auth.models import User
import datetime

class HomeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(HomeForm, self).__init__(*args, **kwargs)
        cur_year = int(datetime.datetime.today().strftime('%Y'))
        self.fields['date'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['price_warm'].label = 'Price for heating water'
        self.fields['consumption_warm'].label = 'Consumption of warm water'
        self.fields['price_cold'].label = 'Price for cold water'
        self.fields['consumption_cold'].label = 'Consumption of cold water'
        self.fields['paid'].label = 'Do we have this paid?'
        self.fields['period'].label = 'What is the billing period?'
        self.fields['year'] = forms.IntegerField(initial=cur_year)
        self.fields['date'].label = 'Date of payment'
        self.fields['image'].label = 'Attach bill'


    class Meta:
        model = home_bill
        fields = '__all__'


class GasForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GasForm, self).__init__(*args, **kwargs)
        cur_day = datetime.datetime.today().strftime('%d/%m/%Y')
        cur_year = int(datetime.datetime.today().strftime('%Y'))
        self.fields['date'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['consumption'].label = 'Consumption of gas'
        self.fields['paid'].label = 'Do we have this paid?'
        self.fields['period'].label = 'What is the billing period?'
        self.fields['year'] = forms.IntegerField(initial=cur_year)
        self.fields['date'].label = 'Date of payment'
        self.fields['image'].label = 'Attach bill'

    class Meta:
        model = gas_bill
        fields = ['price','consumption','paid','period','year','date','notes','image']


class EnergyForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EnergyForm, self).__init__(*args, **kwargs)
        cur_day = datetime.datetime.today().strftime('%d/%m/%Y')
        cur_year = int(datetime.datetime.today().strftime('%Y'))
        # self.fields['date'].widget = forms.DateInput(attrs={"type":'date'})
        self.fields['date'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['year'] = forms.IntegerField(initial=cur_year)
        self.fields['consumption'].label = 'Consumption of energy'
        self.fields['paid'].label = 'Do we have this paid?'
        self.fields['period'].label = 'What is the billing period?'
        self.fields['date'].label = 'Date of payment'
        self.fields['year'].label = 'Billing year'
        self.fields['image'].label = 'Attach bill'

    class Meta:
        model = energy_bill
        fields = fields = ['price','consumption','paid','period','year','date','notes','image']


class InternetForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(InternetForm, self).__init__(*args, **kwargs)
        cur_year = int(datetime.datetime.today().strftime('%Y'))
        self.fields['date'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['price'].label = 'Price of service'
        self.fields['paid'].label = 'Do we have this paid?'
        self.fields['period'].label = 'What is the billing period?'
        self.fields['year'] = forms.IntegerField(initial=cur_year)
        self.fields['date'].label = 'Date of payment'
        self.fields['image'].label = 'Attach bill'

    class Meta:
        model = internet_bill
        fields = '__all__'


class TVForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(TVForm, self).__init__(*args, **kwargs)
        cur_year = int(datetime.datetime.today().strftime('%Y'))
        self.fields['date'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['price'].label = 'Price of service'
        self.fields['paid'].label = 'Do we have this paid?'
        self.fields['period'].label = 'What is the billing period?'
        self.fields['year'] = forms.IntegerField(initial=cur_year)
        self.fields['date'].label = 'Date of payment'
        self.fields['image'].label = 'Attach bill'

    class Meta:
        model = tv_bill
        fields = '__all__'