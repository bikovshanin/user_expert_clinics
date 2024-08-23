from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from custom_auth.api.urls import auth_urlpatterns
from users.api.urls import users_urlpatterns

v1_urls = [
    path('users/', include((users_urlpatterns, 'users'))),
    path('auth/', include((auth_urlpatterns, 'custom_auth'))),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_urls)),
    path(
        'redoc/',
        TemplateView.as_view(
            template_name='redoc.html',
        ), name='redoc'
    ),
]
