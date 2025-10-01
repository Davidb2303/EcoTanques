from django.db import models
from Tank.models import Tanque

# Create your models here.
class RegistroTraining(models.Model):
    tanque = models.ForeignKey(Tanque, on_delete=models.CASCADE, related_name="registros_training")
    nivel_agua = models.FloatField()
    flujo_entrada = models.FloatField()
    flujo_salida = models.FloatField()
    presion = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registro ML - {self.tanque.nombre} ({self.fecha})"
