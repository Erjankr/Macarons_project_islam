from rest_framework import serializers
from .models import *
import logging
from django.contrib.auth import authenticate  # Импортируем authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
# Логгер для отслеживания событий
logger = logging.getLogger(__name__)

# Сериализатор для модели Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        ref_name = 'ProductSerializer'  # Уникальное имя для схемы

# Сериализатор для модели PopularSet
class PopularSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularSet
        fields = '__all__'
        ref_name = 'PopularSetSerializer'  # Уникальное имя для схемы

# Сериализатор для модели News
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        ref_name = 'NewsSerializer'  # Уникальное имя для схемы

# Сериализатор для профиля пользователя
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'country', 'city', 'profile_image')  # Укажите нужные поля
        ref_name = 'UserProfileSerializer'  # Уникальное имя для схемы

class AdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        # Проверяем, совпадают ли пароли
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})

        # Удаляем confirm_password из validated_data
        validated_data.pop('confirm_password')

        # Хешируем пароль перед сохранением
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_staff'] = True  # Устанавливаем пользователя как администратора

        # Создаем нового пользователя
        user = CustomUser(**validated_data)
        user.save()
        return user

    def validate_email(self, value):
        # Проверяем, существует ли уже пользователь с таким email
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Неверный логин или пароль.")
        return {'user': user}

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordVerifySerializer(serializers.Serializer):
    reset_code = serializers.CharField(max_length=100)



class CreateNewPasswordSerializer(serializers.Serializer):
    """
    Сериализатор для создания нового пароля с подтверждением.
    Поля:
    - `password`: Новый пароль пользователя.
    - `confirm_password`: Поле для повторного ввода пароля, чтобы подтвердить его.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        max_length=128,
        help_text="Введите новый пароль."
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Повторите новый пароль для подтверждения."
    )

    def validate(self, data):
        """
        Проверяем, совпадают ли пароли в полях `password` и `confirm_password`.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

        
        
