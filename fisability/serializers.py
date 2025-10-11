from rest_framework import serializers
from .models import Fisability

class FisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fisability
        fields = '__all__'
