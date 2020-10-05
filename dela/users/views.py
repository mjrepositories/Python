from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# We will now create a register view

def register(request):

    # We are checking if the request type sent is "POST" so that we would like to send some info
    if request.method =='POST':
        # We are assing the data entered to the form
        form  = UserCreationForm(request.POST)
        # if the frm is valid - we would like to extract the username entered
        if form.is_valid():
            username = k

    # Here we have to create a form that will be used for user creation
    # Form will be a class that will be converted into HTML

    # We need to create an instance of the form
    form = UserCreationForm()

    # Now we have to render a template that will use the created form
    return render(request,'users/register.html',{'form':form})