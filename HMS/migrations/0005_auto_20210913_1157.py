# Generated by Django 3.2.6 on 2021-09-13 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0004_auto_20210909_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 13, 11, 57, 14, 749428)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 13, 12, 57, 14, 749428)),
        ),
    ]
