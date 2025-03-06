from django.db import models
from simple_history.models import HistoricalRecords

from perfiles.models import PerfilDocente


class Contrato(models.Model):
    perfil = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='contratos')
    tipo_contrato = models.CharField("Tipo de Contrato", max_length=3,
                                     choices=[('TP', 'Tiempo Parcial'),
                                              ('ABC', 'Cuadros no docente (ABC)'),
                                              ('PC', 'Perfil de Competencia')])
    fecha_inicio = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    fecha_fin = models.DateTimeField("Fecha de Actualización", auto_now=True)
    documento = models.FileField(upload_to='contratos/')
    history = HistoricalRecords()
    def __str__(self):
        return f"{self.get_tipo_contrato_display()} - {self.perfil}"

    def get_tipo_contrato_display(self):
        pass
