from . import models
from rest_framework import serializers

# Create serializers here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'
    
class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technician
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = '__all__'

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chef
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceRequest
        fields = '__all__'

class ResolvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resolves
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complaint
        fields = '__all__'

class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodOrder
        fields = '__all__'

class FulfillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fulfills
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Package
        fields = '__all__'





