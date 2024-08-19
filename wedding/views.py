from rest_framework import viewsets
from .models import Wedding
from .serializes import WeddingSerializer


class WeddingViewSet(viewsets.ModelViewSet):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer
