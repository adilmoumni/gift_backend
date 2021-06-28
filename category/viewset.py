
from rest_framework import viewsets
from . import models
from . import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
