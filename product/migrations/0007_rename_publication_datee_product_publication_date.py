# Generated by Django 4.2.6 on 2023-10-20 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_publication_date_product_publication_datee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='publication_datee',
            new_name='publication_date',
        ),
    ]
