# Generated by Django 3.1.1 on 2021-02-17 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyName', models.CharField(max_length=100, verbose_name='Nombre del inmueble')),
                ('priceProperty', models.FloatField(default=None, verbose_name='Precio de inmueble')),
                ('area', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Area construida')),
                ('addressProperty', models.CharField(max_length=100, verbose_name='Ubicacion')),
                ('rooms', models.IntegerField(default=1, verbose_name='N° Habitaciones')),
                ('bath', models.IntegerField(default=1, verbose_name='N° Baños')),
                ('garage', models.IntegerField(default=1, verbose_name='N° Garajes')),
                ('imagesRoom', models.ImageField(upload_to='source/property/img', verbose_name='Fotos de descripcion')),
                ('typeService', models.CharField(choices=[('Alquiler', 'Alquiler'), ('Venta', 'Venta')], default=None, max_length=50, verbose_name='Tipo de Servicio')),
                ('typeProperty', models.CharField(choices=[('Apartamentos', 'Apartamentos'), ('Oficinas', 'Oficinas '), ('Campestre', 'Campestre'), ('Terrenos', 'Terrenos')], default=None, max_length=50, verbose_name='Tipo de Inmueble')),
                ('countryProperty', models.CharField(choices=[('COLOMBIA', 'Colombia')], default=None, max_length=50, verbose_name='Pais/Region')),
                ('departProperty', models.CharField(choices=[('AMAZONAS', 'Amazonas'), ('ANTIOQUIA', 'Antioquia'), ('ARAUCA', 'Arauca'), ('ATLANTICO', 'Atlantico'), ('BOLIVAR', 'Bolivar'), ('BOYACA', 'Boyaca'), ('CALDAS', 'Caldas'), ('CAQUETA', 'Caqueta'), ('CASANARE', 'Casanare'), ('CAUCA', 'Cauca'), ('CESAR', 'Cesar'), ('CHOCO', 'Choco'), ('CORDOBA', 'Cordoba'), ('CUNDINAMARCA', 'Cundinamarca'), ('GUAINIA', 'Guainia'), ('GUAVIARE', 'Guaviare'), ('HUILA', 'Huila'), ('GUAJIRA', 'La Guajira'), ('MAGDALENA', 'Magdalena'), ('META', 'Meta'), ('NARIÑO', 'Nariño'), ('N/SANTANDER', 'N/Santader'), ('PUTUMAYO', 'Putumayo'), ('QUINDIO', 'Quindio'), ('RISARALDA', 'Risaralda'), ('S/ANDRES', 'S/Andres y Providencia'), ('SANTANDER', 'Santader'), ('SUCRE', 'Sucre'), ('TOLIMA', 'Tolima'), ('VALLE', 'Valle'), ('VAUPES', 'Vaupes'), ('VICHADA', 'Vichada')], default=None, max_length=50, verbose_name='Departamento')),
                ('cityProperty', models.CharField(default=None, max_length=100, verbose_name='Ciudad')),
                ('descrip', models.TextField()),
                ('usuario', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
            },
        ),
    ]
