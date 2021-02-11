from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
                self.fields['password'].widget.attrs['id']='password2'

# Formulario de registro de usuario
class RegistryForms (UserCreationForm):

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
                model  = User
                fields =[
                        'first_name',
                        'last_name',
                        'username',
                        'email',
                ]
                labels ={
                        'first_name':'Nombres:',
                        'last_name':'Apellidos:',
                        'username':'Nombre de Usuario:',
                        'email':'Correo Electronico:',
                        
                }