from django.db import models
from User.models import Usuario

# Create your models here.
class Tanque(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.FloatField(help_text="Capacidad máxima del tanque en litros")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tanques", null=True)

    def __str__(self):
        return f"{self.nombre} - {self.User.username}"