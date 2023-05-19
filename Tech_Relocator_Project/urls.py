from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect URL
    path('', lambda req: redirect('api/v1/users/')),

    # DRF URLS
    path('api/v1/users/', include('user_profile.urls')),
    path('api-auth', include("rest_framework.urls")),

    # JWT URLS
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]