# Generated by Django 4.1.7 on 2023-02-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='BannerImage')),
                ('http_link', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
