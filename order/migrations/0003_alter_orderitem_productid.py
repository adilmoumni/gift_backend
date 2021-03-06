# Generated by Django 3.2.4 on 2021-06-30 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_suplayer'),
        ('order', '0002_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderFK', to='product.product', unique=True, verbose_name='product'),
        ),
    ]
