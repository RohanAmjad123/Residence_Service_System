from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here (API Endpoints).

class StudentViewSet(viewsets.ModelViewSet):
    # Refer to QuerySet documentatino for complex SQL queries
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

