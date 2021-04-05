from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Staff)
admin.site.register(models.Technician)
admin.site.register(models.Admin)
admin.site.register(models.Chef)
admin.site.register(models.Building)
admin.site.register(models.Room)
admin.site.register(models.MaintenanceRequest)
admin.site.register(models.Resolves)
admin.site.register(models.Complaint)
admin.site.register(models.FoodOrder)
admin.site.register(models.Fulfills)
admin.site.register(models.Package)