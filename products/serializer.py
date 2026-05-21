from rest_framework import serializers
from .models import Product
from categories.serializer import CategoriesSerializer

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class ProductDetails(serializers.ModelSerializer):
     category=CategoriesSerializer(read_only=True)
     class Meta:
        model=Product
        fields='__all__'

