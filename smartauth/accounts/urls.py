# accounts/urls.py
from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]


# accounts/urls.py
from .views import HRDashboardView, AdminDashboardView

urlpatterns += [
    path('hr/dashboard/', HRDashboardView.as_view(), name='hr-dashboard'),
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
]
