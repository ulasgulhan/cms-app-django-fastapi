# Generated by Django 4.2.9 on 2024-01-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_cart_cartitem_cart_products_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='is_active',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive'), ('Modified', 'Modified')], default='Active', max_length=100),
        ),
    ]