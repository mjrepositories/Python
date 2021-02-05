from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

# below is enabling us to get full database information for all objects for specific model
@api_view(['GET'])
def taskList(request):
    # quering the model to get all objects + order by id descending
    tasks = Task.objects.all().order_by('-id')
    # serializing the data to get many tasks
    serializer = TaskSerializer(tasks,many=True)
    # return a resepone with serialized data
    return Response(serializer.data)

# below is enabling us to get details of specific object of a model
@api_view(['GET'])
def taskDetail(request,pk):
    # quering for specific object with indicated primary key
    tasks = Task.objects.get(id=pk)
    # serializing data to get only adjust only one object for response (thus - many is set for False)
    serializer = TaskSerializer(tasks,many=False)
    # returning a response wtih serialized data
    return Response(serializer.data)

# below is enabling us to create model object
@api_view(['POST'])
def taskCreate(request):
    # we are passing data to serializer here request.data is similar to request.POST
    serializer = TaskSerializer(data=request.data)
    # if data entered in serializer is valid
    if serializer.is_valid():
        # we are saving it
        serializer.save()
    # returning a response with serialized data
    return Response(serializer.data)

# below is enabling us to update object
@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    # we are passing instance to serializer
    serializer = TaskSerializer(instance=task, data=request.data)
    # if data entered in serializer is valid
    if serializer.is_valid():
        # we are saving it
        serializer.save()
    # returning a response with serialized data
    return Response(serializer.data)

# below is enabling us to update object
@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    # returning a response with serialized data
    return Response('Item successfully deleted')