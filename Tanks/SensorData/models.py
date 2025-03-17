from django.db import models
from Tank.models import Tanque

# Create your models here.
class Sensor(models.Model):
    TIPOS_SENSOR = [
        ('nivel_agua', 'Nivel de Agua'),
        ('flujo_entrada', 'Flujo de Entrada'),
        ('flujo_salida', 'Flujo de Salida'),
        ('presion', 'Presión'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS_SENSOR)
    tanque = models.ForeignKey(Tanque, on_delete=models.CASCADE, related_name="sensores")

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.tanque.nombre}"
