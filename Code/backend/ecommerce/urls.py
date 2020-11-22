from .api import *
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get-token/', obtain_auth_token),
    path('change-password/', ChangePasswordViewSet.as_view(), name='change-password'),
    path('register/', UserCreateViewSet.as_view())
]