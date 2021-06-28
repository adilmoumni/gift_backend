from django.contrib.auth.models import User, Group
from rest_framework import serializers
from keywords.models import Keywords


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class KeywordsSerializer(serializers.ModelSerializer):
    avatar_name = serializers.CharField(source='avatar', required=False, read_only=True)

    class Meta:
        model = Keywords
        fields = '__all__'

