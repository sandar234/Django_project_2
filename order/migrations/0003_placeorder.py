# Generated by Django 4.2.6 on 2023-11-02 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_ordercart_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_list', models.JSONField(null=True)),
                ('order_number', models.CharField(max_length=50)),
                ('delivery_address', models.TextField(max_length=100)),
                ('invoice_address', models.TextField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
