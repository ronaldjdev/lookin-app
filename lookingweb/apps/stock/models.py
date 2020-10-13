from django.db import models
from apps.user.models import Usuarios

# Create your models here.

class Inmueble(models.Model):
    """Model define los campos para Inmueble."""
    PROPERTY_TYPE =[
        ('Alquiler','Alquiler'),
        ('Venta','Venta'),
        ('Campestre','Campestre'),
        ('Terrenos','Terrenos'),

    ]

    inmueble = models.CharField('Nombre del inmueble', max_length=100, blank=False, null=False)
    precio = models.DecimalField('Precio de inmueble', max_digits=5, decimal_places=2, blank=False, null=False)
    area = models.DecimalField('Area construida', max_digits=5, decimal_places=2, blank=False, null=False)
    dirreccion = models.CharField('Ubicacion', max_length=100, blank=False, null=False)
    habitaciones = models.IntegerField(default=1, blank=False, null=False)
    baños = models.IntegerField(default=1, blank=False, null=False)
    garaje = models.IntegerField(default=1, blank=False, null=False)
    fotos = models.ImageField('Fotos de descripcion', upload_to='property/img', blank=False, null=False)
    tipoInmueble = models.CharField('Tipo de Inmueble', max_length=50, choices=PROPERTY_TYPE)
    pais = models.CharField('Pais/Region', max_length=50)
    descripcion = models.TextField()

    class Meta:
        """Meta definicion Inmueble."""

        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'

    def __str__(self):
        """Unicode representation of Inmueble."""
        pass

