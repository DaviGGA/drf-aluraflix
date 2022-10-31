from dataclasses import fields
from rest_framework import serializers
from .models import *

class videosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title','description','url','id']