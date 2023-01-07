from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FileViewSet, PlayerViewSet

router = DefaultRouter()

router.register(r'players', PlayerViewSet, basename='players')
router.register(r'files', FileViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls)),
]
