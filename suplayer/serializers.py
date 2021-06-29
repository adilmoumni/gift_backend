from rest_framework import serializers
from suplayer.models import Suplayer


class SuplayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suplayer
        fields = '__all__'

