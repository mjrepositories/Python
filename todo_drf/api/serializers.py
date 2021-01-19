# serializing allows us to return any model object in JSON response

# we need to specify in this file the model which want to serialize

# once it is created here we are able to use it in views

# we need to import serializers from django rest framework
from rest_framework import serializers

# now we have to import our models
from .models import Task

# below class is going to serialize an object
# creation looks a little bit like in forms.py
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

