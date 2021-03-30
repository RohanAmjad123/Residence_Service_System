from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here (API Endpoints).

class StudentViewSet(viewsets.ModelViewSet):
    # Refer to QuerySet documentatino for complex SQL queries
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer

class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = models.Technician.objects.all()
    serializer_class = serializers.TechnicianSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer

class ChefViewSet(viewsets.ModelViewSet):
    queryset = models.Chef.objects.all()
    serializer_class = serializers.ChefSerializer

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

