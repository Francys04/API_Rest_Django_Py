from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = [
            'title',
            'content',
            'sale_price',
            'get_discount',
        ]