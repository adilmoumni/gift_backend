
from rest_framework import viewsets
from . import models
from . import serializers


class SuplayerViewSet(viewsets.ModelViewSet):
    queryset = models.Suplayer.objects.all()
    serializer_class = serializers.SuplayerSerializer
