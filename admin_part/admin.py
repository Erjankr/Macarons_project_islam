from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'country', 'city', 'profile_image')
    search_fields = ('email', 'first_name', 'last_name', 'country', 'city')
    list_filter = ('country', 'city')

admin.site.register(UserProfile, UserProfileAdmin)
# Регистрация других моделей
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price')
    search_fields = ('name',)
    list_filter = ('price', 'discount_price')


@admin.register(PopularSet)
class PopularSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price')
    search_fields = ('name',)
    list_filter = ('price', 'discount_price')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price')
    search_fields = ('title',)
    list_filter = ('price', 'discount_price')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email', 'first_name',)

admin.site.register(CustomUser, CustomUserAdmin)
