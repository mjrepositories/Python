from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

# # In normal view we would declare render to get the page with context passed
# # But in case of API we just want to get JSON data as response
# def test_view(request):
#     data ={
#         'name':'John',
#         'age':23
#     }

#     # If i would like to pass the data like list - i should put safe = False which enables me to do that
#     return JsonResponse(data)


class TestView(APIView):
# In a class view we have to type permission_classes in order to be able to authenticate user
    permission_classes = (IsAuthenticated,)
    
    def get(self,request,*args,**kwargs):
        qs = Post.objects.all()
        # When we are working with many instances of a model, so a queryset, to serializer we have to pass our queryset but also made many to True as this is how multiple elements are processed
        serializer = PostSerializer(qs,many=True)
        return Response(serializer.data)


    def post(self,request,*args, **kwargs):
        # when we create a serializer we have to declare request.data there as a representation of date sent via API
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # if everything went smoothly - we can show the response with serialized data
            return Response(serializer.data)
        return Response(serializer.errors)