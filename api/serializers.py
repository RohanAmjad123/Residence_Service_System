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
        user.is_student = True 
        user.save()
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
        user.is_technician = True 
        user.save()
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
        user.is_admin = True 
        user.save()
        admin = models.Admin.objects.create(user=user, phone_num=validated_data.pop('phone_num'), access_level=validated_data.pop('access_level'))
        return admin

class ChefCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Chef
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['first_name'], validated_data['user']['last_name'],
                                        validated_data['user']['password'])
        user.is_chef = True 
        user.save()
        chef = models.Chef.objects.create(user=user, phone_num=validated_data.pop('phone_num'), position=validated_data.pop('position'))
        return chef

# General Serializers
class StudentSerializer(serializers.ModelSerializer): 
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = models.Student
        fields = '__all__'

class StudentPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['phone_num']

class StaffSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = models.Staff
        fields = '__all__'

class StaffPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = ['phone_num']
    
class TechnicianSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    
    class Meta:
        model = models.Technician
        fields = '__all__'

class TechnicianPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technician
        fields = ['phone_num', 'specialization']

class AdminSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    
    class Meta:
        model = models.Admin
        fields = '__all__'

class AdminPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = ['phone_num', 'access_level']

class ChefSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    
    class Meta:
        model = models.Chef
        fields = '__all__'

class ChefPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chef
        fields = ['phone_num', 'position']

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class RoomPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['room_no']

class RoomPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['student_id']

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceRequest
        fields = '__all__'

class MaintenanceRequestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceRequest
        fields = ['description', 'student_id', 'urgency_rating', 'submit_date_time']

class MaintenanceRequestPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceRequest
        fields = ['technician_id', 'status', 'date_time_resolved']

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complaint
        fields = '__all__'

class ComplaintPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complaint
        fields = ['problem_description', 'student_id', 'submit_date_time', 'urgency_rating']

class ComplaintPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complaint
        fields = ['resolution_description', 'admin_id', 'date_time_resolved', 'status']

class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodOrder
        fields = '__all__'

class FoodOrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodOrder
        fields = ['description', 'student_id', 'submit_date_time']

class FoodOrderPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodOrder
        fields = ['chef_id', 'status', 'date_time_fulfilled']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Package
        fields = '__all__'





