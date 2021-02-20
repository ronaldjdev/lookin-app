from django.db                  import models
from django.contrib.auth.models import User
#from apps.user.models import Usuarios

# Create your models here.

class Inmueble(models.Model):
    """Model define los campos para Inmueble."""
    SERVICE_TYPE   = [
        ('Alquiler','Alquiler'),
        ('Venta'   ,'Venta'   ),
    ]
    PROPERTY_TYPE  = [
        ('Apartamentos','Apartamentos'),
        ('Oficinas'    ,'Oficinas '   ),
        ('Campestre'   ,'Campestre'   ),
        ('Terrenos'    ,'Terrenos'    ),

    ]
    COUNTRY_CHOICES= [
        ('COLOMBIA','Colombia'),
    ]
    DEPAR_CHOICES  = [
        ('AMAZONAS'    ,'Amazonas'              ),
        ('ANTIOQUIA'   ,'Antioquia'             ),
        ('ARAUCA'      ,'Arauca'                ),
        ('ATLANTICO'   ,'Atlantico'             ),
        ('BOLIVAR'     ,'Bolivar'               ),
        ('BOYACA'      ,'Boyaca'                ),
        ('CALDAS'      ,'Caldas'                ),
        ('CAQUETA'     ,'Caqueta'               ),
        ('CASANARE'    ,'Casanare'              ),
        ('CAUCA'       ,'Cauca'                 ),
        ('CESAR'       ,'Cesar'                 ),
        ('CHOCO'       ,'Choco'                 ),
        ('CORDOBA'     ,'Cordoba'               ),
        ('CUNDINAMARCA','Cundinamarca'          ),
        ('GUAINIA'     ,'Guainia'               ),
        ('GUAVIARE'    ,'Guaviare'              ),
        ('HUILA'       ,'Huila'                 ),
        ('GUAJIRA'     ,'La Guajira'            ),
        ('MAGDALENA'   ,'Magdalena'             ),
        ('META'        ,'Meta'                  ),
        ('NARIÑO'      ,'Nariño'                ),
        ('N/SANTANDER' ,'N/Santader'            ),
        ('PUTUMAYO'    ,'Putumayo'              ),
        ('QUINDIO'     ,'Quindio'               ),
        ('RISARALDA'   ,'Risaralda'             ),
        ('S/ANDRES'    ,'S/Andres y Providencia'),
        ('SANTANDER'   ,'Santader'              ),
        ('SUCRE'       ,'Sucre'                 ),
        ('TOLIMA'      ,'Tolima'                ),
        ('VALLE'       ,'Valle'                 ),
        ('VAUPES'      ,'Vaupes'                ),
        ('VICHADA'     ,'Vichada'               ),
    ]
    

    usuario         = models.OneToOneField(User, null=True, blank=True, verbose_name='Usuario', on_delete=models.CASCADE, default=None, unique=True )
    propertyName    = models.CharField    ('Nombre del inmueble' , max_length=100, blank=False, null=False                                          )
    priceProperty   = models.FloatField   ('Precio de inmueble', default=None, blank=False, null=False                                              )
    area            = models.DecimalField ('Area construida', max_digits=5, decimal_places=2, blank=False, null=False                               )
    addressProperty = models.CharField    ('Ubicacion', max_length=100, blank=False, null=False                                                     )
    rooms           = models.IntegerField ('N° Habitaciones',default=1, blank=False, null=False                                                     )
    bath            = models.IntegerField ('N° Baños',default=1, blank=False, null=False                                                            )
    garage          = models.IntegerField ('N° Garajes',default=1, blank=False, null=False                                                          )
    imagesRoom      = models.ImageField   ('Fotos de descripcion', upload_to='source/property/img', blank=False, null=False                         )
    typeService     = models.CharField    ('Tipo de Servicio', max_length=50, choices=SERVICE_TYPE, blank=False, null=False, default=None           )
    typeProperty    = models.CharField    ('Tipo de Inmueble', max_length=50, choices=PROPERTY_TYPE, blank=False, null=False, default=None          )
    countryProperty = models.CharField    ('Pais/Region', max_length=50, choices=COUNTRY_CHOICES, blank=False, null=False,default=None              )
    departProperty  = models.CharField    ('Departamento', max_length=50, choices=DEPAR_CHOICES, blank=False, null=False, default=None              )
    cityProperty    = models.CharField    ('Ciudad', max_length=100, blank=False, null=False, default=None                                          )
    descrip         = models.TextField    (                                                                                                         )

    class Meta:
        """Meta definicion Inmueble."""

        verbose_name        = 'Inmueble'
        verbose_name_plural = 'Inmuebles'
        
    def __str__(self):
        return str(self.propertyName)
