from rest_framework import serializers
from .models import fav

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model=fav
        fields='__all__'