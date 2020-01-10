# Generated by Django 3.0.2 on 2020-01-10 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200109_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='items',
        ),
        migrations.AddField(
            model_name='auction',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.Item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=600),
        ),
    ]
