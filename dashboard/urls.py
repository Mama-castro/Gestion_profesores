from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import dashboard_data


# def dashboard_view(request):
#     return render(request, 'dashboard.html')
#
#
# router = DefaultRouter()
# router.register(r'data/', dashboard_data),
# router.register(r'', dashboard_view)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
