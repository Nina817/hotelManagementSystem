# Generated by Django 3.2.6 on 2021-09-14 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0005_auto_20210913_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 14, 16, 7, 52, 392128)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 14, 17, 7, 52, 392219)),
        ),
    ]
