# Generated by Django 5.0.2 on 2024-02-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_cart_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]