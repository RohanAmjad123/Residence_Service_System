from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register your models here.
admin.site.register(models.CustomUser, CustomUserAdmin)
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