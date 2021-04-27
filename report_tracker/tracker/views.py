from django.shortcuts import render

# Create your views here.

# allows us to return status of the response
from rest_framework import status

# allowing us to return of the request Response
from rest_framework.response import Response

# allowing us to return JSON response
from django.http import JsonResponse

# allows us to have the api view in function based view of the api
from rest_framework.decorators import api_view

# importing model
from .models import Status,ReportingPeriod,Report,Period

# importing serializer
from .serializers import StatusSerializer

# importing Q for combining queries
from django.db.models import Q


# imports to check if we have statuses for current period
import json
import datetime
import calendar

from collections import Counter


# enabling only GET
@api_view(['GET'])
# view to see url end points to see what API is handling
def apiOverview(request):
    api_urls = {
        'List of statuses':'/all-statuses-view/',
        'Detail View of Status':'/status-detail/<str:pk>/',
        'Update View for Status':'/status-update/<str:pk>/',

    }
    return Response(api_urls)


# putting a decorator is telling us what type of requests are allowed for declared view
@api_view(['GET'])
def api_all_status_view(request):
# using try except block to catch errors
    try:
            # getting current month and year and concatenating it
        month_name = calendar.month_name[datetime.datetime.today().month]
        year_value = datetime.datetime.today().year
        current_period = f'{month_name} {year_value}'

        # checking if statuses for current period exist
        status = Status.objects.filter(Q(reporting_period__month=month_name)&Q(reporting_period__year=year_value))

        # previously we were pulling the whole dataset
        # status = Status.objects.all()
        # if there are no statuses then we are return response
    except Status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # we are serializing our data
    serializer = StatusSerializer(status,many=True)
    print(serializer)

    # we are returning the data from our serializer
    return Response(serializer.data)


#view for retrieving reporting days in specific month
@api_view(['GET'])
def api_get_periods(request):
    # getting current month and year
    month_name = calendar.month_name[datetime.datetime.today().month]
    year_value = datetime.datetime.today().year
    current_periods = Period.objects.filter((Q(month=month_name)&Q(year=year_value)))
    period_dict = {'':''}
    for x in current_periods:
        period_dict[str(x)]=x.id

    return Response(period_dict)
   
# allowing to see details of one status
@api_view(['GET'])
def api_single_status_view(request,pk):
    # we are getting the status based on id passed
    status = Status.objects.get(id=pk)

    # we are serializing the data so transforming to readable format
    serializer = StatusSerializer(status)
    

    # we are returing the response with current data for the status
    return Response(serializer.data)

# enabling POST method by using a decorator
@api_view(["POST"])
def api_status_update(request,pk):
    # we are getting the status based on id passed
    status = Status.objects.get(id=pk)
  # passing an instance to serializer
    # for "data" we are using the data that we put in a request
    serializer = StatusSerializer(instance=status,data = request.data)
    print("___________serializer")
    print(serializer)
    print("___________status")
    print(status)
    print("___________request")
    print(request)
    print("___________request.data")
    print(request.data)
    # if serializer is valid
    if serializer.is_valid():
        # we are ready to save the data we used to update the status of the report
        serializer.save()

    # we are returing the response with current data for the status
    return Response(serializer.data)


# allowing to only see data
@api_view(['GET'])
def api_status_check(request):


    # getting current month and year and concatenating it
    month_name = calendar.month_name[datetime.datetime.today().month]
    year_value = datetime.datetime.today().year
    current_period = f'{month_name} {year_value}'

    # checking if statuses for current period exist
    statuses = Status.objects.filter(Q(reporting_period__month=month_name)&Q(reporting_period__year=year_value))

    st_exist = len(statuses)
    if st_exist>0:
        return Response({"message": "Current period is already prepared for reporting statuses"})
    else:
        cur_report_period = ReportingPeriod.objects.get(Q(month=month_name)&Q(year=year_value))

        reports = Report.objects.all()
        # looping over all group matches
        for x in reports:
            # creating initial data
            data = {
                'report' : x,
                'reporting_period' :cur_report_period,
                'executed' : None ,
                'executed_on' : None,
                'on_time' : None,
                'issues' : None,
                'issues_description' : None
                }
            # creating instance with initial data
            status_to_create = Status(**data)
            # saving created bet
            status_to_create.save()

        return Response({"message":f"Reporting statuses have been prepared for period {current_period}"})
    


# View for getting data to visualize it
@api_view(['GET'])
def data_for_graphs(request):

        # using try except block to catch errors
    try:
            # getting current month and year and concatenating it
        month_name = calendar.month_name[datetime.datetime.today().month]
        year_value = datetime.datetime.today().year
        current_period = f'{month_name} {year_value}'

        # checking if statuses for current period exist
        status = Status.objects.filter(Q(reporting_period__month=month_name)&Q(reporting_period__year=year_value))

        # if there are no statuses then we are return response
    except Status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # checking how many reports we have
    how_many = len(status)

    executed = 0
    on_time = 0
    issues = 0
    days = []
    # loop for gathering data
    for report in status:
        days.append(report.report.deadline)
        if report.executed == "YES":
            executed +=1
            if report.on_time == "YES":
                on_time += 1
            if report.issues == ' YES':
                issues += 1 
    print(days)
    missing = how_many - executed
    # creating counter for days when reports are executed        
    days_dict = Counter(days)

    # overwritting dict to have it sorted
    days_dict = {k:v for k,v in sorted(days_dict.items(),key=lambda day:int(day[0][-2:].strip()))}

    target = 0.95
    delivery_rate = on_time/executed
    no_issues = executed - issues


    # checking results over time
    # creating list of months
    months =  [calendar.month_name[i] for i in range(1,13)]
    # finding the index of current month to slice the list
    current_index = months.index(month_name)
    # slicing the list
    months = months[0:current_index]

    year_results = {}

    for mth in months:
        status = Status.objects.filter(Q(reporting_period__month=mth)&Q(reporting_period__year=year_value))
        # checking how many reports we have
        how_many = len(status)
        on_time = 0

        # loop for gathering data
        for report in status:
            # if report was on time - add to list
                if report.on_time == "YES":
                    on_time += 1
        # calculate delivery rate
        delivery_rate = on_time/how_many
        # add to dictionary
        year_results[mth] = delivery_rate
    # add current month to dictionary
    year_results[month_name] = delivery_rate

    return Response(
        {
                'delivery_rate':delivery_rate,
                "days_overview":days_dict,
                'executed':executed,
                "missing":missing,
                "target":target,
                'issues':issues,
                'no_issues':no_issues,
                'month':month_name,
                'year':year_value,
                'year_results':year_results
                
        }
    )