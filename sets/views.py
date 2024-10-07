from rest_framework import viewsets
from .models import SelectTheQuantity, ChooseYourTastes, Additional
from .serializers import SelectTheQuantitySerializer, ChooseYourTastesSerializer, AdditionalSerializer


class SelectTheQuantityViewSet(viewsets.ModelViewSet):
    queryset = SelectTheQuantity.objects.all()
    serializer_class = SelectTheQuantitySerializer


class ChooseYourTastesViewSet(viewsets.ModelViewSet):
    queryset = ChooseYourTastes.objects.all()
    serializer_class = ChooseYourTastesSerializer


class AdditionalViewSet(viewsets.ModelViewSet):
    queryset = Additional.objects.all()
    serializer_class = AdditionalSerializer
