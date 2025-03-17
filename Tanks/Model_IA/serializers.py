from rest_framework import serializers
from .models import RegistroTraining

class RegistroTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroTraining
        fields = '__all__'