from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,ItemForm,ItemPictureForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,Item,Image
import random
from django.views.generic import ListView,DeleteView,UpdateView
from django import forms
from django.forms import formset_factory,modelformset_factory,inlineformset_factory

# Create your views here.

def home_view(request):
    offers_all = Item.objects.all()
    ids = [x.id for x in offers_all]
    ids_to_show = random.sample(ids,3)
    offers = Item.objects.filter(id__in=ids_to_show)
    context = {'offers':offers}
    return render(request,'sheriffy/home_page.html',context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            username = form.cleaned_data.get('username')
            user = User.objects.last()
            uinfo = Profile.objects.get(user=user)
            uinfo.name = cd['name']
            uinfo.phone = cd['phone']
            uinfo.save()
            messages.success(request,f'Account was successfully created for you, {username}')
            print(request.POST)
            return redirect('home-page')

    else:
        form = UserRegisterForm()
        context = {'form':form}
    return render(request,'sheriffy/register.html',context)


# class based view for showing all  offers
class OfferListView(ListView):
    # indicating model used
    model = Item
    # indicating template name that is being generated
    template_name = 'sheriffy/my_offers.html'
    # renaming context to loop over in page
    context_object_name = 'items'

    # overwritting function for getting data required to render page properly
    def get_context_data(self, *args, **kwargs):
        # creating context
        context = super(OfferListView, self).get_context_data(*args, **kwargs)

        profile = Profile.objects.get(user=self.request.user)
        print(profile)
        # gett all offers that were registeredd by this user
        context['items'] = Item.objects.filter(owner=profile)
        print(context['items'])
        return context



def ItemCreate(request):
    profile = Profile.objects.get(user=request.user)

    form = ItemForm(initial={'status': 'Aktywne','owner':profile})
    ItemFormSet = inlineformset_factory(Item, Image, fields=('image',), extra=8)
    formset = ItemFormSet()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            item = Item.objects.filter(owner=profile).last()
            print(item)
            return redirect('/offers')
        else:
            print(form.errors)




    context = {'form': form,'formset':formset}
    return render(request,'sheriffy/item_create.html',context)


# class based view for deleting offer
class ItemDeleteView(DeleteView):
    # model used
    model = Item
    # if offer is successfully delete - go to main page
    success_url = '/offers'

# class based view for updating offer
class ItemUpdateView(UpdateView):
    # model used
    model = Item
    # fields that can be updated
    fields = ['description', 'state','category','zone']
    # how context variable is named and can be used in template
    context_object_name = 'item'
    # if offer is successfully delete - go to main page
    success_url = '/offers'

    def get_form(self,form_class=None):
        form = super(ItemUpdateView, self).get_form()
        form.fields['description'].widget = forms.Textarea(attrs={'wrap':'hard'})
        return form