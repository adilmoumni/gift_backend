from django.db import models


class Keywords(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(
        null=False,
        blank=False
    )

    date = models.DateField(
        auto_now_add=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
