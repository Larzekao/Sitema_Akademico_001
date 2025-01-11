from django.db import models # type: ignore
from usuarios.models import Estudiante, Tutor

class Licencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, choices=[
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Pendiente', 'Pendiente'),
    ])
