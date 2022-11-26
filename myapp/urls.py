from django.urls import path
from django.urls.conf import include
from myapp.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', ProfileViewSet, basename='list')

urlpatterns = [
    path('', include(router.urls))
]