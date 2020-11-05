from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.user.models import Usuarios

# Formulario de inicio de sesion
class LoginForms (AuthenticationForm):
        def __init__(self, *args, **kwargs):
                super(LoginForms, self).__init__(*args, **kwargs)
                self.fields['username'].widget.attrs['class']='form-control'
                self.fields['username'].widget.attrs['type']='text'
                self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
                self.fields['username'].widget.attrs['id']='usermane'
                self.fields['password'].widget.attrs['class']='form-control'
                self.fields['password'].widget.attrs['type']='password'
                self.fields['password'].widget.attrs['placeholder']='Contraseña'
                self.fields['password'].widget.attrs['label']='Contraseña'
                self.fields['password'].widget.attrs['id']='password'

# Formulario de registro de usuario
class RegistryForms (forms.ModelForm):

        password1=forms.CharField(label='Ingrese Contraseña', widget = forms.PasswordInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Contraseña',
                                        'id':'password1'
                                }
                        ))

        password2=forms.CharField(label='Confirme Contraseña', widget = forms.PasswordInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Confirme Contraseña',
                                        'id':'password2'
                                }
                        ))

        class Meta:
                model  = Usuarios
                fields =[
                        'firstName',
                        'lastName',
                        'numIden',
                        'username',
                        'email',
                        'gender',
                        'country',
                        'depart',
                        'address',
                        'address2',
                ]
                labels ={
                        'firstName':'Nombres:',
                        'lastName':'Apellidos:',
                        'numIden':'N° de identifiacion:',
                        'username':'Nombre de Usuario:',
                        'email':'Correo Electronico:',
                        'gender':'Tipo de Genero',
                        'password1':'Contraseña:',
                        'password2':'Confirme Contraseña:',
                        'country':'Pais:',
                        'depart':'Departamento:',
                        'address':'Ciudad:',
                        'address2':'Direccion de Residencia.',

                }
                widgets ={
                        'firstName':forms.TextInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Nombres',
                                        'id':'firstName'
                                }
                        ),
                        'lastName':forms.TextInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Apellidos',
                                        'id':'lastName'
                                }
                        ),
                        'numIden':forms.NumberInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'N° de Identificacion',
                                        'id':'numIden'
                                }
                        ),
                        'username':forms.TextInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Nombre de Usuario',
                                        'id':'username'
                                }
                        ),
                        'email':forms.EmailInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Correo Electronico',
                                        'id':'email'
                                }
                        ),
                        'gender':forms.Select(
                                attrs ={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Tipo de Genero',
                                        'id':'gender'
                                }
                        ),
                        'country':forms.Select(
                                attrs ={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Pais',
                                        'id':'country'
                                }
                        ),
                        'depart':forms.Select(
                                attrs ={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Departamentos',
                                        'id':'depart',
                                        'data-size':'5',
                                }
                        ),
                        'address':forms.TextInput(
                                attrs ={
                                        'class':'form-control ',
                                        'placeholder':'Ciudad',
                                        'id':'address'
                                }
                        ),
                        'address2':forms.TextInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Cll 26BN #4-30',
                                        'id':'address2'
                                }
                        ),
                }
