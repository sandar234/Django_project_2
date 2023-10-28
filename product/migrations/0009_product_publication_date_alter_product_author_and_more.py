# Generated by Django 4.2.6 on 2023-10-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_product_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publication_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimensions_height',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimensions_length',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='language',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='publisher',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='recommended_age',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
