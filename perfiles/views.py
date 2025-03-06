from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from rest_framework import viewsets
from .perfilForms import PerfilDocenteForm
from .models import PerfilDocente
from .serializers import PerfilDocenteSerializer
from django.urls import reverse_lazy


class PerfilDocenteViewSet(viewsets.ModelViewSet):
    queryset = PerfilDocente.objects.all()
    serializer_class = PerfilDocenteSerializer


class CrearPerfilView(CreateView):
    model = PerfilDocente
    form_class = PerfilDocenteForm
    template_name = 'perfiles/template/formulario_perfil.html'
    success_url = reverse_lazy('detalle-perfil')


class ModificarPerfilView(UpdateView):
    model = PerfilDocente
    form_class = PerfilDocenteForm
    template_name = 'perfiles/template/formulario_perfil.html'
    success_url = reverse_lazy('detalle-perfil')


class DetallePerfilView(DetailView):
    model = PerfilDocente
    template_name = 'perfiles/template/detalle_perfil.html'
