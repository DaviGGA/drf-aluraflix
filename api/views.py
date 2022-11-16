from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from .serializer import *
from .models import *

class CategoryCreate(generics.ListCreateAPIView):
    '''Create and list category view'''
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    
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
    permission_classes = (IsAuthenticated,)

class VideoCreate(generics.ListCreateAPIView):
    '''Create and List Video View'''
    serializer_class = VideosSerializer
    permission_classes = (IsAuthenticated,)
   
    def get_queryset(self):
        queryset = Video.objects.all()
        video = self.request.query_params.get('video_search')
        
        if video is not None:
            queryset = queryset.filter(title__icontains = video)
        return queryset

class VideoViewSet(generics.RetrieveUpdateDestroyAPIView):
    '''GET PUT and DELETE by video.id'''
    queryset = Video.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = VideosSerializer

class VideosCategoryViewSet (generics.ListAPIView):
    '''List of videos by category'''
    serializer_class = VideosSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Video.objects.filter(category = self.kwargs['pk'])

        return queryset

class VideosFreeViewset(generics.ListAPIView):
    '''List of videos that doesn't require authentication'''
    serializer_class = VideosSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Video.objects.filter(no_auth_needed = True)

        return queryset

class UserRegisterView(generics.CreateAPIView):
    '''Create User'''
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)