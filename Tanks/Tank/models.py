from django.db import models
from User.models import Usuario

# Create your models here.
class Tanque(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.FloatField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tanques", null=True)

    def __str__(self):
        return self.nombre