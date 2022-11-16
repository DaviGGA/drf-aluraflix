from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','id']
        extra_kwargs = {
            'password' : {'write_only' : True, 'required' : True},
            'username' : {'required' : True} 
        }

    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
        )
        
        user.save()

        return user