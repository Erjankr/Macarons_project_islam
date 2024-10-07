from .models import GiftSet, Sweetdays
from .models import ReadyKits
from .models import Macaron


from rest_framework import serializers
from django.contrib.auth.models import User


class SweetdaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweetdays
        fields = '__all__'


class GiftSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftSet
        fields = '__all__'


class ReadyKitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyKits
        fields = ['id', 'name', 'image', 'description', 'price', 'available', 'in_cart']


class MacaronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macaron
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

