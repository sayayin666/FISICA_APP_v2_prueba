from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import UserApiViewSet

router_user = DefaultRouter()
router_user.register(
    prefix='users', viewset=UserApiViewSet, basename='users'
)