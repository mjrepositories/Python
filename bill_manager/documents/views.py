from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import HomeForm,TVForm, InternetForm,GasForm,EnergyForm
from . import models
import datetime
import pandas as pd
from django.db.models import Q

# Create your views here.

def home_page(request):
    # creating variables for time
    cur_month = datetime.datetime.today().strftime('%B')
    cur_year = int(datetime.datetime.today().strftime('%Y'))
    # quering each model to show bills from current period
    cur_house = models.home_bill.objects.get(Q(year=cur_year)&Q(period=cur_month))
    cur_energy = models.energy_bill.objects.get(Q(year=cur_year)&Q(period=cur_month))
    cur_internet = models.internet_bill.objects.get(Q(year=cur_year)&Q(period=cur_month))
    cur_tv = models.tv_bill.objects.get(Q(year=cur_year)&Q(period=cur_month))
    cur_gas = models.gas_bill.objects.get(Q(year=cur_year)&Q(period__contains=cur_month))
    print(cur_house,cur_energy,cur_internet,cur_tv,cur_gas)

    # calculating total cost (based on all costs we have)
    cost_total = cur_house.warm_calculation + cur_house.cold_calculation + cur_energy.summary \
    + cur_gas.summary + cur_internet.price +cur_tv.price

    # creating list of urls for graph (will be used once bars are clicked)
    urls = ["",str(cur_house.image.url),cur_house.image.url,cur_energy.image.url,cur_gas.image.url,
            cur_internet.image.url,cur_tv.image.url]
    print(urls)
    # getting costs
    costs = [float(cost_total), float(cur_house.warm_calculation), float(cur_house.cold_calculation), \
             float(cur_energy.summary),float(cur_gas.summary), float(cur_internet.price), float(cur_tv.price)]
    print(costs)
    # creating labels for graph
    cost_names = ['Total','Warm Water','Cold Water','Energy','Gas','Internet','TV']
    # assinging variables to context and rendering page
    context = {'costs':costs,'cost_names':cost_names,'urls':urls}
    return render(request,'documents/home_page.html',context)

def register_cost_home(request):
    # getting current month
    cur_month = datetime.datetime.today().strftime('%B')
    # initiating form with initial variables
    form_home = HomeForm(initial={'paid':"YES",'period':cur_month})
    # if method is POST
    if request.method == "POST":
        print(request.POST)
        # filling form with POST data
        form_home = HomeForm(request.POST, request.FILES)
        # if form is valid
        if form_home.is_valid():
            # saving form and redirecting to home page
            form_home.save()
            return redirect('home-page')
        else:
            print(form_home.errors)
    # assigning form to context and rendering page
    context = {'form': form_home}
    return render(request,'documents/register_cost_home.html',context)

