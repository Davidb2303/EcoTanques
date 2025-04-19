from rest_framework import viewsets
from .models import Medicion
from .serializers import MedicionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin

class MedicionViewSet(viewsets.ModelViewSet):
    serializer_class = MedicionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.rol == 'admin':
            return Medicion.objects.all()
        return Medicion.objects.filter(sensor__tanque__usuario=user)

    def perform_create(self, serializer):
        #Añadir código futuramente
        serializer.save()
