from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from . import models as m
from . import forms as f
import csv
from django.http import HttpResponse
import datetime
from django.db.models import Count
from django.conf import settings
import os
import pandas as pd
import numpy as np

# Create your views here.


def home_view(request):

    # Coverage for rates
    # get information on current day
    day = m.ShipmentsOverview.objects.last()
    # calculate coverage for current day
    daily = 100 - (day.missing_src +day.missing_matc + day.missing_dap)/day.number_all
    # round value for coverage
    daily = round(daily,2)
    # get historical data ascending
    history = m.ShipmentOverviewHistory.objects.all().order_by('reporting_date')
    # create list for historical coverage
    coverage = [float(x.coverage_all) for x in history]
    # create list for labels (days)
    dates = [x.reporting_date.strftime('%d-%m') for x in history]
    # add current day coverage to historical list
    coverage.append(daily)
    # add current date to labels
    dates.append(day.date_registered.strftime("%d-%m"))
    # create list for coloring bars
    colors = ['#63FA48' if x>98 else '#ff4538' for x in coverage]
    # create list for target line
    target =[98 for x in range(1,11)]
    # add values to context
    context = {'daily':coverage,'dates':dates,'colors':colors,'target':target}


    # General value of unrated shipments per domain
    daily_pie = [int(day.missing_dap),int(day.missing_matc),int(day.missing_src)]
    daily_pie_label = ['DAP','MATC','SRC']
    context.update({'daily_pie':daily_pie,'daily_pie_label':daily_pie_label})

    # Gap per carrier in AIR
    all_air = m.Shipmentair.objects.all()
    # get no. of shipments for ever carrier and order by this number
    air_shipments = all_air.values('leg_2_carrier_name').distinct().\
        annotate(ship_num=Count('shipment')).order_by('-ship_num')
    # create dictionary with uppercase names for carriers
    air_dict = {stat['leg_2_carrier_name'].upper():stat['ship_num'] for stat in air_shipments}
    # UPS, Expeditors, DHL, DB Schenker, CEVA, DSV,Nippon
    # create dictionary for stats
    air_ship = {'UPS':0,'EXPEDITORS':0,'DHL':0,'DB SCHENKER':0,'CEVA':0,'DSV':0,'NIPPON':0, 'OTHERS':0}
    # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
    for key,value in air_dict.items():
        if "UPS" in key:
            air_ship['UPS'] += value
        elif 'EXPEDITORS' in key:
            air_ship['EXPEDITORS'] += value
        elif 'DHL' in key:
            air_ship['DHL'] += value
        elif 'DB' in key:
            air_ship['DB SCHENKER'] += value
        elif 'CEVA' in key:
            air_ship['CEVA'] += value
        elif 'DSV' in key:
            air_ship['DSV'] += value
        elif 'NIPPON' in key:
            air_ship['NIPPON'] += value
        else:
            air_ship['OTHERS'] += value
    # sort dictionary by values
    air_ship = {k:v for k,v in sorted(air_ship.items(),key=lambda x:x[1],reverse=True)}
    # create list of carrier names and shipments without rates for passing to graph
    air_carriers = [name for name in air_ship.keys()]
    air_numbers = [number for number in air_ship.values()]
    # add two new tables to context for rendering
    context.update({'air_carriers':air_carriers,'air_numbers':air_numbers})


    # Gaps per carrier in FCL
    all_fcl = m.Shipmentfcl.objects.filter(~Q(leg_2_carrier_name=None))
    # get no. of shipments for ever carrier and order by this number
    fcl_shipments = all_fcl.values('leg_2_carrier_name').distinct().\
        annotate(ship_num=Count('shipment')).order_by('-ship_num')
    # create dictionary with uppercase names for carriers
    fcl_dict = {stat['leg_2_carrier_name'].upper(): stat['ship_num'] for stat in fcl_shipments}
    # create dictionary for stats
    fcl_ship = {'MAERSK': 0, 'SEALAND': 0, 'CNC': 0, 'ONE': 0, 'CMA': 0,
    'HYUNDAI': 0, 'HAPAG': 0,'COSCO':0,'APL':0,'EXPEDITORS':0, 'OTHERS': 0}
    # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
    for key, value in fcl_dict.items():
        if "MAERSK" in key and "SEALAND" not in key:
            fcl_ship['MAERSK'] += value
        elif 'SEALAND' in key:
            fcl_ship['SEALAND'] += value
        elif 'CNC' in key:
            fcl_ship['CNC'] += value
        elif 'ONE' in key:
            fcl_ship['ONE'] += value
        elif 'CMA' in key:
            fcl_ship['CMA'] += value
        elif 'HYUNDAI' in key:
            fcl_ship['HYUNDAI'] += value
        elif 'HAPAG' in key:
            fcl_ship['HAPAG'] += value
        elif 'COSCO' in key:
            fcl_ship['COSCO'] += value
        elif 'CMA' in key:
            fcl_ship['CMA'] += value
        elif 'EXPEDITORS' in key:
            fcl_ship['EXPEDITORS'] += value
        else:
            fcl_ship['OTHERS'] += value
    # sort dictionary by values
    fcl_ship = {k: v for k, v in sorted(fcl_ship.items(), key=lambda x: x[1], reverse=True)}
    fcl_ship = {k: v for k, v in fcl_ship.items() if v > 0}
    # create list of carrier names and shipments without rates for passing to graph
    fcl_carriers = [name for name in fcl_ship.keys()]
    fcl_numbers = [number for number in fcl_ship.values()]
    # add two new tables to context for rendering
    context.update({'fcl_carriers': fcl_carriers, 'fcl_numbers': fcl_numbers})

    # Gaps per carrier in LCL

    all_lcl = m.Shipmentlcl.objects.filter(~Q(leg_2_carrier_name=None))
    # get no. of shipments for ever carrier and order by this number
    lcl_shipments = all_lcl.values('leg_2_carrier_name').distinct(). \
        annotate(ship_num=Count('shipment')).order_by('-ship_num')
    # create dictionary with uppercase names for carriers
    lcl_dict = {stat['leg_2_carrier_name'].upper(): stat['ship_num'] for stat in lcl_shipments}
    # create dictionary for stats
    lcl_ship = {'DB SCHENKER':0,'OTHERS':0}
    # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
    for key, value in lcl_dict.items():
        if "DB SCHENKER" in key and "RAIL" not in key:
            lcl_ship['DB SCHENKER'] += value
        else:
            lcl_ship['OTHERS'] += value
    # sort dictionary by values
    lcl_ship = {k: v for k, v in sorted(lcl_ship.items(), key=lambda x: x[1], reverse=True)}
    # create list of carrier names and shipments without rates for passing to graph
    lcl_carriers = [name for name in lcl_ship.keys()]
    lcl_numbers = [number for number in lcl_ship.values()]
    # add two new tables to context for rendering
    context.update({'lcl_carriers': lcl_carriers, 'lcl_numbers': lcl_numbers})

    # Gaps per carrier in Road

    all_road_us = m.Shipmentroadus.objects.filter(~Q(leg_1_carrier_name=None))
    all_road_eu = m.Shipmentroadeu.objects.filter(~Q(leg_1_carrier_name=None))
    # get no. of shipments for ever carrier and order by this number
    roadus_shipments = all_road_us.values('leg_1_carrier_name').distinct(). \
        annotate(ship_num=Count('shipment')).order_by('-ship_num')
    roadeu_shipments = all_road_eu.values('leg_1_carrier_name').distinct(). \
        annotate(ship_num=Count('shipment')).order_by('-ship_num')
    # create dictionary with uppercase names for carriers
    road_dict_us = {stat['leg_1_carrier_name'].upper(): stat['ship_num'] for stat in roadus_shipments}
    road_dict_eu = {stat['leg_1_carrier_name'].upper(): stat['ship_num'] for stat in roadeu_shipments}
    road_all = {**road_dict_eu,**road_dict_us}
    # create dictionary for stats
    road_ship = {'SMH': 0, 'DSV': 0,'DHL': 0, 'CH ROBINSON': 0,'DACHSER': 0, 'MARS': 0,
                 'DB SCHENKER': 0, 'LANDSTAR': 0,'ECHO': 0, 'OTHERS': 0}
    # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
    for key, value in road_all.items():
        if "SPEDITION" in key:
            road_ship['SMH'] += value
        elif "DSV" in key:
            road_ship['DSV'] += value
        elif "ROBINSON" in key:
            road_ship['CH ROBINSON'] += value
        if "DACHSER" in key:
            road_ship['DACHSER'] += value
        elif "DB SCHENKER" in key:
            road_ship['DB SCHENKER'] += value
        elif "LANDSTAR" in key:
            road_ship['LANDSTAR'] += value
        if "ECHO" in key:
            road_ship['ECHO'] += value
        elif "DHL" in key:
            road_ship['DHL'] += value
        elif "MARS" in key:
            road_ship['MARS'] += value
        else:
            road_ship['OTHERS'] += value
    # sort dictionary by values
    road_ship = {k: v for k, v in sorted(road_ship.items(), key=lambda x: x[1], reverse=True)}
    # deleting others
    del road_ship['OTHERS']
    road_ship = {k:v for k,v in road_ship.items() if v > 0}
    # create list of carrier names and shipments without rates for passing to graph
    road_carriers = [name for name in road_ship.keys()]
    road_numbers = [number for number in road_ship.values()]
    # add two new tables to context for rendering
    context.update({'road_carriers': road_carriers, 'road_numbers': road_numbers})

    return render(request, 'manager/home_page.html',context)

