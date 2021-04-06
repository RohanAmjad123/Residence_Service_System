from rest_framework import viewsets, generics
from . import models
from . import serializers
from rest_framework.response import Response

# Registration ViewSets
class StudentRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentCustomRegistrationSerializer
    queryset = models.Student.objects.all()
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        student_data = serializers.StudentSerializer(student, context=self.get_serializer_context()).data
        
        return Response({
             "student": student_data,
             "email": student.user.email,
        })

class StaffRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StaffCustomRegistrationSerializer
    queryset = models.Staff.objects.all()
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff = serializer.save()
        staff_data = serializers.StaffSerializer(staff, context=self.get_serializer_context()).data
        
        return Response({
             "staff": staff_data,
             "email": staff.user.email,
        })

class TechnicianRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TechnicianCustomRegistrationSerializer
    queryset = models.Technician.objects.all()
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        technician = serializer.save()
        technician_data = serializers.TechnicianSerializer(technician, context=self.get_serializer_context()).data
        
        return Response({
             "technician": technician_data,
             "email": technician.user.email,
        })

class AdminRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AdminCustomRegistrationSerializer
    queryset = models.Admin.objects.all()
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        admin = serializer.save()
        admin_data = serializers.AdminSerializer(admin, context=self.get_serializer_context()).data
        
        return Response({
             "admin": admin_data,
             "email": admin.user.email,
        })

class ChefRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChefCustomRegistrationSerializer
    queryset = models.Chef.objects.all()
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chef = serializer.save()
        chef_data = serializers.ChefSerializer(chef, context=self.get_serializer_context()).data
        
        return Response({
             "chef": chef_data,
             "email": chef.user.email,
        })

# General ViewSets
class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    http_method_names = ['get', 'patch']

class StaffViewSet(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    http_method_names = ['get', 'patch']

class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = models.Technician.objects.all()
    serializer_class = serializers.TechnicianSerializer
    http_method_names = ['get', 'patch']

class AdminViewSet(viewsets.ModelViewSet):
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer
    http_method_names = ['get', 'patch']

class ChefViewSet(viewsets.ModelViewSet):
    queryset = models.Chef.objects.all()
    serializer_class = serializers.ChefSerializer
    http_method_names = ['get', 'patch']

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = models.MaintenanceRequest.objects.all()
    serializer_class = serializers.MaintenanceRequestSerializer

class ResolvesViewSet(viewsets.ModelViewSet):
    queryset = models.Resolves.objects.all()
    serializer_class = serializers.ResolvesSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = models.Complaint.objects.all()
    serializer_class = serializers.ComplaintSerializer

class FoodOrderViewSet(viewsets.ModelViewSet):
    queryset = models.FoodOrder.objects.all()
    serializer_class = serializers.FoodOrderSerializer

class FulfillsViewSet(viewsets.ModelViewSet):
    queryset = models.Fulfills.objects.all()
    serializer_class = serializers.FulfillsSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = models.Package.objects.all()
    serializer_class = serializers.PackageSerializer

