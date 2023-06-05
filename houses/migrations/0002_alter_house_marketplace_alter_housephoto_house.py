# Generated by Django 4.2.1 on 2023-05-15 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marketplace', to='houses.marketplace'),
        ),
        migrations.AlterField(
            model_name='housephoto',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='photos', to='houses.house'),
        ),
    ]