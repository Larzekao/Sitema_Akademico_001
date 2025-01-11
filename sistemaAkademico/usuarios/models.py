from django.db import models # type: ignore

class Usuario(models.Model):
    ROLES = [
        ('Admin', 'Administrador'),
        ('Profesor', 'Profesor'),
        ('Tutor', 'Tutor'),
        ('Estudiante', 'Estudiante'),
    ]
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    # Campos de la tabla Usuario
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    ci = models.CharField(max_length=20, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    edad = models.PositiveIntegerField()
    rol = models.CharField(
        max_length=50,
        choices=ROLES
    )

    def __str__(self):
        return f"{self.username} - {self.rol}"

class Tutor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    parentesco = models.CharField(max_length=50)

class Administrativo(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    puesto = models.CharField(max_length=50)

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    rude_x = models.CharField(max_length=50, unique=True)

class TutorEstudiante(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tutor', 'estudiante')
