# Generated by Django 4.2.9 on 2024-01-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_remove_product_parent_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
