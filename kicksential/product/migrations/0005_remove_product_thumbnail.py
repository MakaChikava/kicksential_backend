# Generated by Django 4.2.7 on 2023-11-28 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
