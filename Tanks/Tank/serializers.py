from .models import Tanque
from rest_framework import serializers

class TanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanque
        fields = '__all__'