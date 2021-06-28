
from rest_framework import viewsets
from . import models
from . import serializers

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends =(DjangoFilterBackend, SearchFilter)
    filter_fields = ('category',)

class ImageProductViewSet(viewsets.ModelViewSet):
    queryset = models.ImageProduct.objects.all()
    serializer_class = serializers.ImageProductSerializer
    filter_backends =(DjangoFilterBackend, SearchFilter)