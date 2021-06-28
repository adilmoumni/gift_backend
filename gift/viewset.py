from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from . import models
from . import serializers


class GiftViewSet(viewsets.ModelViewSet):
    queryset = models.Gift.objects.all()
    serializer_class = serializers.GiftSerializer

