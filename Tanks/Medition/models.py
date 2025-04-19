from django.db import models
from SensorData import Sensor

# Create your models here.
class Medicion(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="mediciones")
    valor = models.FloatField(help_text="Valor de la medición tomada por el sensor")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.get_tipo_display()}: {self.valor} ({self.timestamp})"