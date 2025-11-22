from rest_framework import serializers
from .models import CoverageArea

class CoverageAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverageArea
        fields = '__all__'
