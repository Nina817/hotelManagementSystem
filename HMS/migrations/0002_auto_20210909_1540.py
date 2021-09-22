# Generated by Django 3.2.6 on 2021-09-09 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='beds',
        ),
        migrations.RemoveField(
            model_name='room',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='room',
            name='category',
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 9, 15, 40, 24, 989730)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 9, 16, 40, 24, 989730)),
        ),
    ]