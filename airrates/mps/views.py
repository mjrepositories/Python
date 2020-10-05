from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Airlane
from .filters import AirFilter
import pandas as pd

def main_menu(request):
    carrier = list({x.carrier for x in Airlane.objects.all()})
    origin_country = list({x.origin_country for x in Airlane.objects.all()})
    origin_port = list({x.origin_port for x in Airlane.objects.all()})
    destination_country = list({x.dest_country for x in Airlane.objects.all()})
    destination_port = list({x.dest_port for x in Airlane.objects.all()})
    lane_id = list({x.laneid for x in Airlane.objects.all()})

    air_list = Airlane.objects.all()
    air_filter = AirFilter(request.GET, queryset=air_list)
    check_get = len(request.GET)
    cost = 0

    air_start = ''
    air_start_country = ''
    air_stop =''
    air_stop_country = ''
    sl_lvl =''
    service = ''

    if request.method == "POST":
        print(request.POST)
        weight = 0
        volume_weight = 0
        chargeable_weight = 0

        for key,value in request.POST.items():
            print(key,value)
            if len(value) <5:
                offer = Airlane.objects.get(id=value)
                currency = offer.currency
                pickup = offer.pickup
                origin_cust = offer.origin_cust
                origin_hand = offer.origin_hand
                airfreight = offer.airfreight
                dest_cust = offer.dest_cust
                dest_hand = offer.dest_hand
                delivery = offer.delivery
                screening = offer.screening
                screening_metric = offer.screening_metric
                dgfee = offer.dgfee
                dg_metric = offer.dg_metric

                air_start = offer.origin_port
                air_start_country = offer.origin_country
                air_stop = offer.dest_port
                air_stop_country = offer.dest_country
                sl_lvl = offer.service_lvl
                service = offer.carrier

            elif "xlsx" in value:
                df = pd.read_excel(r'C:\Users\310295192\Downloads\\'+ value)
                for index, row in df.iterrows():
                    weight += row['weight']
                    volume_weight += row['width'] * row['length'] * row['height']
                print(weight)
                print(volume_weight)

        chargeable_weight = weight if weight > volume_weight * 166.67 else volume_weight * 166.67

        charge_pickup = offer.pickup * chargeable_weight
        charge_origin_cust = offer.origin_cust
        charge_origin_hand = offer.origin_hand * chargeable_weight
        charge_airfreight = offer.airfreight * chargeable_weight
        charge_dest_cust = offer.dest_cust
        charge_dest_hand = offer.dest_hand * chargeable_weight
        charge_delivery = offer.delivery * chargeable_weight

        if screening_metric =='SHIPMENT':
            charge_screening = offer.screening
        else:
            charge_screening = offer.screening + chargeable_weight

        if dg_metric == "SHIPMENT":
            charge_dgfee = offer.dgfee
        else:
            charge_dgfee = offer.dgfee * chargeable_weight

        cost = charge_pickup + charge_origin_cust + charge_origin_hand + \
               charge_airfreight + charge_dest_cust + charge_origin_hand + \
                charge_screening

        cost = round(cost,2)


    if cost == 0:
        context = {'carrier': carrier, 'origin_country': origin_country, 'origin_port': origin_port,
               'destination_country': destination_country, 'destination_port': destination_port,
               'lane_id': lane_id, 'filter': air_filter, 'check_get': check_get, 'cost': cost}

    else:

        context = {'carrier':carrier,'origin_country':origin_country,'origin_port':origin_port,
               'destination_country':destination_country,'destination_port':destination_port,
               'lane_id':lane_id,'filter': air_filter,'check_get':check_get,'cost':cost,'currency':currency,
                   'chargeable_weight':chargeable_weight,"air_start":air_start,"air_stop":air_stop,
                   "air_start_country":air_start_country,"air_stop_country":air_stop_country,
                    "sl_lvl":sl_lvl,"service":service}

    return render(request,'mps/main_menu.html',context)


from django.http import HttpResponse

def export_template_xls(request):
    # prepare HTTP Response
    response = HttpResponse(content_type='application/vnd.ms-excel')
    # set what will be the content of response
    response['Content-Disposition'] = 'attachment; filename="template_packages.xlsx"'

    df = pd.DataFrame(columns=['package_ID', 'width', 'length', 'height', 'weight'])
    df.to_excel(response,index=False)

    # generate response
    return response