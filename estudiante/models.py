from django.db import models

class Curso (models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_horas = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
class Estudiante (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    nota_curso = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Create your models here.
