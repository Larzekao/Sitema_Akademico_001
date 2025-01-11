from django.db import models # type: ignore
from usuarios.models import Usuario, Estudiante

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    especialidad = models.CharField(max_length=50)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Aula(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=255)

class Clases(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    docente = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    dia = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
