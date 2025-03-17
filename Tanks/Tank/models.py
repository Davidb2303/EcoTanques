from django.db import models

# Create your models here.
class Tanque(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.FloatField()  # Litros
    ubicacion = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"
