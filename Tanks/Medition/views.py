from django.shortcuts import render
from rest_framework import viewsets
from .models import Medicion
from .serializers import MedicionSerializer

# Create your views here.

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer