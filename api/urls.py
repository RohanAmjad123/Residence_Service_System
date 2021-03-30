from . import views
from rest_framework import routers

router = routers.DefaultRouter()

# Register URL's for viewsets here.
router.register('students', views.StudentViewSet)
router.register('buildings', views.BuildingViewSet)
router.register('rooms', views.RoomViewSet)

urlpatterns = router.urls