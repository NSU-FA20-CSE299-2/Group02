from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .api import *
from rest_framework import routers

urlpatterns = [
    path('get-token/', obtain_auth_token),
    path('change-password/', ChangePasswordViewSet.as_view(), name='change-password'),
    path('register/', UserCreateViewSet.as_view(), name='register')
]

router = routers.DefaultRouter()
router.register('address', AddressViewSet, 'address')

urlpatterns += router.urls