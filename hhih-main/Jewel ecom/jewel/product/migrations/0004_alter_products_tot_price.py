# Generated by Django 5.0.1 on 2024-02-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_products_tot_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tot_price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=15),
        ),
    ]
