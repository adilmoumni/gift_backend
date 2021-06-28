# Generated by Django 3.2.4 on 2021-06-27 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0002_auto_20210627_1417'),
        ('product', '0002_auto_20210627_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='keyword',
            field=models.ManyToManyField(to='keywords.Keywords'),
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(blank=True, upload_to='product/image')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='Idea Status')),
            ],
        ),
    ]
