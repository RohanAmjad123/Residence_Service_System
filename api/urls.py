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
router.register('resolves', views.ResolvesViewSet)
router.register('complaints', views.ComplaintViewSet)
router.register('foodorders', views.FoodOrderViewSet)
router.register('fulfills', views.FulfillsViewSet)
router.register('packages', views.PackageViewSet)
router.register('student/register', views.StudentRegistrationViewSet)
router.register('staff/register', views.StaffRegistrationViewSet)
router.register('technician/register', views.TechnicianRegistrationViewSet)
router.register('admin/register', views.AdminRegistrationViewSet)
router.register('chef/register', views.ChefRegistrationViewSet)

urlpatterns = router.urls 