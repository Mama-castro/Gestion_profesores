from rest_framework import serializers
from .models import CategoriaDocente


class CategoriaDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaDocente
        fields = '__all__'
