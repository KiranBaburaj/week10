# Generated by Django 5.0.1 on 2024-02-23 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_rating_unique_together_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_rating',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
