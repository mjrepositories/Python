from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User


from .models import Order,Customer


# we are creating a customer form
#customer will be ale to update their own information
# but they won't be able to update the user
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude =['user']








# here  we import the model form as well as models that we have in our app

# we prepare then the form as a class

class OrderForm(ModelForm):
    class Meta:
        # here we need to indicate for which model we are
        # creating the form for
        model = Order
        fields = '__all__'
        # above is indicating that we want a form with all fields


# we are inheriting from UserCreationForm
class CreateUserForm(UserCreationForm):
    # we are creating a replicate of inherited model
    class Meta:
        model = User
        # we are specifying the fileds we want
        fields = ['username','email','password1','password2']