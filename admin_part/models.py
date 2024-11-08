from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование товара")
    short_description = models.CharField(max_length=500, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена со скидкой")
    description = models.TextField(verbose_name="Описание продукта")
    file = models.FileField(upload_to='products/', verbose_name="Файл")

    class Meta:
        verbose_name = "Акции"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.name


class PopularSet(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование товара")
    short_description = models.CharField(max_length=500, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена со скидкой")
    description = models.TextField(verbose_name="Описание продукта")
    file = models.FileField(upload_to='popularSet/', verbose_name="Файл")

    class Meta:
        verbose_name = "Популярный набор"
        verbose_name_plural = "Популярные наборы"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование товара")
    short_description = models.CharField(max_length=500, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена со скидкой", null=True, blank=True)
    description = models.TextField(verbose_name="Описание продукта")
    file = models.FileField(upload_to='news_files/', verbose_name="Файл")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна", blank=True)
    city = models.CharField(max_length=100, verbose_name="Город", blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', verbose_name="Профильное изображение", null=True, blank=True)
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Создание обычного пользователя"""
        if not email:
            raise ValueError("Email должен быть указан")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создание суперпользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    activation_code_created_at = models.DateTimeField(null=True, blank=True)  # Время генерации кода
    reset_code = models.CharField(max_length=100, blank=True, null=True)  # Добавьте это поле
    activation_code = models.CharField(max_length=4, blank=True, null=True)
    is_staff = models.BooleanField(default=False, verbose_name="Администратор")  # Поле для определения роли администратора

    USERNAME_FIELD = 'email'  # Поле для логина
    REQUIRED_FIELDS = []  # Удалите 'email' из REQUIRED_FIELDS
    objects = CustomUserManager()
