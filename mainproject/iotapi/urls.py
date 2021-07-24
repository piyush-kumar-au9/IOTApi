from django.urls import include, path
from rest_framework import routers
from . import views
from .models import Devices
router = routers.DefaultRouter()
router.register(r'devices', views.DeviceViewSet, basename = Devices)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]