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
class Technician(Staff):
    specialization = models.CharField(max_length=50)

# Admin model
class Admin(Staff):
    access_level = models.IntegerField()


# Chef model
class Chef(Staff):
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
    room_id = models.AutoField(primary_key=True)
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
    resolves_id = models.AutoField(primary_key=True)
    technician_id = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True)
    request_id = models.ForeignKey(MaintenanceRequest, on_delete=models.CASCADE)
    date_time_resolved = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    urgency_rating = models.IntegerField()
    
    # technician_id and request_id pairs are enforced with a unique constraint
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['technician_id', 'request_id'], name='resolves_constraint')
        ]

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    submit_date = models.DateTimeField(auto_now_add=True)
    problem_description = models.CharField(max_length=200)
    resolution_description = models.CharField(max_length=200)
    urgency_rating = models.IntegerField()
    status = models.CharField(max_length=20)

class FoodOrder(models.Model):
    food_order_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

class Fulfills(models.Model):
    fulfills_id = models.AutoField(primary_key=True)
    food_order_id = models.ForeignKey(FoodOrder, on_delete=models.CASCADE)
    chef_id = models.ForeignKey(Chef, on_delete=models.SET_NULL, null=True)
    date_time_fulfilled = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    
    # chef_id and food_order_id pairs are enforced with a unique constraint
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['chef_id', 'food_order_id'], name='fulfills_constraint')
        ]

class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_recieved = models.DateField(auto_now_add=True)


