from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    #path('', MovieViewSet.as_view({'get': 'list', 'post': 'create'}))
]