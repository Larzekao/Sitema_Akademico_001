from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    ci = models.CharField(max_length=20, unique=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    edad = models.IntegerField()
    rol = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    rudex = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} - RUDEX: {self.rudex}"

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} - {self.especialidad}"

class Tutor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} - {self.parentesco}"
