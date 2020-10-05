from django.shortcuts import render,redirect
from .forms import SpotForm,OfferForm,OfferFilteredForm
from .models import Spot,Stakeholder,Offer
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib import messages
from django.forms import formset_factory,modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

# data that was used when i was starting with the whole views.py
spotrequests = [
    {
        'gross_weight':1000,
        'volume':7.5,
         'origin_country':'NL',
         'origin_port':'AMS',
         'dest_country':'US',
         'dest_port':'LAX',
        'week':30
    },
    {
        'gross_weight': 2500,
        'volume': 14.9,
        'origin_country': 'PL',
        'origin_port': 'WAW',
        'dest_country': 'ID',
        'dest_port': 'BTH',
        'week':32
    }
]


# function based view that was rendering page while using the dummy data provided with dictionary

@login_required(login_url='login')
def home_view(request):
    # passing data from the dictionary to the context
    context = {
        'spotrequests':spotrequests
    }
    # returning page with context passed
    return render(request,'spotrequesting/starting.html',context)


# class based view for showing all spot quotes
class SpotListView(ListView,LoginRequiredMixin):
    # name of the model that is used
    model = Spot
    # template name that is being rendered
    template_name = 'spotrequesting/starting.html'
    # renaming context to loop over in page
    context_object_name = 'spotrequests'
    # overwritting function for getting data required to render page properly
    def get_context_data(self, *args, **kwargs):
        # creating context
        context = super(SpotListView, self).get_context_data(*args, **kwargs)
        # registering currently logged  user by geting to self and data present there
        currently_logged_mail = self.request.user.email
        # assigning currently logged in stakeholder
        currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)
        # if philips in in the email of user and F&D is group
        if 'philips' in self.request.user.email and "F&D" in currently_logged.group:
            currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)
            print('i am here philips')
            # gett all spot quotes that were registeredd by this user
            context['spotrequests'] = Spot.objects.all()
        # if philips in the email and key user is group
        if 'philips' in self.request.user.email and "key" in currently_logged.group:
            currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)
            print('i am here philips')
            # gett all spot quotes that were registeredd by this user
            context['spotrequests'] = Spot.objects.filter(requestor = self.request.user.pk)
        else:
            print('i am here carrier')
            # if it is carrier - get the Stakeholder that is logged in
            currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)
            # register all offers that were provided by this Stakeholder
            ofs = Offer.objects.filter(carrier = currently_logged)
            print(Offer.objects.all())
            # create list
            spotlist = []
            # looped over all offers
            for o in ofs:
                # add to the list all primary keys for offers that were provided by this user
                spotlist.append(o.spot.pk)
            print(spotlist)
                # add to context only those Spots that were still not provided with offer by the carrier
            context['spotrequests']  = Spot.objects.exclude(pk__in =spotlist)

        context['group'] = currently_logged.group
        print(currently_logged.group)
        # get the context from processing we done
        return context


# class based view for showing all  offers
class OfferListView(ListView,LoginRequiredMixin):
    # indicating model used
    model = Offer
    # indicating template name that is being generated
    template_name = 'spotrequesting/offer_overview.html'
    # renaming context to loop over in page
    context_object_name = 'offersubmissions'

    # overwritting function for getting data required to render page properly
    def get_context_data(self, *args, **kwargs):
        # creating context
        context = super(OfferListView, self).get_context_data(*args, **kwargs)
        # getting info on currently logged user
        currently_logged_mail = self.request.user.email
        # getting stakeholder logged in
        currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)
        print(currently_logged_mail)
        # if philips is in email address and user from F&D
        if 'philips' in self.request.user.email and "F&D" in currently_logged.group:
            # showing all offers
            context['offersubmissions'] = Offer.objects.all()
            print('philips guy')
        # if philips is in email address and user from key users
        if 'philips' in self.request.user.email and "key" in currently_logged.group:
            # filter spots that are for logged user
            spots = Spot.objects.filter(requestor = self.request.user.pk)
            # getting all spots
            all_spots = Spot.objects.all()
            # create a list of spot ids
            spots_id = [x.pk for x in all_spots]
            print(spots_id)
            # create a list of spots raised by user
            user_spots_id = [x.pk for x in spots]
            print(user_spots_id)
            # create list of spots that were not raised by logged user
            exclude_spots = [x for x in spots_id if x not in user_spots_id]
            print(exclude_spots)
            # get all offers with spots raised by the user
            offers = Offer.objects.exclude(spot__in=exclude_spots)
            print(offers)
            # pass offers to context
            context['offersubmissions'] = offers
            
            print('philips guy')

        else:
            # if carrier is logged in
            # get info on currently logged user
            currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)
            # pass to context all offers that were provided by this user
            context['offersubmissions'] = Offer.objects.filter(carrier=currently_logged.pk)
            print(context['offersubmissions'])
            print(self.request.user.pk)
        # passing group info
        context['group'] = currently_logged.group

        return context



