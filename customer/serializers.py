from rest_framework import serializers
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    avatar_name = serializers.CharField(source='avatar', required=False, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

