from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensor
from .serializers import SensorSerializer

# Create your views here.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer