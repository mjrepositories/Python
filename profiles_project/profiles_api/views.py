from django.shortcuts import render

# importing APIView class
from rest_framework.views import APIView
# importing response for returning responses from API views
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

from profiles_api import models

# importing authentication for API
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

# importing filtering option in rest
from rest_framework import filters

# import for getting the token (generating)
from rest_framework.authtoken.views import ObtainAuthToken

# setting for api
from rest_framework.settings import api_settings

# this will make readonly if user is not authenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

# Create your views here.

# serializer allows data input to Python format

class HelloApiView(APIView):                
    # telling our class what is our serializer
    serializer_class = serializers.HelloSerializer  


    # testing api view
    def get(self,request,format=None):
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to traditional Django view',
            'Gives control over application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'hello','an_apiview':an_apiview
        
        
        
        
        })

    def post(self,request):
        # data is passed along in request
        serializer = self.serializer_class(data=request.data)
        # we are checking if serializer is valid
        if serializer.is_valid():
        # we are retrieving data
            name = serializer.validated_data.get('name')
            message = f'Checking if we will have name {name} here'

            # returning response
            return Response({'message':message})
        else:
            # otherwise - we will return error . default response gives 200 so we change it
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        # updating an object
        return Response({"method":"PUT"})

    def patch(self,request,pk=None):
        # partial update (only those that were provided in a request)
        return Response({"method":"PATCH"})
    
    def delete(self,request,pk=None):
        # deleting an object in a database
        return Response({"method":"DELETE"})



class HelloViewSet(viewsets.ViewSet):
    # declaring serializer
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        # "returning a hello message"
        a_viewset = [
            'uses actions (list,create,retrieve, update)',
            'automatically maps  to URLs using routers',
            'Provides more fucntionalites with less code'
        ]
        return Response({'message':'checking list function','a_viewset':a_viewset})
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
  # validating serializer
        if serializer.is_valid():
   
            name = serializer.validated_data.get('name')
            message = f'Hi {name}'
            return Response({"message":message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    
    def retrieve(self,request,pk=None):
        # handling getting object by id
        return Response({'http-method':"GET"})

    def update(self,request,pk=None):
        # handle updating an object
        return Response({'http-method':'PUT'})

    def partial_update(self,reqest,pk=None):
        # handling partial update
        return Response({'http-method':'PATCH'})

    def destroy(self,request,pk=None):
        # handles removing the object
        return Response({'http-method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    # handle creating and updating viewsets
    serializer_class = serializers.UserProfileSerializer
    # quering our dataset
    queryset = models.UserProfile.objects.all()
    # preparing authentication / the mechanism we use
    authentication_classes = (TokenAuthentication,)
    # setting up permissions (special options that user can use)
    permission_classes = (permissions.UpdateOwnProfile,)
    # enabling filtering
    filter_backends = (filters.SearchFilter,)
    # indicating which field we want to filter
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    # handling creating user authentication tokens
    # we are adjusting that to be able to see it in a browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


    # arranging feed view
    class UserProfileFeedViewSet(viewsets.ModelViewSet):
        # in general it will handle requests for feed 

        # adding authentication
        authentication_classes = (TokenAuthentication,)
        serializer_class = serializers.ProfileFeedItemSerializer
        permission_classes = (
            # setting so that user will be able to update their own status and see (read only) other users statuses
            permissions.UpdateOwnStatus,
            # IsAuthenticatedOrReadOnly
            # below is only for authenticated users
            IsAuthenticated
        )

        # we will manage all objects we have in our db
        queryset =  models.ProfileFeedItem.objects.all()

        def perform_create(self,serializer):
            # setting so that logged user can modify it's data
            serializer.save(user_profile=self.request.user)