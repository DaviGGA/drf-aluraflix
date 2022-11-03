from dataclasses import fields
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