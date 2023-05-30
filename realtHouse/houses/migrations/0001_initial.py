# Generated by Django 4.2.1 on 2023-05-11 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountusd', models.SmallIntegerField(blank=True, db_column='amountUSD', null=True)),
                ('amountbyn', models.SmallIntegerField(blank=True, db_column='amountBYN', null=True)),
                ('rent_rooms', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('address', models.CharField(blank=True, default='Minsk', null=True)),
                ('url', models.CharField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('agency', models.BooleanField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('location_a', models.CharField(blank=True, null=True)),
                ('location_b', models.CharField(blank=True, null=True)),
                ('phoneNumber', models.CharField(blank=True, db_column='phoneNumber', null=True)),
            ],
            options={
                'db_table': 'house',
            },
        ),
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'marketplace',
            },
        ),
        migrations.CreateModel(
            name='HousePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, null=True, unique=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='houses.house')),
            ],
            options={
                'db_table': 'house_photo',
            },
        ),
        migrations.AddField(
            model_name='house',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.marketplace'),
        ),
    ]
