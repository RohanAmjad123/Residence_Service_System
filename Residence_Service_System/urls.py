from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from api.views import frontpage, signup
from django.contrib.auth import views

urlpatterns = [
    path('app/', include('api.dashboard.urls')),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', views.LoginView.as_view(template_name='residentSystem/login.html'), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
