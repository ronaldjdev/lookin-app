# Generated by Django 3.1.1 on 2020-11-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='baños',
            field=models.IntegerField(default=1, verbose_name='N° Baños'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='garaje',
            field=models.IntegerField(default=1, verbose_name='N° Garajes'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='habitaciones',
            field=models.IntegerField(default=1, verbose_name='N° Habitaciones'),
        ),
    ]