from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy  as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, first_name, last_name, phone_num, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_num=phone_num, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, phone_num, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, phone_num, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, first_name, last_name, phone_num, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_num = models.CharField(max_length=10, null=True)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    objects = CustomUserManager()

# Student model
class Student(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    year_of_study = models.IntegerField()

# Staff model
class Staff(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)

# Technician model
class Technician(Staff):
    specialization = models.CharField(max_length=100, null=True)

# Admin model
class Admin(Staff):
    department = models.CharField(max_length=100, null=True)

# Chef model
class Chef(Staff):
    CHEF_POSTIONS = (
        ('LINE', 'LINE'), 
        ('SOUS', 'SOUS'), 
        ('HEAD', 'HEAD'),
    )
    position = models.CharField(max_length=10, choices=CHEF_POSTIONS, default='LINE')

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
    student_id = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)

    # building_id and room_no pairs are enforced with a unique constraint
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['building_id', 'room_no'], name='room_constraint')
        ]

# Maintenance Request model
class MaintenanceRequest(models.Model):
    STATUS = (
        ('RESOLVED', 'RESOLVED'), 
        ('IN PROGRESS', 'IN PROGRESS'),
        ('UNRESOLVED', 'UNRESOLVED'),
    )
    URGENCY_RATING = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    request_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    room_id = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE, null=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    submit_date_time = models.DateTimeField(auto_now_add=True)
    technician_id = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True)
    date_time_resolved = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='UNRESOLVED')
    urgency_rating = models.CharField(max_length=20, choices=URGENCY_RATING, default='1')    

# Complaint Model
class Complaint(models.Model):
    STATUS = (
        ('RESOLVED', 'RESOLVED'), 
        ('IN PROGRESS', 'IN PROGRESS'),
        ('UNRESOLVED', 'UNRESOLVED'),
    )
    URGENCY_RATING = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    complaint_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    submit_date_time = models.DateTimeField(auto_now_add=True)
    problem_description = models.CharField(max_length=200)
    resolution_description = models.CharField(max_length=200)
    date_time_resolved = models.DateTimeField(null=True)
    urgency_rating = models.CharField(max_length=20, choices=URGENCY_RATING, default='1')
    status = models.CharField(max_length=20, choices=STATUS, default='UNRESOLVED')

# FoodOrder model
class FoodOrder(models.Model):
    STATUS = (
        ('FULFILLED', 'FULFILLED'), 
        ('IN PROGRESS', 'IN PROGRESS'),
        ('UNFULFILLED', 'UNFULFILLED')
    )
    food_order_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=100)
    submit_date_time = models.DateTimeField(auto_now_add=True)
    chef_id = models.ForeignKey(Chef, on_delete=models.SET_NULL, null=True)
    date_time_fulfilled = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='UNFULFILLED')

# Package Model
class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_recieved = models.DateField(auto_now_add=True)


