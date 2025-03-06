from rest_framework import serializers
from .models import CartaPagoModel


class CartaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaPagoModel
        fields = '__all__'
