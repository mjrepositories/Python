from rest_framework import serializers

from rest_framework.serializers import ModelSerializer
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(ModelSerializer):
    # serializes a user profile object

    # meta to indicate specific model in our app
    class Meta:
        model = models.UserProfile
        # fields that we want to have accessible in our model
        fields = ('id','email','name','password')
        # password we make write only
        extra_kwargs = {
            'password': {
                "write_only":True,
                # by below we will see only dots
                'style': {
                    'input_type':'password'
                }
            }
        }

    # first data will be validate and then creation will be triggered
    def create(self,validated_data):
        # creating and returning a new user
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user


    # def update(self, instance, validated_data):
    # """Handle updating user account"""
    #     if 'password' in validated_data:
    #         password = validated_data.pop('password')
    #         instance.set_password(password)

    #     return super().update(instance, validated_data)


class  ProfileFeedItemSerializer(serializers.ModelSerializer):
    # serializing feed model
    class Meta:
        # indicating model for using serializer
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        # setting user_profile read only
        extra_kwargs = {
            'user_profile': {
                "read_only":True,
            }
        }