from django.db import models
from Tank.models import Tanque

# Create your models here.
class SensorData(models.Model):
    tanque = models.ForeignKey(Tanque, on_delete=models.CASCADE)
    nivel_agua = models.FloatField()  # cm
    presion = models.FloatField()  # Bar o PSI
    flujo = models.FloatField()  # Litros/minuto
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tanque.nombre} - {self.fecha}"