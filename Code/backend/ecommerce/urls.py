from .api import *
from django.urls import path
from rest_framework import routers

urlpatterns = []

router = routers.DefaultRouter()

router.register('category', CategoryViewSet, 'category')
router.register('item', ItemViewSet, 'item')
router.register('orderitem', OrderItemViewSet, 'orderitem')
router.register('order', OrderViewSet, 'order')
router.register('payment', PaymentViewSet, 'payment')

urlpatterns += router.urls