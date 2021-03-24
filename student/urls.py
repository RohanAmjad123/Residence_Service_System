from rest_framework import routers
from .api import StudentViewSet

router = routers.DefaultRouter()
router.register('api/student', StudentViewSet, 'student')

urlpatterns = router.urls