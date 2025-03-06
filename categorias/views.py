from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.template import loader

from .models import CategoriaDocente
from .serializers import CategoriaDocenteSerializer


class CategoriaDocenteViewSet(viewsets.ModelViewSet):
    queryset = CategoriaDocente.objects.all()
    serializer_class = CategoriaDocenteSerializer
