from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import GiftSet, Macaron
from .serializers import GiftSetSerializer
from .models import Sweetdays
from .serializers import SweetdaysSerializer
from .models import ReadyKits
from .serializers import ReadyKitsSerializer
# from .models import Macaron, MacaronSet, MacaronSetItem
from .serializers import MacaronSerializer


class SweetdaysViewSet(viewsets.ModelViewSet):
    queryset = Sweetdays.objects.all()
    serializer_class = SweetdaysSerializer


class GiftSetViewSet(viewsets.ModelViewSet):
    queryset = GiftSet.objects.all()
    serializer_class = GiftSetSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'name': ['icontains'],
        'price': ['exact', 'gte', 'lte'],
        'available': ['exact'],
    }


class ReadyKitsViewSet(viewsets.ModelViewSet):
    queryset = ReadyKits.objects.all()
    serializer_class = ReadyKitsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'name': ['icontains'],
        'price': ['exact', 'gte', 'lte'],
        'available': ['exact'],
        'in_cart': ['exact'],
    }


class MacaronViewSet(viewsets.ModelViewSet):
    queryset = Macaron.objects.all()
    serializer_class = MacaronSerializer
#
#
# class MacaronSetViewSet(viewsets.ModelViewSet):
#     queryset = MacaronSet.objects.all()
#     serializer_class = MacaronSetSerializer
#
#
# class MacaronSetItemViewSet(viewsets.ModelViewSet):
#     queryset = MacaronSetItem.objects.all()
#     serializer_class = MacaronSetItemSerializer
