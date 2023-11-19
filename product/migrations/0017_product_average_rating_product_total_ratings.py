# Generated by Django 4.2.6 on 2023-11-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_ratings',
            field=models.IntegerField(default=0),
        ),
    ]