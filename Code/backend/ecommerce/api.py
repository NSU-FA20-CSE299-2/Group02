from ecommerce.models import *
from rest_framework import viewsets, permissions, authentication
from .serializer import *

class CategoryViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    serializer_class = CategorySerializer
    
    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

class ItemViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset

class OderItemViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    serializer_class = OrderItemSerializer
    
    def get_queryset(self):
        queryset = OrderItem.objects.all()
        return queryset

class OrderViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Order.objects.all()
        return queryset

class PaymentViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset