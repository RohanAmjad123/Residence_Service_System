from django.db import models

# Create your models here.

# Student Model
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

class Building(models.Model):
    building_id = models.IntegerField(primary_key=True)
    building_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=10)
    year_level = models.CharField(max_length=10)
'''
class Room(models.Model):
    # Define model here

class MaintenanceRequest(models.Model):
    # Define model here

class Resolves(models.Model):
    # Define model here

class Fulfills(models.Model):
    # Define model here

class Package(models.Model):
    # Define model here

class Complaint(models.Model):
    # Define model here

class FoodOrder(models.Model):
    # Define model here

class Staff(models.Model):
    # Define model here

class Technician(models.Model):
    # Define model here

class Admin(models.Model):
    # Define model here

class Chef(models.Model):
    # Define model here
'''


