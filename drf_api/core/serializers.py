from rest_framework import serializers
from .models import Post

# in case of serializers - the easiest way would be to inherit from serializers.ModelSerializer
# then pass Meta class, model that we want to serialize and fields that we want to user
class PostSerializer(serializers.ModelSerializer):
    # Serializer ensures transformation from Django Model to JSON format
    class Meta:
        model = Post
        fields = ['title','description']