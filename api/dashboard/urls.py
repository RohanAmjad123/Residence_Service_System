from django.urls import path
from .views import dashboard
from api.foodOrder.views import foodOrder

urlpatterns = [
    path('', dashboard, name ='dashboard'),
    path('foodOrder/', foodOrder, name='foodOrder')
]
