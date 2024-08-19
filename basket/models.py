from django.db import models


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итоговая сумма")

    def __str__(self):
        return f"Корзина {self.id}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, verbose_name="Корзина")
    product_name = models.CharField(max_length=255, verbose_name="Название товара")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Скидка")

    def __str__(self):
        return f"{self.product_name} в корзине {self.cart.id}"

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
