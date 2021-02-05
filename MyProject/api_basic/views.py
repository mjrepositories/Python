from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# imports for authentications
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes

# Create your views here.


# second method of getting all article would be adding decorator to the function by using import:
# from rest_framework.decorators import api_view
#  and then to adding decorator to function 
# @api_view(['GET'])
# Whic would mean that for specific view we are only accepting GET method
# But in this tutorial we are keeping up with checking the method


@api_view(['GET','POST'])
# we meed to add two decorators for checking is user is authenticated
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def article_list(request):
    # we need to put in content details regarding user that is logged in
    #  if nothing is passed here so data will be treated as None
    # then we can assume that no one is logged in and API will come back to us
    # with information that no credentials were passed so no get/post/any other method can be done
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }

    # if method is GET
    if request.method == 'GET':
        # We create a queryset with all instances of our model
        articles = Article.objects.all()
        #  having queryset we are making many as True
        serializer = ArticleSerializer(articles,many=True)

        # having serializer set - we are able to return the Json response by passing serializer data to import object, and setting safe to False
        
        #  and we put content so data regarding user to context of response which will, using help of decorators, enable us to prevent action with having user logged in
        return Response(serializer.data,content)
    
    #  if we have method POST
    elif request.method == "POST":

        # we are putting data into serializer (as we have decorator on - request.data is providing JSON object)
        serializer = ArticleSerializer(data = request.data)
        # now we have to check if our serializer is ok (so if the data was processed correctly in our API call)
        if serializer.is_valid():
            # We are saving our serializer into database/model
            serializer.save()
            # Once saved - we are returning a JSon response with serialized data and status 201 which indicates that process went smoothly and we have our data saved
            return Response(serializer.data,status=201)
        # if not valid
        else:
            #  we are returning serializers errros with status 400
            return JsonResponse(serializer.data,status=400)



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


@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
# we are quering model to get object with pk
    try:
        article = Article.objects.get(pk=pk)
    except:
        return HttpResponse('No element with pk={}'.format(pk))
    #  if method is GET
    if request.method == 'GET':
        # we are serializing the data for article we queried
        serializer = ArticleSerializer(article)
        # and we are returning this article
        return Response(serializer.data)

    # if method is PUT so for updating
    elif request.method == 'PUT':
        # we are making a serializer based on request.data but we also put an instance of an article to be update in serializer
        serializer = ArticleSerializer(article,data = request.data)
        # if serializer is valid
        if serializer.is_valid():
            # we are able to save it
            serializer.save()
            # and return a response
            return Response(serializer.data)

    #  if method is delete
    elif request.method == 'DELETE':
        # we just remove the object
        article.delete()
        # and return a response with info that item was deleted
        return Response('Item deleted!')