# Generated by Django 5.0.2 on 2024-03-18 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_referralcoupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='available_quantity',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='is_first_purchase_coupon',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='max_usage_count',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='usage_count',
        ),
    ]
