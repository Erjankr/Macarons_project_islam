from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
import logging
import random
import string
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
logger = logging.getLogger(__name__)

# Вьюха для работы с продуктами
class Product(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Вьюха для работы с популярными наборами
class Popular(generics.ListCreateAPIView):
    queryset = PopularSet.objects.all()
    serializer_class = PopularSetSerializer

# Вьюха для работы с новостями
class News(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


# Пример другого представления
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        # Вы можете добавить дополнительную логику перед сохранением нового профиля, если необходимо
        serializer.save()

def generate_reset_code(length=4):
    """Генерирует случайный цифровой код для сброса пароля."""
    return ''.join(random.choices(string.digits, k=length))


class AdminRegistrationView(generics.CreateAPIView):
    """View для регистрации нового администратора."""
    serializer_class = AdminRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'response': False,
                'message': _('Ошибка валидации данных'),
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'response': True,
            'message': _('Регистрация администратора успешна'),
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class UserLoginView(generics.CreateAPIView):
    """Аутентификация пользователя."""
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        if user is None:
            return Response({
                'response': False,
                'message': 'Неверный логин или пароль.'
            }, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'response': True,
            'token': token.key
        }, status=status.HTTP_200_OK)


class ResetPasswordView(generics.GenericAPIView):
    """Запрос на сброс пароля."""
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = CustomUser.objects.get(email=email)
            reset_code = generate_reset_code()  # Генерация кода сброса пароля
            user.reset_code = reset_code
            user.save()

            message = (
                f"Здравствуйте, {user.email}!\n\n"
                f"<p>{_('Ваш код активации')}: {reset_code}</p>"
                f"Ваш код для восстановления пароля: {reset_code}\n\n"
                f"С наилучшими пожеланиями,\nКоманда {settings.BASE_URL}"
            )
            send_mail(
                _('Восстановление пароля'),
                '',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
                html_message=message,
            )

            return Response({
                'response': True,
                'message': _('Письмо с инструкциями по восстановлению пароля было отправлено на ваш email.')
            })

        except CustomUser.DoesNotExist:
            return Response({
                'response': False,
                'message': _('Пользователь с этим адресом электронной почты не найден.')
            }, status=status.HTTP_404_NOT_FOUND)


class ResetPasswordVerifyView(generics.GenericAPIView):
    """Подтверждение сброса пароля."""
    serializer_class = ResetPasswordVerifySerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reset_code = serializer.validated_data['reset_code']

        try:
            user = CustomUser.objects.get(reset_code=reset_code)
            user.reset_code = ''  # Очищаем код сброса после подтверждения
            user.save()

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'response': True,
                'message': _('Пароль успешно сброшен'),
            }, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            logger.error(f"User with reset_code {reset_code} does not exist.")
            return Response({
                'response': False,
                'message': _('Неверный код для сброса пароля.')
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Error in ResetPasswordVerifyView: {str(e)}")
            return Response({
                'response': False,
                'message': _('Произошла ошибка при сбросе пароля.')
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChangePasswordView(generics.UpdateAPIView):
    """Представление для смены пароля."""
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = request.user  # Получаем текущего аутентифицированного пользователя
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({
                'response': True,
                'message': _('Пароль успешно изменен.')
            }, status=status.HTTP_200_OK)
        return Response({
            'response': False,
            'message': _('Ошибка при изменении пароля.'),
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)