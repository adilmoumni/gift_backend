from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)

    firstName = models.TextField(
        null=False,
        blank=False
    )

    lastName = models.TextField(
        null=True,
        blank=False
    )

    email = models.TextField(
        null=False,
        blank=False
    )

    phone = models.TextField(
        null=False,
        blank=False
    )

    password = models.TextField(
        null=False,
        blank=False
    )

    adresse = models.TextField(
        null=True,
        blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