# class based view for deleting offer
class OfferDeleteView(DeleteView,LoginRequiredMixin):
    # model used
    model = Offer
    # if offer is successfully delete - go to main page
    success_url = '/'



# class based view for updating spot
class SpotUpdateView(UpdateView,LoginRequiredMixin):
    # model used
    model = Spot
    # fields that can  be updated
    fields = ['gross_weight', 'volume', 'origin_country', 'origin_port', 'dest_country', 'dest_port',
                   'spot_status','ship_week']




# class based view for updating offer
class OfferUpdateView(UpdateView,LoginRequiredMixin):
    # model used
    model = Offer
    # fields that can be updated
    fields = ['currency','pickup','origin_cust','origin_hand','airfreight','dest_cust',
              'dest_hand','delivery','screening','dgfee','spot']
    # how context variable is named and can be used in template
    context_object_name = 'spotting'

@login_required(login_url='login')
# class based function to register spot
def register_spot(request):
    # getting Stakeholder which is logged in
    my_user = Stakeholder.objects.get(user=request.user)
    print(my_user.pk)
    # generating empty form
    form = SpotForm()
    # if method for request is POST
    if request.method =='POST':
        # if it is POST then it creates the object of form
        print("print",request.POST)
        print(type(request.POST))
        # change POST to mutable
        request.POST._mutable = True
        # assign user logged in to requestor
        request.POST['requestor'] = my_user.pk
        # fill in form with the data from POST
        form = SpotForm(request.POST)
        print(form)
        print(request.POST)
        # if form is valid
        if form.is_valid():
            # save form
            form.save()
            # assign last aspot to spot id
            request.session['spot_id'] = Spot.objects.last().pk
            # redirect to main page
            return redirect('/')
        else:
            print(form.errors)


    # pass form to context
    context = {'form': form,'group':my_user.group}

    # rendering page with passed context
    return render(request, 'spotrequesting/register_spot.html', context)


@login_required(login_url='login')
# functiton based view for creating  offers
def offer_spot(request):
    # if spot_identify is in post keys
    if 'spot_identify' in request.POST.keys():
        # save session spot_id variable from POST
        request.session['spot_id'] = request.POST.get('spot_identify')
    #  save session
    request.session.save()
    print('session created')
    print(request.session['spot_id'])
    # get spot by using id saved in sessiono
    my_spot = Spot.objects.get(pk=request.session['spot_id'])
    print(request.session['spot_id'])
    print(request.session.session_key)
    print(my_spot)
    # get user logged in
    my_user = Stakeholder.objects.get(user=request.user)
    my_s = Spot.objects.first()
    print(my_user)
    # prepare from
    form = OfferForm()
    # if method used is POST
    if request.method == 'POST':
        # make POST mutable
        request.POST._mutable = True
        # assign POSt request carrier as logged user
        request.POST['carrier'] = my_user.pk
        # assign POST request spot to spot filtered
        request.POST['spot'] = my_spot.pk
        print("print", request.POST)
        # fill in form with POST data
        form = OfferForm(request.POST)
        print(form)
        # if form is valid
        if form.is_valid():
            # save instance of form but not commit it
            instance = form.save(commit=False)
            # assign carrier and spot
            instance.carrier = my_user
            instance.spot = my_spot
            # save instance of form
            instance.save()
            # form.save()
            # redirecdt to all offers
            return redirect('/offers')
        else:
            print(form.errors)
        # pass context for template rendering
    context = {'form': form,'identify_spot':request.session['spot_id'],'my_spot':my_spot}

    # render template with context sent
    return render(request, 'spotrequesting/offer_spot.html', context)



# class based view for offer creation
class OfferCreateView(CreateView,LoginRequiredMixin):
    # indicating model used
    model = Offer
    # indicating fields that can be filled in
    fields = ['currency','pickup','origin_cust','origin_hand','airfreight','dest_cust',
              'dest_hand','delivery','screening','dgfee']