def correct_cost(request,group,id):
    # checking billing group
    if group =='home':
        # getting bill
        bill = models.home_bill.objects.get(pk=id)
        # initiating form with bill instance
        form = HomeForm(instance=bill)
        # if method is POST
        if request.method == "POST":
            # filling form with POSt data and bill instance
            home_form = HomeForm(request.POST, request.FILES, instance=bill)
            # if for valid
            if home_form.is_valid():
                # saving form and redirecting to group page
                home_form.save()
                return redirect('check-cost-home')
            else:
                print(home_form.errors)
        # assigning form to context and rendering page
        context = {'form':form}
        return render(request, 'documents/update_bill.html', context)
    # checking billing group
    if group =='tv':
        # getting bill
        bill = models.tv_bill.objects.get(pk=id)
        # filling form with bill instance
        form = TVForm(instance=bill)
        # if method is POST
        if request.method == "POST":
            # filling form with POSt data and bill instance
            tv_form = TVForm(request.POST, request.FILES, instance=bill)
            # if form is valid
            if tv_form.is_valid():
                # saving form and redirecting to group page
                tv_form.save()
                return redirect('check-cost-home')
            else:
                print(tv_form.errors)
        # assigning form to context and rendering page
        context = {'form':form}
        return render(request, 'documents/update_bill.html', context)
    # checking billing group
    elif group =='energy':
        # getting bill
        bill = models.energy_bill.objects.get(pk=id)
        # filling form with bill instance
        form = EnergyForm(instance=bill)
        # if method is POST
        if request.method == "POST":
            # filling form with POSt data and bill instance
            energy_form = EnergyForm(request.POST, request.FILES, instance=bill)
            # if form is valid
            if energy_form.is_valid():
                # saving form and redirecting to group page
                energy_form.save()
                return redirect('check-cost-home')
            else:
                print(energy_form.errors)
        # assigning form to context and rendering page
        context = {'form':form}
        return render(request, 'documents/update_bill.html', context)
    # checking billing group
    elif group =='gas':
        # getting bill
        bill = models.gas_bill.objects.get(pk=id)
        # filling form with bill instance
        form = GasForm(instance=bill)
        # if method is POST
        if request.method == "POST":
            # filling form with POSt data and bill instance
            gas_form = GasForm(request.POST, request.FILES, instance=bill)
            # if form is valid
            if gas_form.is_valid():
                # saving form and redirecting to group page
                gas_form.save()
                return redirect('check-cost-home')
            else:
                print(gas_form.errors)
        # assigning form to context and rendering page
        context = {'form':form}
        return render(request, 'documents/update_bill.html', context)
    # checking billing group
    elif group =='internet':
        # getting bill
        bill = models.internet_bill.objects.get(pk=id)
        # filling form with bill instance
        form = InternetForm(instance=bill)
        # if method is POST
        if request.method == "POST":
            # filling form with POSt data and bill instance
            internet_form = InternetForm(request.POST, request.FILES, instance=bill)
            # if form is valid
            if internet_form.is_valid():
                # saving form and redirecting to group page
                internet_form.save()
                return redirect('check-cost-home')
            else:
                print(internet_form.errors)
        # assigning form to context and rendering page
        context = {'form':form}
        return render(request, 'documents/update_bill.html', context)


def cost_home(request):
    # getting all home bills
    home_bills = models.home_bill.objects.all().order_by('-date')
    # getting costs for home bills
    costs = [float(x.cold_calculation) for x in home_bills.order_by('date')]
    # getting consumption of cold water
    consumption  = [float(x.consumption_cold) for x in home_bills.order_by('date')]
    # getting billing periods
    months = [f'{x.period} {x.year}' for x in home_bills.order_by('date')]
    print(months)
    # assigning variables to context and rendering page
    context = {"bills":home_bills,'costs':costs,'months':months,'consumption':consumption}
    return render(request,'documents/main_cost_home.html',context)


def register_cost_energy(request):
    # getting current month
    cur_month = datetime.datetime.today().strftime('%B')
    # initiating form with initial variables
    form_energy = EnergyForm(initial={'paid':"YES",'period':cur_month})
    # if method is POST
    if request.method == "POST":
        # filling form with POST data
        form_energy = EnergyForm(request.POST, request.FILES)
        # if form is valid
        if form_energy.is_valid():
            # saving form and redirecting to home page
            form_energy.save()
            return redirect('home-page')
        else:
            print(form_energy.errors)
    # assigning form to context and rendering page
    context = {'form': form_energy}
    return render(request,'documents/register_cost_energy.html',context)

def cost_energy(request):
    # getting of energy bills
    energy_bills = models.energy_bill.objects.all()
    # getting costs for billing periods
    costs = [float(x.summary) for x in energy_bills.order_by('date')]
    # getting consumption for billing periods
    consumption = [float(x.consumption) for x in energy_bills.order_by('date')]
    # getting billing periods
    months = [f'{x.period} {x.year}' for x in energy_bills.order_by('date')]
    # assigning variables to context and rendering page
    context = {'bills':energy_bills,'costs':costs,'consumption':consumption,'months':months}
    return render(request,'documents/main_cost_energy.html',context)

