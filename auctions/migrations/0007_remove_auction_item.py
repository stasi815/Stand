# Generated by Django 3.0.2 on 2020-01-10 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200109_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='item',
        ),
    ]