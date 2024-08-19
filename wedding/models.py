from django.db import models


class Wedding(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    in_cart = models.BooleanField(default=False, verbose_name='В корзине')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Свадьба'
        verbose_name_plural = 'Свадьбы'
