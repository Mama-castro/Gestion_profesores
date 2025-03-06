from django import forms
from .models import PerfilDocente


class PerfilDocenteForm(forms.ModelForm):
    class Meta:
        model = PerfilDocente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion']
