# Generated by Django 4.0.6 on 2022-08-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.CharField(max_length=80),
        ),
    ]
