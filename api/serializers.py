from . import models
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Create serializers here.

# JWT Token Obtain Serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['is_student'] = user.is_student
        token['is_admin'] = user.is_admin
        token['is_technician'] = user.is_technician
        token['is_chef'] = user.is_chef
        return token

# Custom User Serializers
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_num')

class CustomUserSerializerTwo(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_num')


class StudentCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    class Meta:
        model = models.Student
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['password'], validated_data['user']['first_name'],
                                        validated_data['user']['last_name'], validated_data['user']['phone_num'])
        user.is_student = True 
        user.save()
        student = models.Student.objects.create(user=user, year_of_study=validated_data.pop('year_of_study'))
        return student

class StaffCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Staff
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['password'], validated_data['user']['first_name'],
                                        validated_data['user']['last_name'], validated_data['user']['phone_num'])
        staff = models.Staff.objects.create(user=user)
        return staff

class TechnicianCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Technician
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['password'], validated_data['user']['first_name'],
                                        validated_data['user']['last_name'], validated_data['user']['phone_num'])
        user.is_technician = True 
        user.save()
        technician = models.Technician.objects.create(user=user, specialization=validated_data.pop('specialization'))
        return technician

class AdminCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Admin
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['password'], validated_data['user']['first_name'],
                                        validated_data['user']['last_name'], validated_data['user']['phone_num'])
        user.is_admin = True 
        user.save()
        admin = models.Admin.objects.create(user=user, department=validated_data.pop('department'))
        return admin

class ChefCustomRegistrationSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    
    class Meta:
        model = models.Chef
        fields = '__all__'

    def create(self, validated_data, *args, **kwargs):
        user = models.CustomUser.objects.create_user(validated_data['user']['email'], validated_data['user']['password'], validated_data['user']['first_name'],
                                        validated_data['user']['last_name'], validated_data['user']['phone_num'])
        user.is_chef = True 
        user.save()
        chef = models.Chef.objects.create(user=user, position=validated_data.pop('position'))
        return chef

# General Serializers
class StudentSerializer(serializers.ModelSerializer): 
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_num = serializers.CharField(source='user.phone_num')

    class Meta:
        model = models.Student
        fields = '__all__'

class StudentPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['year_of_study']

class StaffSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_num = serializers.CharField(source='user.phone_num')

    class Meta:
        model = models.Staff
        fields = '__all__'
  
class TechnicianSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_num = serializers.CharField(source='user.phone_num')
    
    class Meta:
        model = models.Technician
        fields = '__all__'

class TechnicianPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technician
        fields = ['specialization']

class AdminSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_num = serializers.CharField(source='user.phone_num')
    
    class Meta:
        model = models.Admin
        fields = '__all__'

class AdminPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = ['department']

class ChefSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_num = serializers.CharField(source='user.phone_num')
    
    class Meta:
        model = models.Chef
        fields = '__all__'

class ChefPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chef
        fields = ['position']

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
        fields = ['resolution_description', 'staff_id', 'date_time_resolved', 'status']

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





