# Generated by Django 3.1.1 on 2020-10-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201001_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='regisDate',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Registro'),
        ),
    ]