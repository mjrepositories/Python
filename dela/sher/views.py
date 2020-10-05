from django.shortcuts import render

# now we will the option to pull out the data from created database
# dot means that we are importing that from the current package/folder
from .models import Offer


# Create your views here.

offered_products = [
    {
        'seller':'Maciej',
        'product':'Stolnica',
        'description':'Mam do oddania stolnice. Rocznik 2010',
        'date_posted':'2020-04-30'
    },
    {
        'seller': 'Anna',
        'product': 'Mikser',
        'description': 'Super mikser. Swietnie miksuje. Zapraszam',
        'date_posted': '2020-04-10'
    },
    {
        'seller': 'Marek',
        'product': 'Cegi',
        'description': 'Oddam cegi nieuzywane',
        'date_posted': '2020-04-20'
    },
    {
        'seller': 'Monika',
        'product': 'Dyskietka',
        'description': 'Dyskietka z programem do analizy skladu ciala',
        'date_posted': '2020-04-29'
    },

]

def home(request):
    context = {'offers':Offer.objects.all(),'title':'Dela'}
    return render(request,'sher/home.html',context)

def about(request):
    return render(request,'sher/about.html')


def offers(request):
    return render(request,'sher/offers.html')
