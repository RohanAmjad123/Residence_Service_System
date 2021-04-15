from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()

# Register URL's for viewsets here.

router.register('students', views.StudentViewSet)
router.register('staff', views.StaffViewSet)
router.register('technicians', views.TechnicianViewSet)
router.register('admins', views.AdminViewSet)
router.register('chefs', views.ChefViewSet)
router.register('buildings', views.BuildingViewSet)
router.register('rooms', views.RoomViewSet)
router.register('maintreqs', views.MaintenanceRequestViewSet)
router.register('complaints', views.ComplaintViewSet)
router.register('foodorders', views.FoodOrderViewSet)
router.register('packages', views.PackageViewSet)
router.register('users', views.CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'register/student/', views.StudentRegistrationViewSet.as_view({'post': 'create'})),
    path(r'register/staff/', views.StaffRegistrationViewSet.as_view({'post': 'create'})),
    path(r'register/technician/', views.TechnicianRegistrationViewSet.as_view({'post': 'create'})),
    path(r'register/admin/', views.AdminRegistrationViewSet.as_view({'post': 'create'})),
    path(r'register/chef/', views.ChefRegistrationViewSet.as_view({'post': 'create'})),
] 