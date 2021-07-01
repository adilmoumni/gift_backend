
from rest_framework import viewsets
from . import models
from . import serializers


class FavoredViewSet(viewsets.ModelViewSet):
    queryset = models.Favored.objects.all()
    serializer_class = serializers.FavoredSerializer
