# Generated by Django 4.2.1 on 2023-05-30 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_customuser_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 12, 5, 57, 961595, tzinfo=datetime.timezone.utc)),
        ),
    ]
