
from rest_framework import viewsets
from . import models
from . import serializers


class KeywordsViewSet(viewsets.ModelViewSet):
    queryset = models.Keywords.objects.all()
    serializer_class = serializers.KeywordsSerializer
