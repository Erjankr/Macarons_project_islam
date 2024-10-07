from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'select-the-quantity', SelectTheQuantityViewSet)
router.register(r'choose-your-tastes', ChooseYourTastesViewSet)
router.register(r'additional', AdditionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]