from django.db import models
from category.models import Category
from keywords.models import Keywords


class Product(models.Model):
    id = models.AutoField(primary_key=True)

    category = models.ManyToManyField(Category)

    keyword = models.ManyToManyField(Keywords)

    name = models.TextField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    date = models.DateField(
        auto_now_add=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ImageProduct(models.Model):
    id = models.AutoField(primary_key=True)

    image = models.FileField(
        upload_to='product/image',
        blank=True,
    )

    product = models.ForeignKey('product',
                                verbose_name='image',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)

    def __str__(self):
        return self.name
