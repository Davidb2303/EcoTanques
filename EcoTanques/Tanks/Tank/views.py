from rest_framework import viewsets
from .models import Tanque
from .serializers import TanqueSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin

class TanqueViewSet(viewsets.ModelViewSet):
    serializer_class = TanqueSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.rol == 'admin':
            return Tanque.objects.all()
        return Tanque.objects.filter(usuario=user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
