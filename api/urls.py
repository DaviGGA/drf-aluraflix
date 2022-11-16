from django.urls import path
from api.views import *
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Aluraflix",
      default_version='v1',
      description="",
      terms_of_service="#",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('videos/',VideoCreate.as_view(), name = 'videos'),
    path('videos/free/',VideosFreeViewset.as_view(), name = 'videos-free'),
    path('videos/<str:pk>/', VideoViewSet.as_view(), name = 'video-pk'),
    path('categories/',CategoryCreate.as_view(), name = 'categories'),
    path('categories/<str:pk>/',CategoryViewSet.as_view(), name = 'categories-pk'),
    path('categories/<str:pk>/videos', VideosCategoryViewSet.as_view(), name = 'category-videos'),
    path('user/register/', UserRegisterView.as_view(), name = 'user-register'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]  + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)





