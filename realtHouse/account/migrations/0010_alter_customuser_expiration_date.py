# Generated by Django 4.2.1 on 2023-05-15 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_customuser_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 12, 17, 50, 531221, tzinfo=datetime.timezone.utc)),
        ),
    ]
