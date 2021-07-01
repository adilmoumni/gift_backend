from django.contrib.auth.models import User, Group
from rest_framework import serializers
from favored.models import Favored


class FavoredSerializer(serializers.ModelSerializer):
    avatar_name = serializers.CharField(source='avatar', required=False, read_only=True)

    class Meta:
        model = Favored
        fields = '__all__'

