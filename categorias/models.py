from django.db import models

from perfiles.models import PerfilDocente
from simple_history.models import HistoricalRecords


class CategoriaDocente(models.Model):
    OPCIONES_CATEGORIA = (
        ('Asistente', 'Asistente'),
        ('Auxiliar', 'Auxiliar'),
        ('Titular', 'Titular')
    )
    perfil = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='categorias_docentes')
    categoria = models.CharField("Categoría", max_length=100, choices=OPCIONES_CATEGORIA)
    fecha_inicio = models.DateField("Fecha de Inicio")
    fecha_fin = models.DateField("Fecha de Fin", blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.perfil} - {self.categoria}"


class ConfiguracionAlerta(models.Model):
    mensaje_alerta = models.CharField("Mensaje de Alerta", max_length=255)
    dias_anticipacion = models.PositiveIntegerField("Días de Anticipación", default=30)
    activa = models.BooleanField("Alerta Activa", default=True)

    def __str__(self):
        return self.mensaje_alerta
