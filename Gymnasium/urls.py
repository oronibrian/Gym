"""Gymnasium URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from members import views
from members import models
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token






router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet,'user')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('notifications/', include('notifications.urls')),
    path('reports/', include('reports.urls')),
    path('location/', include('GymLocation.urls')),
    path('api/', include(router.urls)),


    path('', include('accounts.urls'))
]

# for handling profile photos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
