# Generated by Django 4.2.9 on 2024-01-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_remove_product_subcategory_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parent_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='cms.category'),
        ),
    ]
