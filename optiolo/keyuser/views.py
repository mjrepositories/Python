from django.shortcuts import render,redirect
from .models import Ticket
from django.contrib import messages

from .forms import TicketForm, RawTicketForm
from .models import Ticket
from django.views.generic import ListView,DetailView,UpdateView,DeleteView

# Create your views here.

calls=[ {
    'issue' : 'Password expired',
    'content' : '',
    'email' : 'maciej.janowski@philips.com',
    'status' : 'New',
    'kuser' : 'Maciej Janowski',
    'date_posted' : 'July 07, 2020'
},

{
    'issue' : 'Other',
    'content' : 'I am not smart enough to log in',
    'email' : 'maciej.janowski@philips.com',
    'status' : 'New',
    'date_posted' : 'July 07, 2020'
}
]
def home(request):
    return render(request,'keyuser/home.html')

def manager(request):

    # I am sending here all the tickets we have
    context={
        'calls':Ticket.objects.order_by('-date_posted').all()
    }
    # And i am adding that to the context that will be rendered
    return render(request,'keyuser/manager.html',context)



# this is a class base view to show the full list of tickets
class TicketListView(ListView):
    # variable is telling the class which model to query to show tickets
    model = Ticket
    # to be able to use a created template we have to specify a variable for that
    template_name = 'keyuser/manager.html'
    # we also need to specify here the variable that we will be looping over
    context_object_name = 'calls'

# this is a class base vie to show each ticket separately with details
class TicketDetailView(DetailView):
    # variable is telling the class which model to query to show tickets
    model = Ticket

# this is a class for deleting the ticket solved
class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = '/manager'


# this is a class base vie to show each ticket separately with details
class TicketUpdateView(UpdateView):
    # variable is telling the class which model to query to show tickets
    model = Ticket
    fields = ['status','kuser','issue','email','content']


def register(request):
    form = RawTicketForm()
    # checks if request method sent to server is post
    if request.method =='POST':
        # if it is POST then it creates the object of form
        print("print",request.POST)
        form =RawTicketForm(request.POST)
        if form.is_valid():
            Ticket.objects.create(**form.cleaned_data)
            form=RawTicketForm()
            messages.success(request, f'Your issue was successfully saved. Please wait for reply from key-users')

    # now we pass it to context so that it can be used on a page
    context = {'form':form}

    # And we are passing that to be rendered on  page
    return render(request,'keyuser/home.html',context)


        # # if the data is valid there
        # if form.is_valid():
        #     # it saves the form to the database
        #     form.save()
        #     # and it shows good information that account was created
        #     messages.success(request, f'You ticket has been created. Please wait for reply from key-users.')
        #      # while redirecting to the blog home page
        #     return redirect('login')
