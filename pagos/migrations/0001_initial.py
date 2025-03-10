# Generated by Django 5.1.6 on 2025-03-02 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.TextField(verbose_name='Detalles de la Carta de Pago')),
                ('fecha_emision', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartas_pago', to='perfiles.perfildocente')),
            ],
        ),
    ]
