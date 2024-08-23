from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from custom_auth.api.views import CustomTokenView, RegisterView

auth_urlpatterns = [
    path('token/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
