from django.db import models

# Create your models here.

# Student model
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

# Staff model
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

# Technician model
class Technician(models.Model):
    technician_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)

# Admin model
class Admin(models.Model):
    admin_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    access_level = models.IntegerField()


# Chef model
class Chef(models.Model):
    chef_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)

# Building model
class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=10)
    year_level = models.IntegerField()

# Room model
class Room(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=10)
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    # building_id and room_no pairs are enforced with a unique constraint
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['building_id', 'room_no'], name='room_constraint')
        ]

# Maintenance Request model
class MaintenanceRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    building_id = models.ForeignKey(Room, related_name='building', on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    submit_date_time = models.DateTimeField(auto_now_add=True)

# Resolves model
class Resolves(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    request_id = models.ForeignKey(MaintenanceRequest, on_delete=models.CASCADE)
    date_time_resolved = models.DateTimeField()
    status = models.CharField(max_length=50)
    urgency_rating = models.IntegerField()

   # staff_id and request_id pairs are enforced with a unique constraint
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['staff_id', 'request_id'], name='resolves_constraint')
        ]

'''
class Fulfills(models.Model):
    # Define model here

class Package(models.Model):
    # Define model here

class Complaint(models.Model):
    # Define model here

class FoodOrder(models.Model):
    # Define model here

'''


