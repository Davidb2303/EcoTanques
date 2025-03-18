from rest_framework import viewsets
from .models import Tanque
from .serializers import TanqueSerializer

# Create your views here.
class TanqueViewSet(viewsets.ModelViewSet):
    queryset = Tanque.objects.all()
    serializer_class = TanqueSerializer