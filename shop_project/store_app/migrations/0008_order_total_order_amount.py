# Generated by Django 4.1.7 on 2023-03-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_order_payment_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_order_amount',
            field=models.IntegerField(default=500),
        ),
    ]