from rest_framework import serializers
from .models import SelectTheQuantity, ChooseYourTastes, Additional


class SelectTheQuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = SelectTheQuantity
        fields = ['id', 'quantity', 'image', 'price']


class ChooseYourTastesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseYourTastes
        fields = ['id', 'the_name_of_the_taste', 'image', 'description']


class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional
        fields = ['id', 'title', 'image', 'price']
