from django.urls import path, include
from api.views import *

urlpatterns = [
    path('videos/',VideoCreate.as_view(), name= 'videos'),
    path('videos/<str:pk>/', VideoViewSet.as_view(), name = 'video-pk'),
]