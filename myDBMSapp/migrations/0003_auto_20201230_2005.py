# Generated by Django 3.1.4 on 2020-12-30 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDBMSapp', '0002_auto_20201230_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='register',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_messaged',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 30, 20, 5, 15, 282052)),
        ),
    ]
