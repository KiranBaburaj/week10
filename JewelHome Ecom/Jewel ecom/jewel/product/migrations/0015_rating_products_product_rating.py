# Generated by Django 5.0.1 on 2024-02-23 07:40

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_remove_products_product_rating_delete_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('product', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='product_ratings', to='product.products')),
                ('user', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('product', 'user')},
            },
        ),
        migrations.AddField(
            model_name='products',
            name='product_rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.rating'),
        ),
    ]