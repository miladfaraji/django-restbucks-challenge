from rest_framework import serializers

from project.apps.product.models import Product, ProductFeature


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class ProductFeatureSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='product_name')

    class Meta:
        model = ProductFeature
        fields = ('id', 'name', 'value', 'price')
        read_only_fields = ('id', 'name', 'value', 'price')