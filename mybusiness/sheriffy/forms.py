from django.forms import ModelForm
# from .models import
from django import forms
from time import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Item,Image



class ItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'wrap':'hard'})

    class Meta:
        model = Item
        fields = ['thing','description','city','zone','category','state','status','owner']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'pattern':"\d{3}-\d{3}-\d{3}",
                                                                        'placeholder':'123-456-789'}))

    class Meta:
        model = User
        fields = ['username','name','email','phone','password1','password2']


class ItemPictureForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']