@login_required(login_url='login')
def OfferFiltered(request):
    # of spot_identity is present in POST data
    if 'spot_identity' in request.POST.keys():
        # then in session data is save
        request.session['spot_id_no'] = request.POST.get('spot_identity')
    # getting spot that has indicated primary key number
    my_spot = Spot.objects.get(pk=request.session['spot_id_no'])
    # getting all offers for found spot
    my_offers = Offer.objects.filter(spot=my_spot)
    # getting number of offers
    form_number = len(my_offers)
    no_of_offers = form_number
    print(my_offers)
    print(form_number)

    # creating model formset for all offers we have which will update only offer_status
    OfferFormSet = modelformset_factory(Offer,fields=('offer_status',),extra=form_number-form_number)
    # creating a query set based on all offers we have
    queryset = my_offers
    # generating form for offers we have
    formset = OfferFormSet(queryset=queryset)
    # creating zip to loop over in a template (for spot and for offer)
    mylist = zip(my_offers, formset)

    # if request method is post and we have more keys that one
    if request.method == "POST" and len(request.POST.keys())>2:
        # fill in formset with data from request.POST for offers we have
        formset = OfferFormSet(request.POST,queryset=queryset)
        # if formset is valud
        if formset.is_valid():
            instances  = formset.save(commit=False)
            # we create instances but not save them
            print(request.POST)
            # looping over each instance
            for instance in instances:
                # save instance
                instance.save()
            # once all is sdone - we assign status to offers as closed
            my_offers.update(closed='Closed')
            # and we redirect to main page
            return redirect('/')

    # getting info on currently logged user
    currently_logged_mail = request.user.email
    # getting stakeholder logged in
    currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)

    print(currently_logged)
    # getting all airfreights offered
    aircost = [x.airfreight for x in my_offers]
    # getting carrier names
    carriers = [x.carrier.user.username for x in my_offers]

    # if the there is at least one offer
    if form_number > 0:
        # indicated lowest offer with green , others with blue
        colors = ['green' if x == min(aircost) else 'blue' for x in aircost]
        # set minimum for y axis 0.2 below minimum value
        minimum = min(aircost) - 0.2
        # set maximum for y axis 0.2 above maximum value
        maximum = max(aircost) + 0.2

    # if there is at least one offer
    if form_number>0:
        # send all data prepared to context
        context = {'spot_requested':my_spot,'mylist':mylist,'formset':formset,
                   'group':currently_logged.group,'no':no_of_offers,
                   'aircost':aircost,'carriers':carriers,'colors':colors,
                   'minimum':minimum,'maximum':maximum}
    else:
        # send data to context without info on offers
        context = {'spot_requested': my_spot, 'mylist': mylist, 'formset': formset,
                   'group': currently_logged.group, 'no': no_of_offers,
                   'aircost': aircost, 'carriers': carriers}

    return render(request, 'spotrequesting/offers_filtered.html', context)


import csv

from django.http import HttpResponse


def export_offers_csv(request):
    # prepare HTTP Response
    response = HttpResponse(content_type='text/csv')
    # set what will be the content of response
    response['Content-Disposition'] = 'attachment; filename="offers.csv"'

    # create writer for csv
    writer = csv.writer(response)
    # write column headers in
    writer.writerow(['currency','pick_up','customs_origin','handling_origin','airfreight',
                     'customs_destination','handling_destination','delivery',
                     'screening_fee','carrier','decision'])

    # find spot
    my_spot = Spot.objects.get(pk=request.session['spot_id_no'])
    # getting all offers for found spot
    my_offers = Offer.objects.filter(spot=my_spot)

    # create list of values for offers
    offers = my_offers.values_list('currency','pickup','origin_cust','origin_hand',
                                            'airfreight','dest_cust','dest_hand','delivery',
                                            'screening','carrier__user__username','offer_status')
    # loop over each offer and write new row with data
    for of in offers:
        writer.writerow(of)

    # generate response
    return response


# BELOW VIEW NOT USED
def graphing(request):
    # check currently logged user
    currently_logged_mail = request.user.email
    # getting stakeholder logged in
    currently_logged = Stakeholder.objects.get(mail=currently_logged_mail)
    #
    data_for_graph = Offer.objects.filter(carrier=currently_logged.pk)
    # prepate air costs
    aircost = [x.airfreight for x in data_for_graph]
    # prepare carriers
    carriers = [x.carrier.user.username for x  in data_for_graph]
    print(aircost)
    print(carriers)


    return render(request, 'spotrequesting/chart.html', context={"data":data_for_graph,
                                                                 'aircost':aircost,'carriers':carriers})