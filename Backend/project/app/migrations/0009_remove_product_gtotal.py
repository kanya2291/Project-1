# Generated by Django 4.2.4 on 2023-08-25 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_gtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='gtotal',
        ),
    ]