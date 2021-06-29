from django.contrib.auth.models import User, Group
from rest_framework import serializers
from product.models import Product, ImageProduct


class ProductSerializer(serializers.ModelSerializer):
    imageProduct = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ('id', 'keyword', 'description', 'imageProduct', 'suplayer')


class ImageProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageProduct
        fields = '__all__'

