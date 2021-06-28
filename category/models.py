from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(
        auto_now_add=True,
    )

    name = models.TextField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image = models.FileField(
        upload_to='category/image',
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