def register_cost_gas(request):
    # creating list for months
    x = pd.date_range('2016-01-01', '2016-12-31', freq='MS').strftime("%B").tolist()
    # creating list of periods
    list_periods = [f'{x[i]} - {x[i + 1]}' for i in range(0, 11, 2)]
    # getting current month
    tod = datetime.datetime.today().strftime("%B")
    # using function to check current period for gas bill
    period = picker(list_periods,tod)
    # initiating form with initial variables
    form_gas = GasForm(initial={'paid':"YES",'period':period})
    # if method is POST
    if request.method == "POST":
        # filling form with POST data
        form_gas = GasForm(request.POST, request.FILES)
        # if form is valid
        if form_gas.is_valid():
            # saving form and redirecting to home page
            form_gas.save()
            return redirect('home-page')
        else:
            print(form_gas.errors)
    # assigning form to context and rendering page
    context = {'form': form_gas}
    return render(request,'documents/register_cost_gas.html',context)

def cost_gas(request):
    # getting all gas bills
    gas_bills = models.gas_bill.objects.all()
    # getting costs for bills in each billing period
    costs = [float(x.summary) for x in gas_bills.order_by('date')]
    # getting consumption of gas for each billing period
    consumption = [float(x.consumption) for x in gas_bills.order_by('date')]
    # getting billing periods
    months = [f'{x.period} {x.year}' for x in gas_bills.order_by('date')]
    # assigning variables to context and rendering page
    context = {'bills':gas_bills,'costs':costs,'consumption':consumption,'months':months}
    return render(request,'documents/main_cost_gas.html',context)

def register_cost_internet(request):
    # getting current month
    cur_month = datetime.datetime.today().strftime('%B')
    # initiating form with initial values
    form_internet = InternetForm(initial={'paid':"YES",'period':cur_month})
    # if method is post
    if request.method == "POST":
        print(request.POST)
        # filling form with POST data
        form_internet = InternetForm(request.POST, request.FILES)
        # if form is valid
        if form_internet.is_valid():
            # saving form and redirecting to home page
            form_internet.save()
            return redirect('home-page')
        else:
            print(form_internet.errors)
    # assigning form to context and rendering page
    context = {'form': form_internet}
    return render(request,'documents/register_cost_internet.html',context)

def cost_internet(request):
    # getting internet bills
    internet_bills = models.internet_bill.objects.all()
    # getting costs for internet bills
    costs = [float(x.price) for x in internet_bills.order_by('date')]
    # getting billing periods
    months = [f'{x.period} {x.year}' for x in internet_bills.order_by('date')]
    # assigning variables to context and rendering page
    context = {'bills':internet_bills,'costs':costs,'months':months}
    return render(request,'documents/main_cost_internet.html',context)

def register_cost_tv(request):
    # getting current month
    cur_month = datetime.datetime.today().strftime('%B')
    # initiating form with initial values
    form_tv = TVForm(initial={'paid':"YES",'period':cur_month})
    # if method is POST
    if request.method == "POST":
        # filling form with POST data
        form_tv = TVForm(request.POST, request.FILES)
        # if form is valid
        if form_tv.is_valid():
            # saving form and redirecting to home page
            form_tv.save()
            return redirect('home-page')
        else:
            print(form_tv.errors)
    # assigning form to context and rendering page
    context = {'form': form_tv}
    return render(request,'documents/register_cost_tv.html',context)

def cost_tv(request):
    # getting tv bills
    tv_bills = models.tv_bill.objects.all()
    # getting costs for tv bills
    costs = [float(x.price) for x in tv_bills.order_by('date')]
    # getting billing periods
    months = [f'{x.period} {x.year}' for x in tv_bills.order_by('date')]
    # assigning variables to context and rendering page
    context = {'bills':tv_bills,'costs':costs,'months':months}
    return render(request,'documents/main_cost_tv.html',context)


# function returning period for gas bills

def picker(list_periods,tod):
    for period in list_periods:
        if tod in period:
            return period
