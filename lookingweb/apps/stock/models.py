from django.db import models
from apps.user.models import Usuarios

# Create your models here.

class Inmueble(models.Model):
    """Model define los campos para Inmueble."""
    PROPERTY_TYPE =[
        ('0','Escoger...'),
        ('Alquiler','Alquiler'),
        ('Venta','Venta'),
        ('Campestre','Campestre'),
        ('Terrenos','Terrenos'),

    ]
    COUNTRY_CHOICES= [
        ('0','Escoger...'),
        ('COLOMBIA','Colombia'),
        ]
    DEPAR_CHOICES = [
                ('0','Escoger...'),
                ('AMAZONAS','Amazonas'),
                ('ANTIOQUIA','Antioquia'),
                ('ARAUCA','Arauca'),
                ('ATLANTICO','Atlantico'),
                ('BOLIVAR','Bolivar'),
                ('BOYACA','Boyaca'),
                ('CALDAS','Caldas'),
                ('CAQUETA','Caqueta'),
                ('CASANARE','Casanare'),
                ('CAUCA','Cauca'),
                ('CESAR','Cesar'),
                ('CHOCO','Choco'),
                ('CORDOBA','Cordoba'),
                ('CUNDINAMARCA','Cundinamarca'),
                ('GUAINIA','Guainia'),
                ('GUAVIARE','Guaviare'),
                ('HUILA','Huila'),
                ('GUAJIRA','La Guajira'),
                ('MAGDALENA','Magdalena'),
                ('META','Meta'),
                ('NARIÑO','Nariño'),
                ('N/SANTANDER','N/Santader'),
                ('PUTUMAYO','Putumayo'),
                ('QUINDIO','Quindio'),
                ('RISARALDA','Risaralda'),
                ('S/ANDRES','S/Andres y Providencia'),
                ('SANTANDER','Santader'),
                ('SUCRE','Sucre'),
                ('TOLIMA','Tolima'),
                ('VALLE','Valle'),
                ('VAUPES','Vaupes'),
                ('VICHADA','Vichada'),
        ]
    
    assignment      = models.ForeignKey   (Usuarios, null=True, blank=True, on_delete=models.CASCADE                                  )
    propertyName    = models.CharField    ('Nombre del inmueble' , max_length=100, blank=False, null=False                            )
    priceProperty   = models.DecimalField ('Precio de inmueble', max_digits=5, decimal_places=2, blank=False, null=False              )
    area            = models.DecimalField ('Area construida', max_digits=5, decimal_places=2, blank=False, null=False                 )
    addressProperty = models.CharField    ('Ubicacion', max_length=100, blank=False, null=False                                       )
    rooms           = models.IntegerField ('N° Habitaciones',default=1, blank=False, null=False                                       )
    bath            = models.IntegerField ('N° Baños',default=1, blank=False, null=False                                              )
    garage          = models.IntegerField ('N° Garajes',default=1, blank=False, null=False                                            )
    imagesRoom      = models.ImageField   ('Fotos de descripcion', upload_to='property/img', blank=False, null=False                  )
    typeProperty    = models.CharField    ('Tipo de Inmueble', max_length=50, choices=PROPERTY_TYPE, default="0"                                   )
    countryProperty = models.CharField    ('Pais/Region', max_length=50, choices=COUNTRY_CHOICES, blank=False, null=False, default="0")
    departProperty  = models.CharField    ('Departamento', max_length=50, choices=DEPAR_CHOICES, blank=False, null=False, default="0" )
    cityProperty    = models.CharField    ('Ciudad', max_length=100, blank=False, null=False, default=None                            )
    descrip         = models.TextField    (                                                                                           )

    class Meta:
        """Meta definicion Inmueble."""

        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'

    def __str__(self):
        """Unicode representation of Inmueble."""
        pass

