from django.forms import ModelForm
from django import forms

from .models import Ticket

# we imported modelform from django nd also Ticket model that we created

# We now need to create a form for entering data by users

class TicketForm(ModelForm):
    class Meta:
        # we are here indicating that we are creating a form for ticket creation (for which model it is built)
        model = Ticket
        # Now we indicate which fields we allow
        fields = ['issue', 'content', 'email']


class RawTicketForm(forms.Form):
    ISSUES = (
        ('Password expired', "Password expired"),
        ('Account blocked', 'Account blocked'),
        ("Don't remember the password", "Don't remember the password"),
        ("Other", "Other")
    )
    issue =forms.ChoiceField(choices=ISSUES,widget= forms.Select(attrs={'id':'issue','onchange':"myFunction()"}))
    content = forms.CharField(required=False,widget=forms.Textarea(attrs={'id':'content','rows':1}))
    email = forms.CharField(widget=forms.Textarea(attrs={'id': 'email', 'rows': 1}))


