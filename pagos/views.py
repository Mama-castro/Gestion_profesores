from rest_framework import viewsets

from .models import CartaPagoModel
from .serializers import CartaPagoSerializer


class CartaPagosViewSet(viewsets.ModelViewSet):
    queryset = CartaPagoModel.objects.all()
    serializer_class = CartaPagoSerializer
