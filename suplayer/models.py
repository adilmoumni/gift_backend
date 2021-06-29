from django.db import models


class Suplayer(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(
        null=False,
        blank=False
    )

    phone = models.TextField(
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
