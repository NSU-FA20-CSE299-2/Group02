from rest_framework import serializers
from ecommerce.models import (
    Address, Item, Order, OrderItem, Coupon, Variation, ItemVariation,
    Payment
)


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = (
            'id',
            'code',
            'amount'
        )


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'category',
            'label',
            'slug',
            'description',
            'image'
        )


class VariationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = (
            'id',
            'name',
            'item'
        )


class ItemVariationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemVariation
        fields = (
            'id',
            'value',
            'attachment',
            'variation'
        )


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'item',
            'item_variations',
            'quantity',
            'final_price'
        )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id',
            'items',
            'total',
            'coupon'
        )


class ItemVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariation
        fields = (
            'id',
            'value',
            'attachment'
        )


class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = (
            'id',
            'name',
            'item_variations'
        )


class ItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'category',
            'label',
            'slug',
            'description',
            'image',
            'variations'
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'amount',
            'timestamp'
        )