from rest_framework import serializers
from .models import Cart
from products.serializer import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'  

class CartDetails(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'

