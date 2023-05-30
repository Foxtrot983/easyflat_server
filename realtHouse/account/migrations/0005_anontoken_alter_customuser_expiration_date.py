# Generated by Django 4.2.1 on 2023-05-11 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_expiration_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(unique=True)),
                ('exp_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 12, 14, 12, 323496, tzinfo=datetime.timezone.utc)),
        ),
    ]
