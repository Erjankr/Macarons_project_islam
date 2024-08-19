from django.db import models


class Order(models.Model):
    DELIVERY_CHOICES = [
        ('courier', 'Курьерская доставка'),
        ('pickup', 'Самовывоз'),
    ]

    PAYMENT_CHOICES = [
        ('online', 'Оплата картой онлайн'),
        ('cash_on_delivery', 'Наличными при получении'),
        ('yandex_money', 'Яндекс деньги'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name="Ваше имя"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Ваш телефон"
    )
    delivery_method = models.CharField(
        max_length=10,
        choices=DELIVERY_CHOICES,
        verbose_name="Способ доставки"
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Адрес доставки"
    )
    delivery_date = models.DateField(
        verbose_name="Дата получения"
    )
    delivery_time = models.TimeField(
        verbose_name="Время"
    )
    comments = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Комментарии к заказу"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        verbose_name="Метод оплаты"
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Итоговая сумма заказа вместе с доставкой"
    )

    def __str__(self):
        return f"Заказ {self.id} - {self.name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
