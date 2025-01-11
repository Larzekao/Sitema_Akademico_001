from django.db import models # type: ignore

class PeriodoEscolar(models.Model):
    anio = models.PositiveIntegerField()
    division = models.CharField(max_length=50, choices=[
        ('Bimestral', 'Bimestral'),
        ('Semestral', 'Semestral'),
        ('Trimestral', 'Trimestral'),
    ])

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
