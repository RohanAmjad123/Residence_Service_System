from . import models
from rest_framework import serializers

# Create serializers here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = '__all__'
