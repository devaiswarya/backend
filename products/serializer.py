from rest_framework import serializers
from .models import Product
from categories.serializer import CategoriesSerializer
from fav.models import fav 
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    isFav = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    def get_isFav(self,obj):

        request = self.context.get('request')

        user_id = request.query_params.get('user_id')

        if not user_id:
            return False

        return fav.objects.filter(
            users=user_id,
            product=obj.id
        ).exists()

class ProductDetails(serializers.ModelSerializer):
     category=CategoriesSerializer(read_only=True)
     class Meta:
        model=Product
        fields='__all__'

