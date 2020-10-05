from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    # checks if request method sent to server is post
    if request.method =='POST':
        # if it is POST then it creates the object of form
        form = UserRegisterForm(request.POST)
         # if the data is valid there
        if form.is_valid():
            # it saves the form to the database
            form.save()
            # it assings the usernme to the variable
            username = form.cleaned_data.get('username')
            # and it shows good information that account was created
            # messages.success(request,f'Account created for {username}!')
            messages.success(request, f'You account has been created. You can no log in !')
             # while redirecting to the blog home page
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You account has been updated!')
             # while redirecting to the blog home page
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users\profile.html',context)