from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Usuario(AbstractUser):
    ADMIN = 'admin'
    OPERADOR = 'operador'
    TECNICO = 'tecnico'
    ROLES = [(ADMIN, 'Admin'), (OPERADOR, 'Operador'), (TECNICO, 'Técnico')]
    rol = models.CharField(max_length=20, choices=ROLES, default=OPERADOR)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="usuarios_groups",  # Cambiado de user_set a usuarios_groups
        related_query_name="usuario",
        )
        
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="usuarios_permissions",  # Cambiado de user_set a usuarios_permissions
        related_query_name="usuario",
    )

    def __str__(self):
        return self.username
    