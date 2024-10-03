from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import *
# Создаем экземпляр маршрутизатора
router = DefaultRouter()

# Регистрируем вьюхи в маршрутизаторе
router.register(r'promotion', ProductViewSet, basename='promotion')
router.register(r'popular-sets', PopularSetViewSet, basename='popular-set')
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [ # Включаем маршруты из роутера
    path('register/', AdminRegistrationView.as_view(), name='admin_register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset-password-verify/', ResetPasswordVerifyView.as_view(), name='reset_password_verify'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('profiles/', UserProfileListCreateView.as_view(), name='user_profiles'),  # Для списка и создания
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),

    # Маршрут для входа
]
