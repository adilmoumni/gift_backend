# Generated by Django 3.2.4 on 2021-06-29 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210627_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='image'),
        ),
    ]