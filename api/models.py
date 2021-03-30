from django.db import models

# Create your models here.

# Student Model
class Student(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

# Building model
class Building(models.Model):
    building_id = models.CharField(max_length=8, primary_key=True)
    building_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=10)
    year_level = models.CharField(max_length=1)

class Room(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=10)
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    # building_id and room_no pairs are enforced with a unique constraint
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['building_id', 'room_no'], name='constraint')
        ]

'''
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


