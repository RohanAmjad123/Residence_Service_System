from . import views
from rest_framework import routers
from rest_framework_nested import routers
from django.urls import path
from django.urls import include

router = routers.SimpleRouter()

# Register URL's for viewsets here.

router.register('students', views.StudentViewSet)
router.register('staff', views.StaffViewSet)
router.register('technicians', views.TechnicianViewSet)
router.register('admins', views.AdminViewSet)
router.register('chefs', views.ChefViewSet)
router.register('buildings', views.BuildingViewSet)
router.register('maintreqs', views.MaintenanceRequestViewSet)
router.register('complaints', views.ComplaintViewSet)
router.register('foodorders', views.FoodOrderViewSet)
router.register('packages', views.PackageViewSet)

resolves_router = routers.NestedSimpleRouter(router, 'maintreqs', lookup='maintreq')
resolves_router.register('resolves', views.ResolvesViewSet, basename='maintreq-resolves')

rooms_router = routers.NestedSimpleRouter(router, 'buildings', lookup='building')
rooms_router.register('rooms', views.RoomViewSet, basename='building-rooms')

fulfills_router = routers.NestedSimpleRouter(router, 'foodorders', lookup='foodorder')
fulfills_router.register('fulfills', views.FulfillsViewSet, basename='foodorder-fulfills')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(resolves_router.urls)),
    path('', include(rooms_router.urls)),
    path('', include(fulfills_router.urls))
]