from collections import Counter

from django.http import JsonResponse
from django.shortcuts import render

from perfiles.models import PerfilDocente
from contratos.models import Contrato
from categorias.models import CategoriaDocente


def dashboard_view(request):
    return render(request, 'dashboard.html')


def dashboard_data(request):
    total_profesores = PerfilDocente.objects.count()

    total_contratos = Contrato.objects.values_list('tipo', flat=True)
    contratos_count = dict(Counter(total_contratos))

    categorias = CategoriaDocente.objects.values_list('categoria', flat=True)
    categorias_count = dict(Counter(categorias))

    data = {
        "total_Profesores": total_profesores,
        "contratos": contratos_count,
        "categorias": categorias_count,
    }

    return JsonResponse
