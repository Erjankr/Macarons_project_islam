from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компонента')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.name} ({self.quantity} шт)"

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'

