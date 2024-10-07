from django.db import models


class Sweetdays(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    information = models.TextField(verbose_name='Информация')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    buy = models.BooleanField(default=False, verbose_name='Купить')
    in_cart = models.BooleanField(default=False, verbose_name='В корзине')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сладкие Дни'
        verbose_name_plural = 'Сладкие Дни'


class GiftSet(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    in_cart = models.BooleanField(default=False, verbose_name='В корзине')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подарочный набор'
        verbose_name_plural = 'Подарочные наборы'


class ReadyKits(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    in_cart = models.BooleanField(default=False, verbose_name='В корзине')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Готовые наборы'
        verbose_name_plural = 'Готовые наборы'




class Macaron(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Макарон"
        verbose_name_plural = "Макароны"

# #
# class MacaronSet(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Название набора")
#     macarons = models.ManyToManyField('Macaron', through='MacaronSetItem', verbose_name="Собрать наборы")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Собрать наборы"
#         verbose_name_plural = "Собрать наборы"
#
#
# class MacaronSetItem(models.Model):
#     macaron_set = models.ForeignKey(MacaronSet, on_delete=models.CASCADE, verbose_name="Набор")
#     macaron = models.ForeignKey(Macaron, on_delete=models.CASCADE, verbose_name="Собрать наборы")
#     quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
#
#     def __str__(self):
#         return f"{self.macaron.name} x {self.quantity}"
#
#     class Meta:
#         verbose_name = "Элемент набора собрать наборы"
#         verbose_name_plural = "Элементы наборов собрать наборы"
