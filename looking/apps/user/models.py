from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Importante: Creamos el manager que se comunica y hace la traduccion SQL
class UserManager (BaseUserManager):
    'Metodo que crea usuarios generales'
    def create_user(self,email,username,firstName,lastName,numIden,address,address2,country,gender,depart,password):
        if not email or not username:
            raise ValueError('Este campo es requerido')
    
        user= self.model(
            email = self.normalize_email(email),
            username = username,
            firstName = firstName,
            lastName = lastName,
            numIden = numIden,
            address = address,
            address2 = address2,
            country = country,
            gender = gender,
            depart = depart,
            password = password
        )

        user.set_password(password)
        user.save()
        return user

    # Metodo que crea super usuarios
    def create_superuser(self,email,username,firstName,lastName,numIden,address,password):
        user=self.create_user(
            email,
            username = username,
            firstName = firstName,
            lastName = lastName,
            numIden = numIden,
            address = address,
            password = password
            
        )
        user.admUser=True
        user.save()
        return user
    




# Modelo que crea las tablas en la base de datos:
class Usuarios (AbstractBaseUser):
    GENDER_TYPE_CHOICES=[
        ('0','No Especifica'),
        ('HOMBRE','Hombre'),
        ('MUJER','Mujer'),
        ('OTROS','Otros'),
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


    username = models.CharField('Nombre de Usuario', max_length=50, unique=True)
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    firstName = models.CharField('Nombre', max_length=50, blank=False, null=False, default="" )
    lastName = models.CharField('Apellidos', max_length=50, blank=False, null=False, default="")
    address = models.CharField('Ciudad', max_length=50, blank=False, null=False, default="")
    address2 = models.CharField('Barrio', max_length=50, blank=True, null=True, default="")
    numIden = models.CharField('N° de Identificacion', max_length=50, blank=False, null=False, unique=True, default="")
    country = models.CharField('Pais', max_length=50, choices=COUNTRY_CHOICES, blank=False, null=False, default="0")
    depart = models.CharField('Departamento', max_length=50, choices=DEPAR_CHOICES, blank=False, null=False, default="0")
    gender = models.CharField('Tipo de Genero', max_length=50, choices=GENDER_TYPE_CHOICES,  blank=False, null=False, default="0")
    profileImg = models.ImageField('Imagen de Perfil', upload_to='profile/img/', blank=True, null=True)
    regisDate = models.DateField('Fecha de Registro', auto_now=True, auto_now_add=False)
    postal = models.IntegerField(default=0)
    activeUser = models.BooleanField(default=True)
    admUser = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

# Importante: indica parametro por defecto para inicio de sesion y los campos obligatorios:
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
                        'email',
                        'firstName',
                        'lastName',
                        'address',
                        'numIden',
                        
                ]
    
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

# Importante: Otorga los permisos de user a nuestra tabla
    def has_perm (self, perm, obj= None):
        return True

    def has_module_perms (self, app_label):
        return True

# Propiedad que marca los superusuarios en la tabla


    @property
    def is_staff (self):
        return self.admUser
