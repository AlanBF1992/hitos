# Generated by Django 4.0.6 on 2022-08-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0002_alter_region_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmuebles',
            name='m2_terreno',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]