from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
#from usuarios.models import UserManage


class PerfilDocente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellidos", max_length=254)
    correo = models.EmailField("Correo Electrónico")
    telefono = models.CharField("Telefono", max_length=11, blank=True, null=True)
    direccion = models.TextField("Direccion", max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.nombre}{' '}{self.apellido}"


class TituloCertificacion(models.Model):
    perfil = models.ForeignKey(PerfilDocente, on_delete=models.CASCADE, related_name='titulos_certificaciones')
    titulo = models.CharField("Título/Certificación", max_length=250)
    institucion = models.CharField("Institución", max_length=200)
    fecha_obtencion = models.DateField("Fecha de Obtención")

    def __str__(self):
        return self.titulo
