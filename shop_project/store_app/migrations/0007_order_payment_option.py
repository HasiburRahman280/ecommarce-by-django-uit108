# Generated by Django 4.1.7 on 2023-03-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_option',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
