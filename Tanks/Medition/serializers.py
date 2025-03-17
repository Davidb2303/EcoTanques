import rest_framework.serializers as serializers
from .models import Medicion

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = '__all__'