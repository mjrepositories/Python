# As for api - we have to create serializers files so that our data will be turned into JSON or pulled from JSON
from rest_framework import serializers

from .models import Article

# Below is for standard serializer class

# We put fields that we want to serialize (so turn int JSON)
# That is different from model serializer as we have to put all the data on our own 
# Where in model serializer - django rest framework is doing it itself

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    #  Here we create a serializer by returning the created object with validated data
    def create(self,validated_data):
        return Article.objects.create(validated_data)

    #  Here we update our instance with the data passed
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.author = validated_data.get('author',instance.author)
        instance.email = validated_data.get('email',instance.email)
        instance.date = validated_data.get('date',instance.date)
        instance.save()
        return instance

'''So in general serializer works this way:

1. Two objects are imported which are:

a) from rest_framework.renderers import JSONRenderer
b) from rest_framework.parsers import JSONParser 

2. Once we have it - django uses serializers that we created  to turn data to python native data format

To be fair - looks like a dictionary
(serializer.data passed)
{'title': 'Second article', 'author': 'Edwin', 'email': 'edwin.wiewora@gmail.com', 'date': '2021-01-23T20:44:23.702865Z'}

3. Then Django uses JSONrenderer object to turn our dictionary to JSON format

And in the end it looks like this

b'{"title":"Second article","author":"Edwin","email":"edwin.wiewora@gmail.com","date":"2021-01-23T20:44:23.702865Z"}'

4. We can also get queryset serialized by adding many as parameter and setting it up as true)


'''

# Now let's go to ModelSerializer

class ArticleSerializer(serializers.ModelSerializer):
    #  In ModelSerializer we declare class Meta and there we have to put model we want to serialize and fields that we want to process
    class Meta:
        model = Article
        fields = ['id','title','author']