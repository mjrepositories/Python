from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from . import models as m
import datetime

class AirForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AirForm, self).__init__(*args, **kwargs)
        self.fields['date_of_email'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['comments'].widget = forms.Textarea(attrs={'wrap': 'hard', 'rows': "10", "cols": "70"})
        self.fields['email_subject'].widget = forms.TextInput(attrs={'size': "72"})
        self.fields['email_subject'].widget = forms.TextInput(attrs={'size': "72"})
    class Meta:
        model = m.Shipmentair
        fields = ['action_taken', 'pending_solved','mail_sent','date_of_email',
                  'email_subject','delay_in_answer','comments']


class FclForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FclForm, self).__init__(*args, **kwargs)
        self.fields['date_of_email'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['comments'].widget = forms.Textarea(attrs={'wrap': 'hard','rows':"10","cols":"70"})
        self.fields['email_subject'].widget = forms.TextInput(attrs={'size':"72"})

    class Meta:
        model = m.Shipmentfcl
        fields = ['action_taken', 'pending_solved','mail_sent','date_of_email',
                  'email_subject','delay_in_answer','comments']


class LclForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LclForm, self).__init__(*args, **kwargs)
        self.fields['date_of_email'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['comments'].widget = forms.Textarea(attrs={'wrap': 'hard', 'rows': "10", "cols": "70"})
        self.fields['email_subject'].widget = forms.TextInput(attrs={'size': "72"})

    class Meta:
        model = m.Shipmentlcl
        fields = ['action_taken', 'pending_solved','mail_sent','date_of_email',
                  'email_subject','delay_in_answer','comments']

class RoadEuForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoadEuForm, self).__init__(*args, **kwargs)
        self.fields['date_of_email'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['comments'].widget = forms.Textarea(attrs={'wrap': 'hard', 'rows': "10", "cols": "70"})
        self.fields['email_subject'].widget = forms.TextInput(attrs={'size': "72"})

    class Meta:
        model = m.Shipmentroadeu
        fields = ['action_taken', 'pending_solved','mail_sent','date_of_email',
                  'email_subject','delay_in_answer','comments']


class RoadUsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoadUsForm, self).__init__(*args, **kwargs)
        self.fields['date_of_email'] = forms.DateField(initial=datetime.date.today(),
                                              widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['comments'].widget = forms.Textarea(attrs={'wrap': 'hard', 'rows': "10", "cols": "70"})
        self.fields['email_subject'].widget = forms.TextInput(attrs={'size': "72"})

    class Meta:
        model = m.Shipmentroadus
        fields = ['action_taken', 'pending_solved','mail_sent','date_of_email',
                  'email_subject','delay_in_answer','comments']


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"

class FileForm(ModelForm):
    class Meta:
        model = m.ImportingFile
        fields = '__all__'