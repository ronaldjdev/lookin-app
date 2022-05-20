from django.db                  import models
from django.contrib.auth.models import User
from django.urls.base import reverse, reverse_lazy




class Usuarios (models.Model):
    GENDER_TYPE_CHOICES=[
        ('0'     ,'No Especifica'),
        ('HOMBRE','Hombre'       ),
        ('MUJER' ,'Mujer'        ),
        ('OTROS' ,'Otros'        ),
    ]
    COUNTRY_CHOICES= [
        ('0'       ,'Escoger...'),
        ('COLOMBIA','Colombia'  ),
    ]
    DEPAR_CHOICES = [
        ('0'           ,'Escoger...'            ),
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


    usuario    = models.OneToOneField           (User, null=True, blank=True, verbose_name='Usuario',on_delete=models.CASCADE, default=None, unique=True )
    address    = models.CharField               ('Ciudad' , max_length            = 50, blank=False, null=False, default=""                              )
    streets    = models.CharField               ('Barrio' , max_length            = 50, blank=True, default=""                                           )
    numIden    = models.PositiveBigIntegerField ('N° de Identificacion' , blank   =False, null=False, unique=True, default=None                          )
    numPhone   = models.PositiveBigIntegerField ('N° de Telefono' , default       = "0"                                                                  )
    country    = models.CharField               ('Pais' , max_length              = 50, choices=COUNTRY_CHOICES, blank=False, null=False, default=""     )
    depart     = models.CharField               ('Departamento' , max_length      = 50, choices=DEPAR_CHOICES, blank=False, null=False, default="0"      )
    gender     = models.CharField               ('Tipo de Genero' , max_length    = 50, choices=GENDER_TYPE_CHOICES, blank=False, null=False, default="0")
    profileImg = models.ImageField              ('Imagen de Perfil' , upload_to   = 'source/profile/img/', blank=True, null=True                         )
    regisDate  = models.DateField               ('Fecha de Registro' , auto_now   = False, auto_now_add=True                                             )
    postal     = models.IntegerField            ('Codigo Postal' , default        = 0                                                                    )
    birthday   = models.DateField               ('Fecha de Nacimiento' , auto_now =False, auto_now_add=False, blank=False, null=False, default=None      )

    class Meta:
        verbose_name        = 'Tabla de perfil'
        verbose_name_plural = 'Tabla de perfiles'

    def __str__(self) -> str:
        return str(self.usuario)

    def get_absolute_url(self):
        return reverse('users', kwargs={'pk': self.pk})