def charts(request,t_type):
    # creating color list for pie charts
    colors = ["#3498db", "#f59342", "#2ecc71",'#fc0303','#090991','#dce307']
    # initiating context
    context={}
    # checking type of transport
    if t_type == 'AIR':
        all_infodis = m.Shipmentair.objects.all()
        # get no. of shipments for ever carrier and order by this number
        infodis_shipments = all_infodis.values('leg_2_carrier_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for carriers
        infodis_dict = {stat['leg_2_carrier_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # UPS, Expeditors, DHL, DB Schenker, CEVA, DSV,Nippon
        # create dictionary for stats
        infodis_ship = {'UPS': 0, 'EXPEDITORS': 0, 'DHL': 0, 'DB SCHENKER': 0,
                    'CEVA': 0, 'DSV': 0, 'NIPPON': 0}
        # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
        for key, value in infodis_dict.items():
            if "UPS" in key:
                infodis_ship['UPS'] += value
            elif 'EXPEDITORS' in key:
                infodis_ship['EXPEDITORS'] += value
            elif 'DHL' in key:
                infodis_ship['DHL'] += value
            elif 'DB' in key:
                infodis_ship['DB SCHENKER'] += value
            elif 'CEVA' in key:
                infodis_ship['CEVA'] += value
            elif 'DSV' in key:
                infodis_ship['DSV'] += value
            elif 'NIPPON' in key:
                infodis_ship['NIPPON'] += value
            else:
                infodis_ship[key] = value
        # sort dictionary by values
        infodis_ship = {k: v for k, v in sorted(infodis_ship.items(), key=lambda x: x[1], reverse=True)}
        # create list of carrier names and shipments without rates for passing to graph
        carriers = [name for name in infodis_ship.keys()]
        numbers = [number for number in infodis_ship.values()]

        # calculating gaps per domain
        infodis_shipments = all_infodis.values('domain_code').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for domains
        infodis_dict = {stat['domain_code'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting domains stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # create list for storing data for domain
        domain = []
        domain_stats = []
        #  looping over data for domains and assigning values to lists for context
        for k,v in infodis_dict.items():
            domain.append(k)
            domain_stats.append(v)
        # adjusting names for domains
        domain = ['DAP' if x=="CL" else x for x in domain]
        domain = ['MATC' if x == "PHILIPSM1" else x for x in domain]
        domain = ['SPS' if x == "PHILIPSSPS" else x for x in domain]
        # assigning colors pallet
        coloring = colors[0:len(domain)]
        # checking shipments per origin country
        infodis_shipments = all_infodis.values('pickup_country').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['pickup_country'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        country = []
        country_stats = []
        # assigning values to list in loop
        for k,v in infodis_dict.items():
            country.append(k)
            country_stats.append(v)
        # taking only values which are higher than 1
        country = country[0:country_stats.index(1)]
        country_stats = country_stats[0:country_stats.index(1)]

        # checking shipments per booker
        infodis_shipments = all_infodis.values('shipment_booker_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['shipment_booker_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        booker = []
        booker_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            booker.append(k)
            booker_stats.append(v)

        booker = booker[0:13]
        booker_stats = booker_stats[0:13]


        title_main = 'Missing AIR rates per carrier'
        title_pie = 'AIR gaps per domain'
        title_pick_up = 'AIR gaps per pickup country'
        title_booker = ' AIR gaps per booker'
        # add tables to context for rendering
        context.update({'carriers': carriers, 'numbers': numbers,'domain':domain,'domain_stats':domain_stats,
                       'coloring':coloring,'country':country,'country_stats':country_stats,'title_main':title_main,
                        'title_pie':title_pie,'title_pick_up':title_pick_up,'title_booker':title_booker,
                        'booker':booker,'booker_stats':booker_stats})


    # checking type of transport -FCL
    elif t_type == 'FCL':
        all_infodis = m.Shipmentfcl.objects.filter(~Q(leg_2_carrier_name=None))
        # get no. of shipments for ever carrier and order by this number
        infodis_shipments = all_infodis.values('leg_2_carrier_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for carriers
        infodis_dict = {stat['leg_2_carrier_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # UPS, Expeditors, DHL, DB Schenker, CEVA, DSV,Nippon
        # create dictionary for stats
        infodis_ship = {'MAERSK': 0, 'SEALAND': 0, 'CNC': 0, 'ONE': 0, 'CMA': 0,
    'HYUNDAI': 0, 'HAPAG': 0,'COSCO':0,'APL':0,'EXPEDITORS':0}
        if 'MEDITERRANEAN SHIPPING COMPANY S' in infodis_dict.keys():
            del infodis_dict['MEDITERRANEAN SHIPPING COMPANY S']
        if 'DHL LCL OCEAN S (CONSOLIDATION)' in infodis_dict.keys():
            del infodis_dict['DHL LCL OCEAN S (CONSOLIDATION)']
        # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
        for key, value in infodis_dict.items():
            if "MAERSK" in key and "SEALAND" not in key:
                infodis_ship['MAERSK'] += value
            elif 'EXPEDITORS' in key:
                infodis_ship['EXPEDITORS'] += value
            elif 'SEALAND' in key:
                infodis_ship['SEALAND'] += value
            elif 'CNC' in key:
                infodis_ship['CNC'] += value
            elif 'ONE' in key:
                infodis_ship['ONE'] += value
            elif 'CMA' in key:
                infodis_ship['CMA'] += value
            elif 'HYUNDAI' in key:
                infodis_ship['HYUNDAI'] += value
            elif 'HAPAG' in key:
                infodis_ship['HAPAG'] += value
            elif 'COSCO' in key:
                infodis_ship['COSCO'] += value
            else:
                infodis_ship[key] = value
        # sort dictionary by values
        infodis_ship = {k: v for k, v in sorted(infodis_ship.items(), key=lambda x: x[1], reverse=True)}
        # create list of carrier names and shipments without rates for passing to graph
        carriers = [name for name in infodis_ship.keys()]
        numbers = [number for number in infodis_ship.values()]
        carriers = carriers[:12]
        numbers = numbers[:12]
        # calculating gaps per domain
        infodis_shipments = all_infodis.values('domain_code').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for domains
        infodis_dict = {stat['domain_code'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting domains stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # create list for storing data for domain
        domain = []
        domain_stats = []
        #  looping over data for domains and assigning values to lists for context
        for k, v in infodis_dict.items():
            domain.append(k)
            domain_stats.append(v)
        # adjusting names for domains
        domain = ['DAP' if x == "CL" else x for x in domain]
        domain = ['MATC' if x == "PHILIPSM1" else x for x in domain]
        domain = ['SPS' if x == "PHILIPSSPS" else x for x in domain]
        # assigning colors pallet
        coloring = colors[0:len(domain)]
        # checking shipments per origin country
        infodis_shipments = all_infodis.values('pickup_country').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['pickup_country'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        country = []
        country_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            country.append(k)
            country_stats.append(v)
        # taking only values which are higher than 1
        country = country[0:country_stats.index(1)]
        country_stats = country_stats[0:country_stats.index(1)]

        # checking shipments per booker
        infodis_shipments = all_infodis.values('shipment_booker_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['shipment_booker_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        booker = []
        booker_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            booker.append(k)
            booker_stats.append(v)

        booker = booker[0:13]
        booker_stats = booker_stats[0:13]

        title_main = 'Missing FCL rates per carrier'
        title_pie = 'FCL gaps per domain'
        title_pick_up = 'FCL gaps per pickup country'
        title_booker = ' FCL gaps per booker'
        # add tables to context for rendering
        context.update({'carriers': carriers, 'numbers': numbers, 'domain': domain, 'domain_stats': domain_stats,
                        'coloring': coloring, 'country': country, 'country_stats': country_stats,
                        'title_main': title_main,
                        'title_pie': title_pie, 'title_pick_up': title_pick_up, 'title_booker': title_booker,
                        'booker': booker, 'booker_stats': booker_stats})

    # checking type of transport - LCL
    elif t_type == 'LCL':
        all_infodis = m.Shipmentlcl.objects.filter(~Q(leg_2_carrier_name=None))
        # get no. of shipments for ever carrier and order by this number
        infodis_shipments = all_infodis.values('leg_2_carrier_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for carriers
        infodis_dict = {stat['leg_2_carrier_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # UPS, Expeditors, DHL, DB Schenker, CEVA, DSV,Nippon
        # create dictionary for stats
        infodis_ship = {'DB SCHENKER LCL': 0}

        # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
        for key, value in infodis_dict.items():
            if "DB SCHENKER" in key and "RAIL" not in key:
                infodis_ship['DB SCHENKER LCL'] += value
            else:
                infodis_ship[key] = value
        # sort dictionary by values
        infodis_ship = {k: v for k, v in sorted(infodis_ship.items(), key=lambda x: x[1], reverse=True)}
        # create list of carrier names and shipments without rates for passing to graph
        carriers = [name for name in infodis_ship.keys()]
        numbers = [number for number in infodis_ship.values()]
        carriers = carriers[:12]
        numbers = numbers[:12]
        # calculating gaps per domain
        infodis_shipments = all_infodis.values('domain_code').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for domains
        infodis_dict = {stat['domain_code'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting domains stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # create list for storing data for domain
        domain = []
        domain_stats = []
        #  looping over data for domains and assigning values to lists for context
        for k, v in infodis_dict.items():
            domain.append(k)
            domain_stats.append(v)
        # adjusting names for domains
        domain = ['DAP' if x == "CL" else x for x in domain]
        domain = ['MATC' if x == "PHILIPSM1" else x for x in domain]
        domain = ['SPS' if x == "PHILIPSSPS" else x for x in domain]
        # assigning colors pallet
        coloring = colors[0:len(domain)]
        # checking shipments per origin country
        infodis_shipments = all_infodis.values('pickup_country').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['pickup_country'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        country = []
        country_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            country.append(k)
            country_stats.append(v)
        # taking only values which are higher than 1
        country = country[0:country_stats.index(1)]
        country_stats = country_stats[0:country_stats.index(1)]

        # checking shipments per booker
        infodis_shipments = all_infodis.values('shipment_booker_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['shipment_booker_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        booker = []
        booker_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            booker.append(k)
            booker_stats.append(v)

        booker = booker[0:13]
        booker_stats = booker_stats[0:13]

        title_main = 'Missing LCL rates per carrier'
        title_pie = 'LCL gaps per domain'
        title_pick_up = 'LCL gaps per pickup country'
        title_booker = ' LCL gaps per booker'
        # add tables to context for rendering
        context.update({'carriers': carriers, 'numbers': numbers, 'domain': domain, 'domain_stats': domain_stats,
                        'coloring': coloring, 'country': country, 'country_stats': country_stats,
                        'title_main': title_main,
                        'title_pie': title_pie, 'title_pick_up': title_pick_up, 'title_booker': title_booker,
                        'booker': booker, 'booker_stats': booker_stats})

    # checking type of transport - ROAD US
    elif t_type == 'ROAD_US':
        all_infodis = m.Shipmentroadus.objects.filter(~Q(leg_1_carrier_name=None))
        # get no. of shipments for ever carrier and order by this number
        infodis_shipments = all_infodis.values('leg_1_carrier_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for carriers
        infodis_dict = {stat['leg_1_carrier_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # create dictionary for stats
        infodis_ship = {'LANDSTAR': 0,'CH ROBINSON':0,'ECHO':0}
        # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
        for key, value in infodis_dict.items():
            if "LANDSTAR" in key:
                infodis_ship['LANDSTAR'] += value
            elif 'ROBINSON' in key:
                infodis_ship['CH ROBINSON'] += value
            elif 'ECHO' in key:
                infodis_ship['ECHO'] += value
            else:
                infodis_ship[key] = value
        # sort dictionary by values
        infodis_ship = {k: v for k, v in sorted(infodis_ship.items(), key=lambda x: x[1], reverse=True)}
        # create list of carrier names and shipments without rates for passing to graph
        carriers = [name for name in infodis_ship.keys()]
        numbers = [number for number in infodis_ship.values()]
        carriers = carriers[:12]
        numbers = numbers[:12]
        # calculating gaps per domain
        infodis_shipments = all_infodis.values('domain_code').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for domains
        infodis_dict = {stat['domain_code'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting domains stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # create list for storing data for domain
        domain = []
        domain_stats = []
        #  looping over data for domains and assigning values to lists for context
        for k, v in infodis_dict.items():
            domain.append(k)
            domain_stats.append(v)
        # adjusting names for domains
        domain = ['DAP' if x == "CL" else x for x in domain]
        domain = ['MATC' if x == "PHILIPSM1" else x for x in domain]
        domain = ['SPS' if x == "PHILIPSSPS" else x for x in domain]
        # assigning colors pallet
        coloring = colors[0:len(domain)]

        # checking shipments per origin country
        infodis_shipments = all_infodis.values('pickup_country').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['pickup_country'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        country = []
        country_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            country.append(k)
            country_stats.append(v)
        # # taking only values which are higher than 1
        # country = country[0:country_stats.index(1)]
        # country_stats = country_stats[0:country_stats.index(1)]

        # checking shipments per booker
        infodis_shipments = all_infodis.values('shipment_booker_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['shipment_booker_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        booker = []
        booker_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            booker.append(k)
            booker_stats.append(v)

        booker = booker[0:13]
        booker_stats = booker_stats[0:13]

        title_main = 'Missing ROAD US rates per carrier'
        title_pie = 'ROAD US gaps per domain'
        title_pick_up = 'ROAD US gaps per pickup country'
        title_booker = 'ROAD US gaps per booker'
        # add tables to context for rendering
        context.update({'carriers': carriers, 'numbers': numbers, 'domain': domain, 'domain_stats': domain_stats,
                        'coloring': coloring, 'country': country, 'country_stats': country_stats,
                        'title_main': title_main,
                        'title_pie': title_pie, 'title_pick_up': title_pick_up, 'title_booker': title_booker,
                        'booker': booker, 'booker_stats': booker_stats})

    # checking type of transport - ROAD EU
    elif t_type == 'ROAD_EU':
        all_infodis = m.Shipmentroadeu.objects.filter(~Q(leg_1_carrier_name=None))
        # get no. of shipments for ever carrier and order by this number
        infodis_shipments = all_infodis.values('leg_1_carrier_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for carriers
        infodis_dict = {stat['leg_1_carrier_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # create dictionary for stats
        infodis_ship = {'DACHSER': 0,'DSV':0,'DHL':0,'SPEDITION HELMUT MULLER':0,
                        'CH ROBINSON':0,'DB SCHENKER':0}
        # loop over all entries in dictionary. If key contains carrier name -> add value to stats dictionary
        for key, value in infodis_dict.items():
            if "DSV" in key:
                infodis_ship['DSV'] += value
            elif 'DHL' in key:
                infodis_ship['DHL'] += value
            elif 'DACHSER' in key:
                infodis_ship['DACHSER'] += value
            elif 'SCHENKER' in key:
                infodis_ship['DB SCHENKER'] += value
            elif 'ROBINSON' in key:
                infodis_ship['CH ROBINSON'] += value
            elif 'SPEDITION' in key:
                infodis_ship['SPEDITION HELMUT MULLER'] += value
            else:
                infodis_ship[key] = value
        # sort dictionary by values
        infodis_ship = {k: v for k, v in sorted(infodis_ship.items(), key=lambda x: x[1], reverse=True)}
        # create list of carrier names and shipments without rates for passing to graph
        carriers = [name for name in infodis_ship.keys()]
        numbers = [number for number in infodis_ship.values()]
        carriers = carriers[:12]
        numbers = numbers[:12]
        # calculating gaps per domain
        infodis_shipments = all_infodis.values('domain_code').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for domains
        infodis_dict = {stat['domain_code'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting domains stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # create list for storing data for domain
        domain = []
        domain_stats = []
        #  looping over data for domains and assigning values to lists for context
        for k, v in infodis_dict.items():
            domain.append(k)
            domain_stats.append(v)
        # adjusting names for domains
        domain = ['DAP' if x == "CL" else x for x in domain]
        domain = ['MATC' if x == "PHILIPSM1" else x for x in domain]
        domain = ['SPS' if x == "PHILIPSSPS" else x for x in domain]
        # assigning colors pallet
        coloring = colors[0:len(domain)]

        # checking shipments per origin country
        infodis_shipments = all_infodis.values('pickup_country').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['pickup_country'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        country = []
        country_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            country.append(k)
            country_stats.append(v)
        # # taking only values which are higher than 1
        # country = country[0:country_stats.index(1)]
        # country_stats = country_stats[0:country_stats.index(1)]

        # checking shipments per booker
        infodis_shipments = all_infodis.values('shipment_booker_name').distinct(). \
            annotate(ship_num=Count('shipment')).order_by('-ship_num')
        # create dictionary with uppercase names for origin country
        infodis_dict = {stat['shipment_booker_name'].upper(): stat['ship_num'] for stat in infodis_shipments}
        # sorting origin country stats
        infodis_dict = {k: v for k, v in sorted(infodis_dict.items(), key=lambda x: x[1], reverse=True)}
        # creating lists for storing data for countries
        booker = []
        booker_stats = []
        # assigning values to list in loop
        for k, v in infodis_dict.items():
            booker.append(k)
            booker_stats.append(v)

        booker = booker[0:13]
        booker_stats = booker_stats[0:13]

        title_main = 'Missing ROAD EU rates per carrier'
        title_pie = 'ROAD EU gaps per domain'
        title_pick_up = 'ROAD EU gaps per pickup country'
        title_booker = 'ROAD EU gaps per booker'
        # add tables to context for rendering
        context.update({'carriers': carriers, 'numbers': numbers, 'domain': domain, 'domain_stats': domain_stats,
                        'coloring': coloring, 'country': country, 'country_stats': country_stats,
                        'title_main': title_main,
                        'title_pie': title_pie, 'title_pick_up': title_pick_up, 'title_booker': title_booker,
                        'booker': booker, 'booker_stats': booker_stats})

    # rendering page
    return render(request,'manager/charts.html',context)


def register(request):
    # if method is POST
    if request.method == "POST":
        # passing data for user to user form
        form = f.CustomUserCreationForm(request.POST)
        # if form is valid
        if form.is_valid():
            # creating user
            form.save()
            messages.success(request, f'Account was successfully created for you')
            # authenticating newly created user into app
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            # logging with authentication
            login(request, new_user)
            return redirect('home_page')
    else:
        # initiating form
        form = f.CustomUserCreationForm()
        # sending form to context for rendering
        context = {'form': form}
    return render(request, 'manager/register.html',context)


def about(request):
    return render(request, 'manager/about.html')


def shipments(request,t_type):
    # if transport type if FCL
    if t_type == "FCL":
        # get all FCL shipments, send to context and render page
        transports = m.Shipmentfcl.objects.all().order_by('pending_solved')
        context = {"transports":transports}
        return render(request, 'manager/shipments.html',context)
    # if transport type is LCL
    elif t_type == "LCL":
        # get all LCL shipments, send to context and render page
        transports = m.Shipmentlcl.objects.all().order_by('pending_solved')
        context = {"transports": transports}
        return render(request, 'manager/shipments.html',context)
    # if transport type is AIR
    elif t_type == "AIR":
        # get all AIR shipments, send to context and render page
        transports = m.Shipmentair.objects.all().order_by('pending_solved')
        context = {"transports": transports}
        return render(request, 'manager/shipments.html', context)
    # if transport type is ROAD EU
    elif t_type == "ROAD_EU":
        # get all ROAD EU shipments, send to context and render page
        transports = m.Shipmentroadeu.objects.all().order_by('pending_solved')
        context = {"transports": transports}
        return render(request, 'manager/shipments.html', context)
    # if transport type is ROAD US
    elif t_type == "ROAD_US":
        # get all ROAD US shipments, send to context and render page
        transports = m.Shipmentroadus.objects.all().order_by('pending_solved')
        context = {"transports": transports}
        return render(request, 'manager/shipments.html', context)


def reporting(request,t_type):
    # if method is GET
    if request.method =='GET':
        # if transport type is FCL
        if t_type == "FCL":
            transports = m.Shipmentfcl.objects.all()
            context = {"transports": transports}

        # if transport type is LCL
        elif t_type == "LCL":
            transports = m.Shipmentlcl.objects.all()
            context = {"transports": transports}

        # if transport type is AIR
        elif t_type == "AIR":
            transports = m.Shipmentair.objects.all()
            context = {"transports": transports}

        # if transport type is ROAD EU
        elif t_type == "ROAD_EU":
            transports = m.Shipmentroadeu.objects.all()
            context = {"transports": transports}

        # if transport type is ROAD US
        elif t_type == "ROAD_US":
            transports = m.Shipmentroadus.objects.all()
            context = {"transports": transports}

        # getting domains
        domains_list = [x['domain_code'] for x in transports.values('domain_code').distinct()]
        # replacing names for domains
        domains_list = ['DAP' if x=="CL" else x for x in domains_list]
        domains_list = ['MATC' if x=='PHILIPSM1' else x for x in domains_list]
        # create dictionary for domains
        domains ={}
        # loop through dictionary
        for x in domains_list:
            # check naming and adjust in dictionary
            if x =='MATC':
                domains['MATC'] = 'PHILIPSM1'
            elif x =='SRC':
                domains['SRC'] ="SRC"
            elif x =='DAP':
                domains['DAP'] = 'CL'

        # if shipments are road
        if t_type == 'ROAD_EU' or t_type == 'ROAD_US':
            # getting sorted carriers
            carriers = [x['leg_1_carrier_name'] for x in transports.values('leg_1_carrier_name').distinct()]
            carriers = sorted(carriers)
        else:
            # getting sorted carriers
            carriers = [x['leg_2_carrier_name'] for x in transports.values('leg_2_carrier_name').distinct()]
            if None in carriers:
                carriers.remove(None)
            carriers = sorted(carriers)
        # getting sorted pick-up countries
        pick_country = [x['pickup_country'] for x in transports.values('pickup_country').distinct()]
        if None in pick_country:
            pick_country.remove(None)
        pick_country = sorted(pick_country)
        # getting sorted delivery countries
        del_country = [x['delivery_country'] for x in transports.values('delivery_country').distinct()]
        if None in del_country:
            del_country.remove(None)
        del_country = sorted(del_country)

        context = {'domains':domains,'carriers':carriers,'pickups':pick_country,'deliveries':del_country}
    # if method is POST
    if request.method == "POST":
        # getting lists of domains,carriers and countries
        domains = request.POST.getlist('domain')
        carriers = request.POST.getlist('carrier')
        pick_country = request.POST.getlist('pickup')
        del_country = request.POST.getlist('delivery')

        # if ALL in domains
        if 'ALL' in domains:
            # assign ALL to list
            domains = ['ALL']
            # and create opposite query
            query_domains = ~Q(domain_code__in=domains)
        else:
            # else - include selected domains
            query_domains = Q(domain_code__in=domains)
            # if all in list carriers and road type
        if 'ALL' in carriers and t_type  in ['ROAD_US','ROAD_EU']:
            # assign ALL to list
            carriers = ['ALL']
            # and create opposite query
            query_carriers = ~Q(leg_1_carrier_name__in=carriers)
        # if all in list carriers and not road
        elif "ALL" in carriers and t_type in ['FCL',"LCL",'AIR']:
            # assign all to list
            carriers = ['ALL']
            # and create oppposite query
            query_carriers = ~Q(leg_2_carrier_name__in=carriers)
            # if all not in list carriers and road
        elif "ALL" not in carriers and t_type in ['ROAD_US','ROAD_EU']:
            # query carriers in normal way
            query_carriers = Q(leg_1_carrier_name__in=carriers)
            # if all not in list carriers and not road
        elif "ALL" not in carriers and t_type in ['FCL',"LCL",'AIR']:
            # query carriers in normal way
            query_carriers = Q(leg_2_carrier_name__in=carriers)



        # if all in pickup countires
        if 'ALL' in pick_country:
            # assign all in pickup list
            pick_country = ['ALL']
            # and query opposite
            query_pick = ~Q(pickup_country__in=pick_country)
        else:
            # query pickup selected
            query_pick = Q(pickup_country__in=pick_country)
            # if all in delivery list
        if 'ALL' in del_country:
            # assign all in delivery list
            del_country = ['ALL']
            # and query opposite
            query_delivery = ~Q(delivery_country__in=del_country)
        else:
            # query delivery selected
            query_delivery = Q(delivery_country__in=del_country)
        # print(request.POST)
        # print('query_domain',query_domains,'query_carriers',query_carriers,
        #       'query_pickup',query_pick,'query_delivery',query_delivery)
        #
        # if (not domains) or (not carriers) or (not pick_country) or (not del_country):
        #     print('Wrong selection')
        # if domains:
        #     print('something is there')
        # else:
        #     print('empty')
        # print(request.POST['domain'])
        # print(len(request.POST['domain']))
        # if transport type is FCL
        if "FCL" in request.path:
            # get FCL transports based on queries
            transports = m.Shipmentfcl.objects.filter(query_domains&query_carriers&query_pick&query_delivery)
            context = {"transports": transports}

        # if transport type is LCL
        elif "LCL" in request.path:
            # filter shipments using queries and send to context
            transports = m.Shipmentlcl.objects.filter(query_domains&query_carriers&query_pick&query_delivery)
            context = {"transports": transports}

        # if transport type is AIR
        elif "AIR" in request.path:
            # filter shipments using queries and send to context
            transports = m.Shipmentair.objects.filter(query_domains&query_carriers&query_pick&query_delivery)
            context = {"transports": transports}

        # if transport type is ROAD EU
        elif "ROAD_EU" in request.path:
            # filter shipments using queries and send to context
            transports = m.Shipmentroadeu.objects.filter(query_domains&query_carriers&query_pick&query_delivery)
            context = {"transports": transports}

        # if transport type is ROAD US
        elif "ROAD_US" in request.path:
            # filter shipments using queries and send to context
            transports = m.Shipmentroadus.objects.filter(query_domains&query_carriers&query_pick&query_delivery)
            context = {"transports": transports}






        # prepare HTTP Response
        response = HttpResponse(content_type='text/csv')
        # set what will be the content of response
        response['Content-Disposition'] = f'attachment; filename="shipments.csv"'

        # create writer for csv
        writer = csv.writer(response)
        # idicate columns
        columns = ['infodis', 'shipment', 'booker_id', 'shipment_booker_name',
       'shipper_id', 'consignee_id', 'pickup_city', 'pickup_country',
       'port_of_loading', 'port_of_discharge', 'delivery_city',
       'delivery_country', 'del_terms', 'container_number', 'bill_of_lading',
       'pickup_zip_code', 'hawb', 'delivery_zip_code', 'booking_date',
       'leg_1_pickup_planned', 'leg_1_pickup_actual', 'leg_2_pickup_planned',
       'leg_2_pickup_actual', 'leg_3_delivery_actual', 'leg_1_carrier_name',
       'leg_2_carrier_name', 'leg_3_carrier_name', 'billable_indicator_leg_1',
       'billable_indicator_leg_2', 'billable_indicator_leg_3',
       'container_type', 'leg_1_transport_mode', 'leg_2_transport_mode',
       'leg_3_transport_mode', 'domain_code', 'total_costs_sales',
       'leg_1_total_costs_purchase', 'leg_2_total_costs_purchase',
       'leg_3_total_costs_purchase', 'pallets', 'weight', 'volume']

        # # write column headers in
        writer.writerow(columns)


        # create list of values for transports
        movements = transports.values_list(*columns)
        # loop over each offer and write new row with data
        for move in movements:
            writer.writerow(move)

        # generate response
        return response

    # render page
    return render(request,'manager/reporting.html',context)

def notes(request,mode,shipment):
    # getting current date
    cur_date = datetime.datetime.today()
    # check mode of transport
    if "FCL" in mode:
        #filter shipments
        transport = m.Shipmentfcl.objects.get(shipment=shipment)
        # if shipment has no comment
        if transport.comments == None:
            # create form with initial data
            form = f.FclForm(initial={'action_taken':'YES',
                                      'date_of_email':cur_date,
                                      "mail_sent":'YES',
                                      'pending_solved':'PENDING',
                                      'delay_in_answer':0})
        else:
            # if comments present - create form with data already in transport entry
            form = f.FclForm(instance=transport)
        # if method is POST
        if request.method == 'POST':
            # send POST to form
            form = f.FclForm(request.POST,instance=transport)
            # if form is valid
            if form.is_valid():
                # save form
                form.save()
                # redirect
                return redirect('shipments',t_type=mode)
            else:
                # print errors
                print(form.errors)
        # pass form to context and render page
        context = {'form':form}
        return render (request,'manager/shipment_check.html',context)
    # check mode of transport
    elif "LCL" in mode:
        # filter shipments
        transport = m.Shipmentlcl.objects.get(shipment = shipment)
        # if shipment has no comment
        if transport.comments == None:
            # create form with initial data
            form = f.LclForm(initial={'action_taken':'YES',
                                      'date_of_email':cur_date,
                                      "mail_sent":'YES',
                                      'pending_solved':'PENDING',
                                      'delay_in_answer':0})
        else:
            # if comments present - create form with data already in transport entry
            form = f.LclForm(instance=transport)
    # if method is POST
        if request.method == 'POST':
            # send POST to form
            form = f.LclForm(request.POST,instance=transport)
            # if form is valid
            if form.is_valid():
                # save form
                form.save()
                return redirect('shipments',t_type=mode)
            else:
                print(form.errors)
        # pass form to context and render page
        context = {'form':form}
        return render (request,'manager/shipment_check.html',context)
    # check mode of transport
    elif "AIR" in mode:
        transport = m.Shipmentair.objects.get(shipment = shipment)
        # if shipment has no comment
        if transport.comments == None:
            # create form with initial data
            form = f.AirForm(initial={'action_taken':'YES',
                                      'date_of_email':cur_date,
                                      "mail_sent":'YES',
                                      'pending_solved':'PENDING',
                                      'delay_in_answer':0})
        else:
            # if comments present - create form with data already in transport entry
            form = f.AirForm(instance=transport)
        # if method is POST
        if request.method == 'POST':
            # send POST to form
            form = f.AirForm(request.POST,instance=transport)
            # if form is valid
            if form.is_valid():
                # save form
                form.save()
                # redirect
                return redirect('shipments',t_type=mode)
            else:
                print(form.errors)
        # pass form to context and render page
        context = {'form':form}
        return render (request,'manager/shipment_check.html',context)
    # check mode of transport
    elif "ROAD_EU" in mode:
        #filter shipment
        transport = m.Shipmentroadeu.objects.get(shipment = shipment)
        # if shipment has no comment
        if transport.comments == None:
            # create form with initial data
            form = f.RoadEuForm(initial={'action_taken':'YES',
                                      'date_of_email':cur_date,
                                      "mail_sent":'YES',
                                      'pending_solved':'PENDING',
                                      'delay_in_answer':0})
        else:
            # if comments present - create form with data already in transport entry
            form = f.RoadEuForm(instance=transport)
        # if method is POST
        if request.method == 'POST':
            # send POST to form
            form = f.RoadEuForm(request.POST,instance=transport)
            # if form is valid
            if form.is_valid():
                # save form
                form.save()
                # redirect
                return redirect('shipments',t_type=mode)
            else:
                print(form.errors)
        # pass form to context and render page
        context = {'form':form}
        return render (request,'manager/shipment_check.html',context)
    # check mode of transport
    elif "ROAD_US" in mode:
        # filter shipment
        transport = m.Shipmentroadus.objects.get(shipment = shipment)
        # if shipment has no comment
        if transport.comments == None:
            # create form with initial data
            form = f.RoadUsForm(initial={'action_taken':'YES',
                                      'date_of_email':cur_date,
                                      "mail_sent":'YES',
                                      'pending_solved':'PENDING',
                                      'delay_in_answer':0})
        else:
        # if comments present - create form with data already in transport entry
            form = f.RoadUsForm(instance=transport)
        # if method is POST
        if request.method == 'POST':
            # send POST to form
            form = f.FclForm(request.POST,instance=transport)
            # if form is valid
            if form.is_valid():
                # save form
                form.save()
                # redirect
                return redirect('shipments',t_type=mode)
            else:
                print(form.errors)
        # pass form to context and render page
        context = {'form':form}
        return render (request,'manager/shipment_check.html',context)

    # render page
    return  render(request,'manager/shipment_check.html')


def load_data(request):
    # form = f.FileForm()
    # if request.method == "POST":
    #     form = f.FileForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,'File saved')
    #         return render(request, 'manager/load_data.html')
    #
    # context = {'form':form}

    # finding file
    file = m.ImportingFile.objects.first()
    # getting address for file
    source_file = settings.MEDIA_ROOT+"\\" + str(file.file)

    # ROAD US
    # opening file and creating dataframe
    df = pd.read_excel(source_file,sheet_name="US ROAD rates")
    # creating list of all shipments from current report
    new_report = df['Infodis'].to_list()

    # checking all database for infodis numbers
    all_shipments = [x.infodis for x in m.Shipmentroadus.objects.all()]
    # loopoing over all infodis numbers collected
    print(new_report)
    print('all',all_shipments)
    for infodis in all_shipments:
        # if number is not present in report
        if infodis not in new_report:
            print('dleting',infodis)
            # otherwise - find element in database and delete it
            move_to_delete = m.Shipmentroadus.objects.get(infodis=infodis)
            move_to_delete.delete()


    # present = 6680019 #- present with date
    # absent = 4483367 #- no longer present
    # newly = 8093174 #- newly created


    # looping over list
    for transport in new_report:
        # filtering for checking if the shipment already exists in the database
        # switch to transport in production
        shipment = m.Shipmentroadus.objects.filter(infodis=transport)
        # if shipment present
        if shipment:
            # getting shipment from queryset
            db_transport = shipment[0]
            # getting date of email
            email_date = db_transport.date_of_email
            # checking today date
            today = datetime.date.today()
            print('date email ',email_date)
            print('date today ',today)
            # if there is email sent
            if email_date is not None:
                # check difference between today and day of action
                day_dif = today-email_date
                day_dif = day_dif.days
                # assign difference and save in database
                db_transport.delay_in_answer = day_dif
                db_transport.save()
                print(type(day_dif))
                print('Difference in days is',day_dif)
        else:
            # checking necessary index
            # switch to transport in production
            indexing = df.index[df['Infodis'] == transport].values[0]
            print(indexing)
            # checking dates
            dates_check = [df.loc[indexing, 'Leg 1 Pickup Planned'],
                           df.loc[indexing, 'Leg 1 Pickup Actual'],
                           df.loc[indexing, 'Leg 2 Pickup Planned'],
                           df.loc[indexing, 'Leg 2 Pickup Actual'],
                           df.loc[indexing, 'Leg 3 Delivery Actual']]
            # creating list for using in entry
            d_data = []
            # looping over all dates
            for x in dates_check:
                # if date is na then assign NULL
                if pd.isna(x):
                    d_data.append(None)
                else:
                    # otherwise assign value of date
                    d_data.append(x.strftime('%Y-%m-%d'))
            print(d_data)
            new_transport = m.Shipmentroadus.objects.create(infodis=int(df.loc[indexing,'Infodis']),
               shipment=df.loc[indexing,'Shipment'],
               booker_id= df.loc[indexing,'Booker id'],
               shipment_booker_name=df.loc[indexing,'Shipment Booker Name'],
               shipper_id=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Shipper id']]][0],
               consignee_id=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Consignee id']]][0],
               pickup_city=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Pickup city']]][0],
               pickup_country=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Pickup country']]][0],
               port_of_loading=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Port of loading']]][0],
               port_of_discharge=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Port of discharge']]][0],
               delivery_city=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Delivery city']]][0],
               delivery_country=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Delivery country']]][0],
               del_terms=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Del terms']]][0],
               container_number=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Container number']]][0],
               bill_of_lading=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Bill of lading']]][0],
               pickup_zip_code=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Pickup ZIP code']]][0],
               hawb=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'HAWB']]][0],
               delivery_zip_code=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Delivery ZIP code']]][0],
               booking_date=df.loc[indexing,'Booking date'].strftime('%Y-%m-%d'),
               leg_1_pickup_planned=d_data[0],
               leg_1_pickup_actual=d_data[1],
               leg_2_pickup_planned=d_data[2],
               leg_2_pickup_actual=d_data[3],
               leg_3_delivery_actual=d_data[4],
               leg_1_carrier_name=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Leg 1 Carrier Name']]][0],
               leg_2_carrier_name=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Leg 2 Carrier Name']]][0],
               leg_3_carrier_name=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Leg 3 Carrier Name']]][0],
               billable_indicator_leg_1=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Billable Indicator Leg 1']]][0],
               billable_indicator_leg_2=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Billable Indicator Leg 2']]][0],
               billable_indicator_leg_3=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Billable Indicator Leg 3']]][0],
               container_type=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Container type']]][0],
               leg_1_transport_mode=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Leg 1 Transport Mode']]][0],
               leg_2_transport_mode=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Leg 2 Transport Mode']]][0],
               leg_3_transport_mode=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Leg 3 Transport Mode']]][0],
               domain_code=[None if pd.isna(x) else str(x) for x in [df.loc[indexing,'Domain Code']]][0],
               total_costs_sales=[0.00 if pd.isna(x) else float(x) for x in [df.loc[indexing,'Total costs Sales']]][0],
               leg_1_total_costs_purchase=[0.00 if pd.isna(x) else float(x) for x in [df.loc[indexing,'Leg 1, Total costs Purchase']]][0],
               leg_2_total_costs_purchase=[0.00 if pd.isna(x) else float(x) for x in [df.loc[indexing,'Leg 2, Total costs Purchase']]][0],
               leg_3_total_costs_purchase=[0.00 if pd.isna(x) else float(x) for x in [df.loc[indexing,'Leg 3, Total costs Purchase']]][0],
               pallets=[None if pd.isna(x) else int(x) for x in [df.loc[indexing,'Pallets']]][0],
               weight=[None if pd.isna(x) else float(x) for x in [df.loc[indexing,'Weight']]][0],
               volume=[None if pd.isna(x) else float(x) for x in [df.loc[indexing,'Volume']]][0]
                                                            )
            new_transport.save()


    # ROAD EU
        # opening file and creating dataframe
    df = pd.read_excel(source_file, sheet_name="EU ROAD rates")
    # creating list of all shipments from current report
    new_report = df['Infodis'].to_list()

    # checking all database for infodis numbers
    all_shipments = [x.infodis for x in m.Shipmentroadeu.objects.all()]
    # loopoing over all infodis numbers collected
    print(new_report)
    print('all', all_shipments)
    for infodis in all_shipments:
        # if number is not present in report
        if infodis not in new_report:
            print('dleting', infodis)
            # otherwise - find element in database and delete it
            move_to_delete = m.Shipmentroadeu.objects.get(infodis=infodis)
            move_to_delete.delete()

    # present = 6680019 #- present with date
    # absent = 4483367 #- no longer present
    # newly = 8093174 #- newly created


    # looping over list
    for transport in new_report:
        # filtering for checking if the shipment already exists in the database
        # switch to transport in production
        shipment = m.Shipmentroadeu.objects.filter(infodis=transport)
        # if shipment present
        if shipment:
            # getting shipment from queryset
            db_transport = shipment[0]
            # getting date of email
            email_date = db_transport.date_of_email
            # checking today date
            today = datetime.date.today()
            print('date email ', email_date)
            print('date today ', today)
            # if there is email sent
            if email_date is not None:
                # check difference between today and day of action
                day_dif = today - email_date
                day_dif = day_dif.days
                # assign difference and save in database
                db_transport.delay_in_answer = day_dif
                db_transport.save()
                print(type(day_dif))
                print('Difference in days is', day_dif)
        else:
            # checking necessary index
            # switch to transport in production
            indexing = df.index[df['Infodis'] == transport].values[0]
            print(indexing)
            # checking dates
            dates_check = [df.loc[indexing, 'Leg 1 Pickup Planned'],
                           df.loc[indexing, 'Leg 1 Pickup Actual'],
                           df.loc[indexing, 'Leg 2 Pickup Planned'],
                           df.loc[indexing, 'Leg 2 Pickup Actual'],
                           df.loc[indexing, 'Leg 3 Delivery Actual']]
            # creating list for using in entry
            d_data = []
            # looping over all dates
            for x in dates_check:
                # if date is na then assign NULL
                if pd.isna(x):
                    d_data.append(None)
                else:
                    # otherwise assign value of date
                    d_data.append(x.strftime('%Y-%m-%d'))
            print(d_data)
            new_transport = m.Shipmentroadeu.objects.create(infodis=int(df.loc[indexing, 'Infodis']),
                                                            shipment=df.loc[indexing, 'Shipment'],
                                                            booker_id=df.loc[indexing, 'Booker id'],
                                                            shipment_booker_name=df.loc[
                                                                indexing, 'Shipment Booker Name'],
                                                            shipper_id=[None if pd.isna(x) else str(x) for x in
                                                                        [df.loc[indexing, 'Shipper id']]][0],
                                                            consignee_id=[None if pd.isna(x) else str(x) for x in
                                                                          [df.loc[indexing, 'Consignee id']]][0],
                                                            pickup_city=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Pickup city']]][0],
                                                            pickup_country=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Pickup country']]][0],
                                                            port_of_loading=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Port of loading']]][0],
                                                            port_of_discharge=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Port of discharge']]][
                                                                0],
                                                            delivery_city=[None if pd.isna(x) else str(x) for x in
                                                                           [df.loc[indexing, 'Delivery city']]][0],
                                                            delivery_country=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Delivery country']]][
                                                                0],
                                                            del_terms=[None if pd.isna(x) else str(x) for x in
                                                                       [df.loc[indexing, 'Del terms']]][0],
                                                            container_number=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Container number']]][
                                                                0],
                                                            bill_of_lading=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Bill of lading']]][0],
                                                            pickup_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Pickup ZIP code']]][0],
                                                            hawb=[None if pd.isna(x) else str(x) for x in
                                                                  [df.loc[indexing, 'HAWB']]][0],
                                                            delivery_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Delivery ZIP code']]][
                                                                0],
                                                            booking_date=df.loc[indexing, 'Booking date'].strftime(
                                                                '%Y-%m-%d'),
                                                            leg_1_pickup_planned=d_data[0],
                                                            leg_1_pickup_actual=d_data[1],
                                                            leg_2_pickup_planned=d_data[2],
                                                            leg_2_pickup_actual=d_data[3],
                                                            leg_3_delivery_actual=d_data[4],
                                                            leg_1_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 1 Carrier Name']]][
                                                                0],
                                                            leg_2_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 2 Carrier Name']]][
                                                                0],
                                                            leg_3_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 3 Carrier Name']]][
                                                                0],
                                                            billable_indicator_leg_1=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 1']]][0],
                                                            billable_indicator_leg_2=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 2']]][0],
                                                            billable_indicator_leg_3=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 3']]][0],
                                                            container_type=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Container type']]][0],
                                                            leg_1_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 1 Transport Mode']]][0],
                                                            leg_2_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 2 Transport Mode']]][0],
                                                            leg_3_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 3 Transport Mode']]][0],
                                                            domain_code=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Domain Code']]][0],
                                                            total_costs_sales=[0.00 if pd.isna(x) else float(x) for x in
                                                                               [df.loc[indexing, 'Total costs Sales']]][
                                                                0],
                                                            leg_1_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 1, Total costs Purchase']]][0],
                                                            leg_2_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 2, Total costs Purchase']]][0],
                                                            leg_3_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 3, Total costs Purchase']]][0],
                                                            pallets=[None if pd.isna(x) else int(x) for x in
                                                                     [df.loc[indexing, 'Pallets']]][0],
                                                            weight=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Weight']]][0],
                                                            volume=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Volume']]][0]
                                                            )
            new_transport.save()


    #FCL
    # opening file and creating dataframe
    df = pd.read_excel(source_file, sheet_name="FCL rates")
    # creating list of all shipments from current report
    new_report = df['Infodis'].to_list()

    # checking all database for infodis numbers
    all_shipments = [x.infodis for x in m.Shipmentfcl.objects.all()]
    # loopoing over all infodis numbers collected
    print(new_report)
    print('all', all_shipments)
    for infodis in all_shipments:
        # if number is not present in report
        if infodis not in new_report:
            print('dleting', infodis)
            # otherwise - find element in database and delete it
            move_to_delete = m.Shipmentfcl.objects.get(infodis=infodis)
            move_to_delete.delete()

    # present = 6680019 #- present with date
    # absent = 4483367 #- no longer present
    # newly = 8093174 #- newly created

    # looping over list
    for transport in new_report:
        # filtering for checking if the shipment already exists in the database
        # switch to transport in production
        shipment = m.Shipmentfcl.objects.filter(infodis=transport)
        # if shipment present
        if shipment:
            # getting shipment from queryset
            db_transport = shipment[0]
            # getting date of email
            email_date = db_transport.date_of_email
            # checking today date
            today = datetime.date.today()
            print('date email ', email_date)
            print('date today ', today)
            # if there is email sent
            if email_date is not None:
                # check difference between today and day of action
                day_dif = today - email_date
                day_dif = day_dif.days
                # assign difference and save in database
                db_transport.delay_in_answer = day_dif
                db_transport.save()
                print(type(day_dif))
                print('Difference in days is', day_dif)
        else:
            # checking necessary index
            # switch to transport in production
            indexing = df.index[df['Infodis'] == transport].values[0]
            print(indexing)
            # checking dates
            dates_check = [df.loc[indexing, 'Leg 1 Pickup Planned'],
                           df.loc[indexing, 'Leg 1 Pickup Actual'],
                           df.loc[indexing, 'Leg 2 Pickup Planned'],
                           df.loc[indexing, 'Leg 2 Pickup Actual'],
                           df.loc[indexing, 'Leg 3 Delivery Actual']]
            # creating list for using in entry
            d_data = []
            # looping over all dates
            for x in dates_check:
                # if date is na then assign NULL
                if pd.isna(x):
                    d_data.append(None)
                else:
                    # otherwise assign value of date
                    d_data.append(x.strftime('%Y-%m-%d'))
            print(d_data)
            new_transport = m.Shipmentfcl.objects.create(infodis=int(df.loc[indexing, 'Infodis']),
                                                            shipment=df.loc[indexing, 'Shipment'],
                                                            booker_id=df.loc[indexing, 'Booker id'],
                                                            shipment_booker_name=df.loc[
                                                                indexing, 'Shipment Booker Name'],
                                                            shipper_id=[None if pd.isna(x) else str(x) for x in
                                                                        [df.loc[indexing, 'Shipper id']]][0],
                                                            consignee_id=[None if pd.isna(x) else str(x) for x in
                                                                          [df.loc[indexing, 'Consignee id']]][0],
                                                            pickup_city=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Pickup city']]][0],
                                                            pickup_country=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Pickup country']]][0],
                                                            port_of_loading=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Port of loading']]][0],
                                                            port_of_discharge=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Port of discharge']]][
                                                                0],
                                                            delivery_city=[None if pd.isna(x) else str(x) for x in
                                                                           [df.loc[indexing, 'Delivery city']]][0],
                                                            delivery_country=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Delivery country']]][
                                                                0],
                                                            del_terms=[None if pd.isna(x) else str(x) for x in
                                                                       [df.loc[indexing, 'Del terms']]][0],
                                                            container_number=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Container number']]][
                                                                0],
                                                            bill_of_lading=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Bill of lading']]][0],
                                                            pickup_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Pickup ZIP code']]][0],
                                                            hawb=[None if pd.isna(x) else str(x) for x in
                                                                  [df.loc[indexing, 'HAWB']]][0],
                                                            delivery_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Delivery ZIP code']]][
                                                                0],
                                                            booking_date=df.loc[indexing, 'Booking date'].strftime(
                                                                '%Y-%m-%d'),
                                                            leg_1_pickup_planned=d_data[0],
                                                            leg_1_pickup_actual=d_data[1],
                                                            leg_2_pickup_planned=d_data[2],
                                                            leg_2_pickup_actual=d_data[3],
                                                            leg_3_delivery_actual=d_data[4],
                                                            leg_1_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 1 Carrier Name']]][
                                                                0],
                                                            leg_2_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 2 Carrier Name']]][
                                                                0],
                                                            leg_3_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 3 Carrier Name']]][
                                                                0],
                                                            billable_indicator_leg_1=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 1']]][0],
                                                            billable_indicator_leg_2=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 2']]][0],
                                                            billable_indicator_leg_3=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 3']]][0],
                                                            container_type=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Container type']]][0],
                                                            leg_1_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 1 Transport Mode']]][0],
                                                            leg_2_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 2 Transport Mode']]][0],
                                                            leg_3_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 3 Transport Mode']]][0],
                                                            domain_code=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Domain Code']]][0],
                                                            total_costs_sales=[0.00 if pd.isna(x) else float(x) for x in
                                                                               [df.loc[indexing, 'Total costs Sales']]][
                                                                0],
                                                            leg_1_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 1, Total costs Purchase']]][0],
                                                            leg_2_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 2, Total costs Purchase']]][0],
                                                            leg_3_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 3, Total costs Purchase']]][0],
                                                            pallets=[None if pd.isna(x) else int(x) for x in
                                                                     [df.loc[indexing, 'Pallets']]][0],
                                                            weight=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Weight']]][0],
                                                            volume=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Volume']]][0]
                                                            )
            new_transport.save()

        # LCL
        # opening file and creating dataframe
    df = pd.read_excel(source_file, sheet_name="LCL rates")
    # creating list of all shipments from current report
    new_report = df['Infodis'].to_list()

    # checking all database for infodis numbers
    all_shipments = [x.infodis for x in m.Shipmentlcl.objects.all()]
    # loopoing over all infodis numbers collected
    print(new_report)
    print('all', all_shipments)
    for infodis in all_shipments:
        # if number is not present in report
        if infodis not in new_report:
            print('dleting', infodis)
            # otherwise - find element in database and delete it
            move_to_delete = m.Shipmentlcl.objects.get(infodis=infodis)
            move_to_delete.delete()

    # present = 6680019 #- present with date
    # absent = 4483367 #- no longer present
    # newly = 8093174 #- newly created

    # looping over list
    for transport in new_report:
        # filtering for checking if the shipment already exists in the database
        # switch to transport in production
        shipment = m.Shipmentlcl.objects.filter(infodis=transport)
        # if shipment present
        if shipment:
            # getting shipment from queryset
            db_transport = shipment[0]
            # getting date of email
            email_date = db_transport.date_of_email
            # checking today date
            today = datetime.date.today()
            print('date email ', email_date)
            print('date today ', today)
            # if there is email sent
            if email_date is not None:
                # check difference between today and day of action
                day_dif = today - email_date
                day_dif = day_dif.days
                # assign difference and save in database
                db_transport.delay_in_answer = day_dif
                db_transport.save()
                print(type(day_dif))
                print('Difference in days is', day_dif)
        else:
            # checking necessary index
            # switch to transport in production
            indexing = df.index[df['Infodis'] == transport].values[0]
            print(indexing)
            # checking dates
            dates_check = [df.loc[indexing, 'Leg 1 Pickup Planned'],
                           df.loc[indexing, 'Leg 1 Pickup Actual'],
                           df.loc[indexing, 'Leg 2 Pickup Planned'],
                           df.loc[indexing, 'Leg 2 Pickup Actual'],
                           df.loc[indexing, 'Leg 3 Delivery Actual']]
            # creating list for using in entry
            d_data = []
            # looping over all dates
            for x in dates_check:
                # if date is na then assign NULL
                if pd.isna(x):
                    d_data.append(None)
                else:
                    # otherwise assign value of date
                    d_data.append(x.strftime('%Y-%m-%d'))
            print(d_data)
            new_transport = m.Shipmentlcl.objects.create(infodis=int(df.loc[indexing, 'Infodis']),
                                                            shipment=df.loc[indexing, 'Shipment'],
                                                            booker_id=df.loc[indexing, 'Booker id'],
                                                            shipment_booker_name=df.loc[
                                                                indexing, 'Shipment Booker Name'],
                                                            shipper_id=[None if pd.isna(x) else str(x) for x in
                                                                        [df.loc[indexing, 'Shipper id']]][0],
                                                            consignee_id=[None if pd.isna(x) else str(x) for x in
                                                                          [df.loc[indexing, 'Consignee id']]][0],
                                                            pickup_city=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Pickup city']]][0],
                                                            pickup_country=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Pickup country']]][0],
                                                            port_of_loading=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Port of loading']]][0],
                                                            port_of_discharge=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Port of discharge']]][
                                                                0],
                                                            delivery_city=[None if pd.isna(x) else str(x) for x in
                                                                           [df.loc[indexing, 'Delivery city']]][0],
                                                            delivery_country=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Delivery country']]][
                                                                0],
                                                            del_terms=[None if pd.isna(x) else str(x) for x in
                                                                       [df.loc[indexing, 'Del terms']]][0],
                                                            container_number=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Container number']]][
                                                                0],
                                                            bill_of_lading=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Bill of lading']]][0],
                                                            pickup_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Pickup ZIP code']]][0],
                                                            hawb=[None if pd.isna(x) else str(x) for x in
                                                                  [df.loc[indexing, 'HAWB']]][0],
                                                            delivery_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Delivery ZIP code']]][
                                                                0],
                                                            booking_date=df.loc[indexing, 'Booking date'].strftime(
                                                                '%Y-%m-%d'),
                                                            leg_1_pickup_planned=d_data[0],
                                                            leg_1_pickup_actual=d_data[1],
                                                            leg_2_pickup_planned=d_data[2],
                                                            leg_2_pickup_actual=d_data[3],
                                                            leg_3_delivery_actual=d_data[4],
                                                            leg_1_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 1 Carrier Name']]][
                                                                0],
                                                            leg_2_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 2 Carrier Name']]][
                                                                0],
                                                            leg_3_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 3 Carrier Name']]][
                                                                0],
                                                            billable_indicator_leg_1=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 1']]][0],
                                                            billable_indicator_leg_2=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 2']]][0],
                                                            billable_indicator_leg_3=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 3']]][0],
                                                            container_type=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Container type']]][0],
                                                            leg_1_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 1 Transport Mode']]][0],
                                                            leg_2_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 2 Transport Mode']]][0],
                                                            leg_3_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 3 Transport Mode']]][0],
                                                            domain_code=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Domain Code']]][0],
                                                            total_costs_sales=[0.00 if pd.isna(x) else float(x) for x in
                                                                               [df.loc[indexing, 'Total costs Sales']]][
                                                                0],
                                                            leg_1_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 1, Total costs Purchase']]][0],
                                                            leg_2_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 2, Total costs Purchase']]][0],
                                                            leg_3_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 3, Total costs Purchase']]][0],
                                                            pallets=[None if pd.isna(x) else int(x) for x in
                                                                     [df.loc[indexing, 'Pallets']]][0],
                                                            weight=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Weight']]][0],
                                                            volume=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Volume']]][0]
                                                            )
            new_transport.save()

        # AIR
        # opening file and creating dataframe
    df = pd.read_excel(source_file, sheet_name="US ROAD rates")
    # creating list of all shipments from current report
    new_report = df['Infodis'].to_list()

    # checking all database for infodis numbers
    all_shipments = [x.infodis for x in m.Shipmentair.objects.all()]
    # loopoing over all infodis numbers collected
    print(new_report)
    print('all', all_shipments)
    for infodis in all_shipments:
        # if number is not present in report
        if infodis not in new_report:
            print('dleting', infodis)
            # otherwise - find element in database and delete it
            move_to_delete = m.Shipmentair.objects.get(infodis=infodis)
            move_to_delete.delete()

    # present = 6680019 #- present with date
    # absent = 4483367 #- no longer present
    # newly = 8093174 #- newly created

    # looping over list
    for transport in new_report:
        # filtering for checking if the shipment already exists in the database
        # switch to transport in production
        shipment = m.Shipmentair.objects.filter(infodis=transport)
        # if shipment present
        if shipment:
            # getting shipment from queryset
            db_transport = shipment[0]
            # getting date of email
            email_date = db_transport.date_of_email
            # checking today date
            today = datetime.date.today()
            print('date email ', email_date)
            print('date today ', today)
            # if there is email sent
            if email_date is not None:
                # check difference between today and day of action
                day_dif = today - email_date
                day_dif = day_dif.days
                # assign difference and save in database
                db_transport.delay_in_answer = day_dif
                db_transport.save()
                print(type(day_dif))
                print('Difference in days is', day_dif)
        else:
            # checking necessary index
            # switch to transport in production
            indexing = df.index[df['Infodis'] == transport].values[0]
            print(indexing)
            # checking dates
            dates_check = [df.loc[indexing, 'Leg 1 Pickup Planned'],
                           df.loc[indexing, 'Leg 1 Pickup Actual'],
                           df.loc[indexing, 'Leg 2 Pickup Planned'],
                           df.loc[indexing, 'Leg 2 Pickup Actual'],
                           df.loc[indexing, 'Leg 3 Delivery Actual']]
            # creating list for using in entry
            d_data = []
            # looping over all dates
            for x in dates_check:
                # if date is na then assign NULL
                if pd.isna(x):
                    d_data.append(None)
                else:
                    # otherwise assign value of date
                    d_data.append(x.strftime('%Y-%m-%d'))
            print(d_data)
            new_transport = m.Shipmentair.objects.create(infodis=int(df.loc[indexing, 'Infodis']),
                                                            shipment=df.loc[indexing, 'Shipment'],
                                                            booker_id=df.loc[indexing, 'Booker id'],
                                                            shipment_booker_name=df.loc[
                                                                indexing, 'Shipment Booker Name'],
                                                            shipper_id=[None if pd.isna(x) else str(x) for x in
                                                                        [df.loc[indexing, 'Shipper id']]][0],
                                                            consignee_id=[None if pd.isna(x) else str(x) for x in
                                                                          [df.loc[indexing, 'Consignee id']]][0],
                                                            pickup_city=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Pickup city']]][0],
                                                            pickup_country=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Pickup country']]][0],
                                                            port_of_loading=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Port of loading']]][0],
                                                            port_of_discharge=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Port of discharge']]][
                                                                0],
                                                            delivery_city=[None if pd.isna(x) else str(x) for x in
                                                                           [df.loc[indexing, 'Delivery city']]][0],
                                                            delivery_country=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Delivery country']]][
                                                                0],
                                                            del_terms=[None if pd.isna(x) else str(x) for x in
                                                                       [df.loc[indexing, 'Del terms']]][0],
                                                            container_number=[None if pd.isna(x) else str(x) for x in
                                                                              [df.loc[indexing, 'Container number']]][
                                                                0],
                                                            bill_of_lading=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Bill of lading']]][0],
                                                            pickup_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                             [df.loc[indexing, 'Pickup ZIP code']]][0],
                                                            hawb=[None if pd.isna(x) else str(x) for x in
                                                                  [df.loc[indexing, 'HAWB']]][0],
                                                            delivery_zip_code=[None if pd.isna(x) else str(x) for x in
                                                                               [df.loc[indexing, 'Delivery ZIP code']]][
                                                                0],
                                                            booking_date=df.loc[indexing, 'Booking date'].strftime(
                                                                '%Y-%m-%d'),
                                                            leg_1_pickup_planned=d_data[0],
                                                            leg_1_pickup_actual=d_data[1],
                                                            leg_2_pickup_planned=d_data[2],
                                                            leg_2_pickup_actual=d_data[3],
                                                            leg_3_delivery_actual=d_data[4],
                                                            leg_1_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 1 Carrier Name']]][
                                                                0],
                                                            leg_2_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 2 Carrier Name']]][
                                                                0],
                                                            leg_3_carrier_name=[None if pd.isna(x) else str(x) for x in
                                                                                [df.loc[
                                                                                     indexing, 'Leg 3 Carrier Name']]][
                                                                0],
                                                            billable_indicator_leg_1=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 1']]][0],
                                                            billable_indicator_leg_2=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 2']]][0],
                                                            billable_indicator_leg_3=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Billable Indicator Leg 3']]][0],
                                                            container_type=[None if pd.isna(x) else str(x) for x in
                                                                            [df.loc[indexing, 'Container type']]][0],
                                                            leg_1_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 1 Transport Mode']]][0],
                                                            leg_2_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 2 Transport Mode']]][0],
                                                            leg_3_transport_mode=
                                                            [None if pd.isna(x) else str(x) for x in
                                                             [df.loc[indexing, 'Leg 3 Transport Mode']]][0],
                                                            domain_code=[None if pd.isna(x) else str(x) for x in
                                                                         [df.loc[indexing, 'Domain Code']]][0],
                                                            total_costs_sales=[0.00 if pd.isna(x) else float(x) for x in
                                                                               [df.loc[indexing, 'Total costs Sales']]][
                                                                0],
                                                            leg_1_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 1, Total costs Purchase']]][0],
                                                            leg_2_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 2, Total costs Purchase']]][0],
                                                            leg_3_total_costs_purchase=
                                                            [0.00 if pd.isna(x) else float(x) for x in
                                                             [df.loc[indexing, 'Leg 3, Total costs Purchase']]][0],
                                                            pallets=[None if pd.isna(x) else int(x) for x in
                                                                     [df.loc[indexing, 'Pallets']]][0],
                                                            weight=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Weight']]][0],
                                                            volume=[None if pd.isna(x) else float(x) for x in
                                                                    [df.loc[indexing, 'Volume']]][0]
                                                            )
            new_transport.save()


    del df
    return render(request,'manager/load_data.html')