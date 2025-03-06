from django.db import models
from simple_history.models import HistoricalRecords

from perfiles.models import PerfilDocente


class CartaPagoModel(models.Model):
    perfil = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='cartas_pago')
    detalles = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateField("Fecha de Creación", auto_now_add=True)
    documento = models.FileField(upload_to='pagos/', null=True, blank=True)
    history = HistoricalRecords()

    # def __str__(self):
    #     return f"Carta de Pago - {self.perfil}"
