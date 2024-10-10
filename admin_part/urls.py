from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import *
# Создаем экземпляр маршрутизатора
urlpatterns = [
    path('products/', Product.as_view(), name='product-list-create'),  # Вьюха для работы с продуктами
    path('popular-sets/', Popular.as_view(), name='popular-set-list-create'),  # Вьюха для работы с популярными наборами
    path('news/', News.as_view(), name='news-list-create'),  # Вьюха для работы с новостями
# Включаем маршруты из роутера
    path('register/', AdminRegistrationView.as_view(), name='admin_register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset-password-verify/', ResetPasswordVerifyView.as_view(), name='reset_password_verify'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('profiles/', UserProfileListCreateView.as_view(), name='user_profiles'),  # Для списка и создания
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),

    # Маршрут для входа
]
