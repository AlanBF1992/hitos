# Generated by Django 4.0.6 on 2022-08-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0006_alter_inmuebles_numero_banos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmuebles',
            name='nombre_inmueble',
            field=models.CharField(max_length=200),
        ),
    ]
