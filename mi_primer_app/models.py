from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def  __str__(self):
        return f"{self.nombre} tiene {self.edad} años"  