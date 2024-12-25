from django.db import models
from usuarios.models import Estudiante

class AsistenciaGeneral(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

    def __str__(self):
        return f"Asistencia de {self.estudiante.usuario.nombre} el {self.fecha}"

class Comportamiento(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50, choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')])

    def __str__(self):
        return f"Comportamiento de {self.estudiante.usuario.nombre} el {self.fecha}: {self.tipo}"
