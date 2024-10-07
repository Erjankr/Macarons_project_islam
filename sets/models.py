from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class SelectTheQuantity(models.Model):
    quantity = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, verbose_name='изображение')
    price = models.CharField(max_length=100)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = 'Выберите количество'
        verbose_name_plural = 'Выберите количество'


class ChooseYourTastes(models.Model):
    the_name_of_the_taste = models.CharField(max_length=100, verbose_name='Название вкуса')
    image = models.ImageField(null=True, blank=True, verbose_name='изображение')
    description = models.TextField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return self.the_name_of_the_taste

    class Meta:
        verbose_name = 'Выберите вкус'
        verbose_name_plural = 'Выберите вкус'


class Additional(models.Model):
    title = models.CharField(max_length=190, verbose_name='Название')
    image = models.ImageField(null=True, blank=True, verbose_name='изображение')
    price = models.CharField(max_length=100, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительное'
        verbose_name_plural = 'Дополнительные'

