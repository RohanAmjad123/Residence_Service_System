from . import models
from rest_framework import serializers

# Create serializers here.

# Custom User Serializers
class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.CustomUser
        fields = ('email', 'first_name', 'last_name', 'password',)

class StudentCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Student
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['first_name'], validated_data['user']['last_name'],
                                        validated_data['user']['password'])
        student = models.Student.objects.create(user=user, phone_num=validated_data.pop('phone_num'))
        return student

class StaffCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Staff
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['first_name'], validated_data['user']['last_name'],
                                        validated_data['user']['password'])
        staff = models.Staff.objects.create(user=user, phone_num=validated_data.pop('phone_num'))
        return staff

class TechnicianCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Technician
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['first_name'], validated_data['user']['last_name'],
                                        validated_data['user']['password'])
        technician = models.Technician.objects.create(user=user, phone_num=validated_data.pop('phone_num'), specialization=validated_data.pop('specialization'))
        return technician

class AdminCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Admin
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['first_name'], validated_data['user']['last_name'],
                                        validated_data['user']['password'])
        admin = models.Admin.objects.create(user=user, phone_num=validated_data.pop('phone_num'), access_level=validated_data.pop('access_level'))
        return admin

class ChefCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Admin
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['first_name'], validated_data['user']['last_name'],
                                        validated_data['user']['password'])
        chef = models.Chef.objects.create(user=user, phone_num=validated_data.pop('phone_num'), position=validated_data.pop('position'))
        return chef

# General Serializers
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





