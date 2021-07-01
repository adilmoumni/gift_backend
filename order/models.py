from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)

    OrderNumber = models.CharField(max_length=100, null=False, blank=False)

    OrderDate = models.DateTimeField(auto_now_add=True)

    TotalAmount = models.DecimalField(max_digits=5, decimal_places=2)

    AdresseLivraison = models.TextField(null=True, blank=False)

    Note = models.TextField(null=True, blank=False)

    ModePaiement = models.TextField(null=True, blank=False)

    datePrevueLivraison = models.DateTimeField()

    isCancled = models.BooleanField(null=True)

    lastName = models.TextField(null=True, blank=False)

    email = models.TextField(null=False, blank=False)

    phone = models.TextField(null=False, blank=False)

    password = models.TextField(null=False, blank=False)

    adresse = models.TextField(null=True, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    orderId = models.ForeignKey('order',
                                unique=True,
                                verbose_name=''
                                             '',
                                related_name='orderFK',
                                on_delete=models.CASCADE)

    productId = models.ForeignKey('product.Product',
                                  unique=True,
                                  verbose_name='product',
                                  related_name='orderFK',
                                  on_delete=models.CASCADE,
                                  )
    UnitPrice = models.DecimalField(max_digits=5, decimal_places=2)

    Quantity = models.IntegerField()

    def __str__(self):
        return self.id
