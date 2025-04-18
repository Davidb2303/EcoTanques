from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
