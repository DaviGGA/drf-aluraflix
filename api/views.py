from django.shortcuts import render
from rest_framework import viewsets,filters,generics
from rest_framework.views import APIView
from .serializer import videosSerializer
from .models import Video

class VideoCreate(generics.ListCreateAPIView):
    '''Create View'''
    queryset = Video.objects.all()
    serializer_class = videosSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    
    


class VideoViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''GET PUT and DELETE by Video.id'''
    queryset = Video.objects.all()
    serializer_class = videosSerializer