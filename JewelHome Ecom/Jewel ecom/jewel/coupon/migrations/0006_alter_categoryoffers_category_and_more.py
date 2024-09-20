# Generated by Django 5.0.2 on 2024-03-23 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0005_categoryoffers_productoffers'),
        ('product', '0018_alter_rating_unique_together_remove_rating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryoffers',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='product.category'),
        ),
        migrations.AlterField(
            model_name='productoffers',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='product.products'),
        ),
    ]