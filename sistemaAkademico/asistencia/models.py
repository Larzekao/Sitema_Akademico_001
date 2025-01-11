from django.db import models # type: ignore
from usuarios.models import Estudiante

class AsistenciaGeneral(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=[
        ('Presente', 'Presente'),
        ('Ausente', 'Ausente'),
        ('Tarde', 'Tarde'),
    ])
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)

class Comportamiento(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=[
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo'),
    ])
