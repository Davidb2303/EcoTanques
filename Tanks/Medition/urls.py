from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicionViewSet

router = DefaultRouter()
router.register(r'mediciones', MedicionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
