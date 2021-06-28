from django.contrib.auth.models import User, Group
from rest_framework import serializers
from gift.models import Gift


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GiftSerializer(serializers.ModelSerializer):
    avatar_name = serializers.CharField(source='avatar', required=False, read_only=True)

    class Meta:
        model = Gift
        fields = '__all__'

