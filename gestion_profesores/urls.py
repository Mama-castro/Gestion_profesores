"""
URL configuration for gestion_profesores project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from categorias.views import CategoriaDocenteViewSet
from contratos.views import ContratoViewSet
from dashboard.views import dashboard_view
from perfiles.views import PerfilDocenteViewSet
from pagos.views import CartaPagosViewSet

router = DefaultRouter()
# router.register(r'usuarios', ),
router.register(r'perfil', PerfilDocenteViewSet),
router.register(r'categorias', CategoriaDocenteViewSet),
router.register(r'pagos', CartaPagosViewSet),
router.register(r'contratos', ContratoViewSet),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
