from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    ADMIN = 'admin'
    OPERADOR = 'operador'
    TECNICO = 'tecnico'
    ROLES = [(ADMIN, 'Admin'), (OPERADOR, 'Operador'), (TECNICO, 'Técnico')]
    rol = models.CharField(max_length=20, choices=ROLES, default=OPERADOR)