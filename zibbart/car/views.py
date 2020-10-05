from django.shortcuts import render,redirect
from .forms import RepairForm,PartServiceForm
from django.views.generic import ListView,DeleteView,UpdateView
from .models import Repair,Service

# Create your views here.


def home_view(request):
    context = {'title': 'main'}
    return render(request,'car/home_page.html',context)


def create_service(request):
    form = RepairForm()
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/panel')

    context = {'form':form,'title':'service'}
    return render(request, 'car/service_page.html',context)

def check_history(request):
    context = {'title': 'history'}
    return render(request,'car/history_page.html',context)

def panel(request):
    context = {'title': 'panel'}
    return render(request,'car/panel_page.html',context)

# class based view for showing all spot quotes
class ServiceListView(ListView):
    # name of the model that is used
    model = Repair
    # template name that is being rendered
    template_name = 'car/panel_page.html'
    # renaming context to loop over in page
    context_object_name = 'repairs'


# class based view for deleting offer
class RepairDeleteView(DeleteView):
    # model used
    model = Repair
    # if offer is successfully delete - go to main page
    success_url = '/'

# class based view for updating offer
class RepairUpdateView(UpdateView):
    # model used
    model = Repair
    # fields that can be updated
    fields = '__all__'
    # how context variable is named and can be used in template
    context_object_name = 'repairs'
    # if offer is successfully delete - go to main page
    success_url = '/panel'


def create_part_or_service(request):
    if 'repair_no' in request.POST.keys():
        # save session spot_id variable from POST
        request.session['repair_id'] = request.POST.get('repair_no')
        #  save session
    request.session.save()
    print(request.session['repair_id'])
    my_repair = Repair.objects.get(pk=request.session['repair_id'])
    print(my_repair)
    print('hannah')
    my_parts = Service.objects.filter(what_provided='CZĘŚĆ',repair=my_repair)
    my_services= Service.objects.filter(what_provided='USŁUGA',repair=my_repair)
    print(my_services)
    form = PartServiceForm(initial={'repair':my_repair})
    print(request.POST)
    if request.method == 'POST' and len(request.POST.keys())>2:
        print(request.POST)
        form = PartServiceForm(request.POST)
        if form.is_valid():
            print('hello')
            print(request.POST)
            form.save()
            return redirect('/part_service')

        else:
            print(form.errors)

    context = {'form':form,'my_services':my_services,'my_parts':my_parts}
    return render(request, 'car/part_service_page.html',context)


# class based view for deleting offer
class ServiceDeleteView(DeleteView):
    # model used
    model = Service
    # if offer is successfully delete - go to main page
    success_url = '/part_service'

# class based view for updating offer
class ServiceUpdateView(UpdateView):
    # model used
    model = Service
    # fields that can be updated
    fields = '__all__'
    # how context variable is named and can be used in template
    context_object_name = 'services'
    # if offer is successfully delete - go to main page
    success_url = '/part_service'

def billing(request):
    if 'repair_no' in request.POST.keys():
        # save session spot_id variable from POST
        request.session['repair_id'] = request.POST.get('repair_no')
        #  save session
    request.session.save()
    my_repair = Repair.objects.get(pk=request.session['repair_id'])
    print(my_repair)
    print('hannah')
    my_parts = Service.objects.filter(what_provided='CZĘŚĆ', repair=my_repair)
    my_services = Service.objects.filter(what_provided='USŁUGA', repair=my_repair)
    sum_parts = 0
    sum_services = 0
    for x in my_parts:
        sum_parts += x.price

    for x in my_services:
        sum_services += x.price

    summing = str(sum_services+sum_parts)
    context={'my_parts':my_parts,"my_services":my_services,
             "sum_parts":str(sum_parts),"sum_services":str(sum_services),
             "plate":my_repair.plate,"car":my_repair.car,'sum':summing}
    return render(request,'car/billing.html',context)





from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': '2020-09-20',
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('car/billing.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('car/billing.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('car/billing.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")



import pdfkit
def PDF_generation(request):
    if 'repair_no_doc' in request.POST.keys():
        # save session spot_id variable from POST
        request.session['repair_id_doc'] = request.POST.get('repair_no_doc')
        #  save session
    request.session.save()
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_url('http://localhost:8000/billing', r'C:\Users\310295192\Desktop\testing\SEAT.pdf',configuration=config)
    return redirect('/panel')

