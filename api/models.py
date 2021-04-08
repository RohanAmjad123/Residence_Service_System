from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy  as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    objects = CustomUserManager()

# Student model
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    phone_num = models.CharField(max_length=10)

# Staff model
class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    staff_id = models.AutoField(primary_key=True)
    phone_num = models.CharField(max_length=10)

# Technician model
class Technician(Staff):
    SPECIALIZATIONS = (
        ('GENERAL', 'GENERAL'), 
        ('HEATING', 'HEATING'), 
        ('PLUMBING', 'PLUMBING'),
    )
    specialization = models.CharField(max_length=50, choices=SPECIALIZATIONS, default='GENERAL')

# Admin model
class Admin(Staff):
    ACCESS_LEVELS = (
        ('LOW', 'LOW'), 
        ('MID', 'MID'), 
        ('HIGH', 'HIGH'),
    )
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVELS, default='LOW')

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
    request_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    room_id = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE, null=False)
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


