from django.urls import path, include
from api.views import *

urlpatterns = [
    path('videos/',VideoCreate.as_view(), name= 'videos'),
    path('videos/<str:pk>/', VideoViewSet.as_view(), name = 'video-pk'),
    path('categories/',CategoryCreate.as_view(), name = 'categories'),
    path('categories/<str:pk>/',CategoryViewSet.as_view(), name = 'categories-pk'),
    path('categories/<str:pk>/videos', VideosCategoryViewSet.as_view(), name = 'category-videos')
]
