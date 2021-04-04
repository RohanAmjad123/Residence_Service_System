from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

    def get_queryset(self):
        return models.Room.objects.filter(building_id=self.kwargs['building_pk'])

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = models.MaintenanceRequest.objects.all()
    serializer_class = serializers.MaintenanceRequestSerializer

class ResolvesViewSet(viewsets.ModelViewSet):
    queryset = models.Resolves.objects.all()
    serializer_class = serializers.ResolvesSerializer

    def get_queryset(self):
        return models.Resolves.objects.filter(request_id=self.kwargs['maintreq_pk'])

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = models.Complaint.objects.all()
    serializer_class = serializers.ComplaintSerializer

class FoodOrderViewSet(viewsets.ModelViewSet):
    queryset = models.FoodOrder.objects.all()
    serializer_class = serializers.FoodOrderSerializer

class FulfillsViewSet(viewsets.ModelViewSet):
    queryset = models.Fulfills.objects.all()
    serializer_class = serializers.FulfillsSerializer

    def get_queryset(self):
        return models.Fulfills.objects.filter(food_order_id=self.kwargs['foodorder_pk'])

class PackageViewSet(viewsets.ModelViewSet):
    queryset = models.Package.objects.all()
    serializer_class = serializers.PackageSerializer

def frontpage(request):
    return render(request, 'residentSystem/frontpage.html')



def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

    if form.is_valid():
        user = form.save()
        login(request,user)

        return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'residentSystem/signup.html', {'form': form})
 