from .api import *
from django.urls import path
from rest_framework import routers

urlpatterns = []

router = routers.DefaultRouter()

router.register('', TransactionViewSet, 'category')

urlpatterns += router.urls