from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensor
from .serializers import SensorSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin

# Create your views here.
class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    
    def get_queryset(self):
        user = self.request.user
        if user.rol == 'admin':
            return Sensor.objects.all()
        return Sensor.objects.filter(tanque__usuario=user)

    def perform_create(self, serializer):
        tanque = Sensor.objects.get(id=self.request.data.get('tanque'))
        if tanque.usuario == self.request.user:
            serializer.save(tanque=tanque)

