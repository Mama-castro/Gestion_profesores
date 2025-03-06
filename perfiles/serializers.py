from rest_framework import serializers
from .models import PerfilDocente


class PerfilDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilDocente
        fields = '__all__'
