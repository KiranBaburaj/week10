# Generated by Django 5.0.2 on 2024-02-12 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
