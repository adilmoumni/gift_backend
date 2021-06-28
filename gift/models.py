from django.db import models


# Create your models here.

class Gift(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(
        auto_now_add=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.TextField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )
    files = models.FileField(
        upload_to='gift',
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=False,
        blank=False,
        default=""
    )
    app_url = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
