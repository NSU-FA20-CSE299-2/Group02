from django.urls import path
from .api import (
    UserIDView,
    ItemListView,
    ItemDetailView,
    AddToCartView,
    OrderDetailView,
    OrderQuantityUpdateView,
    AddCouponView,
    OrderItemDeleteView,
)

urlpatterns = [
    path('user-id/', UserIDView.as_view(), name='user-id'),
    path('products/', ItemListView.as_view(), name='product-list'),
    path('products/<pk>/', ItemDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('order-summary/', OrderDetailView.as_view(), name='order-summary'),
    path('checkout/', PaymentView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('order-items/<pk>/delete/',
         OrderItemDeleteView.as_view(), name='order-item-delete'),
    path('order-item/update-quantity/',
         OrderQuantityUpdateView.as_view(), name='order-item-update-quantity'),
]