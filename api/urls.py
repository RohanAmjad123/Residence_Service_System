from . import views
from rest_framework import routers

router = routers.DefaultRouter()

# Register URL's for viewsets here.
router.register('students', views.StudentViewSet)
router.register('staff', views.StaffViewSet)
router.register('technicians', views.TechnicianViewSet)
router.register('admins', views.AdminViewSet)
router.register('chefs', views.ChefViewSet)
router.register('buildings', views.BuildingViewSet)
router.register('rooms', views.RoomViewSet)
router.register('maintreqs', views.MaintenanceRequestViewSet)

urlpatterns = router.urls