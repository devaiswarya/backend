from rest_framework import serializers
from .models import fav
from products.serializer import ProductSerializer

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model=fav
        fields='__all__'

class FavProduct(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model=fav
        fields='__all__'
