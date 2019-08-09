from rest_framework import serializers

from project.apps.order.models import Order, OrderProductFeature
from project.apps.product.serializers import ProductFeatureSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product_feature = ProductFeatureSerializer()

    class Meta:
        model = OrderProductFeature
        fields = ('id', 'product_feature', 'number')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'created_at', 'price', 'order_items')


class ProductFeatureNumberSerializer(serializers.Serializer):
    product_feature_id = serializers.IntegerField()
    number = serializers.IntegerField()


class OrderCreateSerializer(serializers.Serializer):
    order_items = ProductFeatureNumberSerializer(many=True)

    # class Meta:
    #     model = Order
    #     fields = ('id', 'created_at', 'product_features', 'price')
    #     read_only_fields = ('id', 'created_at', 'price')


class CancelOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status')

