from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SweetdaysViewSet, GiftSetViewSet, ReadyKitsViewSet, MacaronViewSet

# MacaronViewSet, MacaronSetViewSet, \
#     # MacaronSetItemViewSet


router = DefaultRouter()
router.register(r'sweetdays', SweetdaysViewSet)
router.register(r'giftsets', GiftSetViewSet)
router.register(r'readykits', ReadyKitsViewSet, basename='readykits')
router.register(r'macarons', MacaronViewSet)
# router.register(r'macaron-sets', MacaronSetViewSet)
# router.register(r'macaron-set-items', MacaronSetItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
