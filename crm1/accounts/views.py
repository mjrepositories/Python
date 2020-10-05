from django.shortcuts import render,redirect
from django.http import HttpResponse
# inlineformset enables us to created multiple forms within one form
from django.forms import inlineformset_factory

# we are importing form for using creation
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# we have to import models from models
from .models import *

from .forms import OrderForm,CreateUserForm,CustomerForm

# we are impoting filters
from .filters import OrderFilter

# we are importing the decorator we created
from .decorators import unauthenticated_user,allowed_users,admin_only

from django.contrib.auth.models import Group


from django.contrib.auth.decorators import login_required


# Create your views here.

# VIEW FOR register page
@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    # we are checking if method is POST
    if request.method == 'POST':
        # if it is - we fill in the Userform with data provided by the user
        # and we validate it if it is correct
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # # below is giving us the clean information about the username without any other attribute
            username = form.cleaned_data.get('username')
            # # we are assigning the group of "customer" to newly created user
            # group  = Group.objects.get(name='customer')
            # user.groups.add(group)
            #
            # # we are giving the user the customer
            # Customer.objects.create(user=user)
            messages.success(request,'Account was created for ' + username)
            # when the form is saved we are redirected to the login page
            return redirect('login')

    return render(request, 'accounts/register.html',{'form':form})

# view for login page
@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        # we are getting username an password sent from the page by the user
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password=password)

        # we are checking if we have this user registered
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {}
    return render(request,'accounts/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')
'''
Each of these functions is referring to the template we have created in  templates for our app
So depending on the url we type in we will go to specific template'''

# login_requred decorated is just giving the option so that we have to be logged in to
# have the access to the specific page
# if we are not logged in - we are redirected to specific website - in this case login page
@login_required(login_url='login')
@admin_only
def home(request):

    # below two lanes are quering the database to have information on orders and customers

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status= 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()

    # below is the dictionary that we will pass to template so that data achieved
    # from the database will be able to access
    context = {'orders':orders,'customers':customers,
               'total_orders':total_orders,
               'delivered':delivered,
               'pending':pending}
    return render(request,'accounts/dashboard.html',context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    # we are accessing orders for specific user
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()

    delivered = orders.filter(status= 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()

    print("orders: ",orders)
    context={'orders': orders, 'total_orders':total_orders,
             'delivered':delivered,'pending':pending}
    return render(request,'accounts/user.html',context)


# page is only available for users that are looged in and fo customer
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    # we are getting currently logged in customer
    customer=request.user.customer
    form = CustomerForm(instance=customer)


    if request.method == "POST":
        form=CustomerForm(request.POST,request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    # and we are passing the form to context so that it will be rendered
    context={'form':form}
    # it goes to account_settings html page
    return render(request,'accounts/account_settings.html',context)










@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
    # below is quering the database to get all the products available
    products = Product.objects.all()
    # second argument in the function below is enabling the template to read data from the database
    # in such siuation we will have to use "products" as the source of the data
    # because such variable was assigned to the data we pulled from the database by query above
    return render(request,'accounts/products.html',{'products':products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    # we are creating filter here
    # as the variables - we are sending a request data to this view
    # as for query set - we are passing all orders we have so that filter will refer to them


    # data is sent to the view, then view passes it to our filter,
    # filter works on queryset and renders the data out
    myFilter = OrderFilter(request.GET,queryset=orders)

    # and we are overwriting the data set of orders to those that
    # were selected by the filter we created
    orders = myFilter.qs

    # and we need to pass it to context
    context = {'customer':customer,'orders':orders,
               'order_count':order_count,'myFilter':myFilter}

    return render(request,'accounts/customer.html',context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):

    # for inlineformset we have to type in parent model as well as child model and then
    # we type in what fields we want to allow in the form
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    # using extra is enabling to have 10 fields


    # we are getting the customer here
    customer = Customer.objects.get(id=pk)
    # customer in the dictionary is referring to the variable of customer inmoels
    # And we are populating this value with the customer that we get from quering the database
    # Initial means that there will be some intial value already filling in the form we have on the webpage
    # and this value is from our database

    # queryset is hiding our already filled in forms
    formset = OrderFormSet(queryset = Order.objects.none(), instance = customer)

    # so we commented out the form to enable multiple forms at once
    #form = OrderForm(initial={'customer':customer})

    if request.method == "POST":
        # here we are filling in the data with what has been entered on the webpage and sent as POST data
        #form = OrderForm(request.POST)
        #print("Printing POST:", request.POST) / that what's left from previous exercise

        # we are commenting out form and replacing with formset
        # by passing the customer we are sharing the data that is currently available
        formset = OrderFormSet(request.POST, instance = customer)
        # If we for was filled in correctly and data is valid then we save it


        # if form.is_valid():
        #     # saving in th database
        #     form.save()
        #     return redirect('/')


        # we are switching the execution and we are not checking if formset is correct
        if formset.is_valid():
            # saving in th database
            formset.save()
            return redirect('/')

    # context={'form':form}
    # We are commenting out form to swithc to formset

    context = {'formset':formset}
    return render(request,'accounts/order_form.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):

    # we are quering here the data base by pasing the id number
    order = Order.objects.get(id=pk)

    # then form is filled in with the data for the instance that we queried
    form = OrderForm(instance=order)

    if request.method == "POST":
        # here we are filling in the data with what has been entered on the webpage and sent as POST data

        # by indicating the instance we are updating the already existing order and not creating a new one
        form = OrderForm(request.POST,instance=order)
        # print("Printing POST:", request.POST) / that what's left from previous exercise

        # If we for was filled in correctly and data is valid then we save it
        if form.is_valid():
            # saving in th database
            form.save()
            return redirect('/')


    # we pass the data for form to the variable and send it via content to our page
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)







@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    # if the method is Post
    if request.method == "POST":
        # we delete the item
        order.delete()
        # and we move to the main template
        return redirect('/')

    context ={'item':order}
    return render(request,'accounts/delete.html',context)
'''
Hierachy of looking through the folders
1. templates
2. accounts
3.
a) dashboard.html
b) profile.html
c) customer.html

'''