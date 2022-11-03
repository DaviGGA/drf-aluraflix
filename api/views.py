from django.shortcuts import render
from rest_framework import viewsets,filters,generics
from rest_framework.views import APIView
import django_filters.rest_framework
from .serializer import *
from .models import *

class CategoryCreate(generics.ListCreateAPIView):
    '''Create and list Category View'''
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        queryset = Category.objects.all()
        video = self.request.query_params.get('category_search')
        
        if video is not None:
            queryset = queryset.filter(title__icontains = video)
       
        return queryset

class CategoryViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''GET PUT and DELETE by Category.id'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VideoCreate(generics.ListCreateAPIView):
    '''Create and List Video View'''
    serializer_class = VideosSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        video = self.request.query_params.get('video_search')
        
        if video is not None:
            queryset = queryset.filter(title__icontains = video)
        return queryset

class VideoViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''GET PUT and DELETE by Video.id'''
    queryset = Video.objects.all()
    serializer_class = VideosSerializer

class VideosCategoryViewSet (generics.ListAPIView):
    '''List Videos by category'''
    serializer_class = VideosSerializer
    def get_queryset(self):
        queryset = Video.objects.filter(category = self.kwargs['pk'])

        return queryset