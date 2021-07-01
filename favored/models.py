from django.db import models


class Favored(models.Model):
    customer = models.ForeignKey('customer.Customer',
                                 unique=True,
                                 verbose_name='customer',
                                 related_name='customer',
                                 on_delete=models.CASCADE,
                                )

    product = models.ForeignKey('product.Product',
                                unique=True,
                                verbose_name='product',
                                related_name='product',
                                on_delete=models.CASCADE,
                               )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
