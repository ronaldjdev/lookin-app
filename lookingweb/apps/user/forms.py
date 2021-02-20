from django             import forms
from apps  .user.models import Usuarios


class PerfilForm(forms.ModelForm):
    """definicion Form para Perfil."""

    class Meta:
        """definicion Meta para Perfilform."""

        model  = Usuarios
        fields = (
            'address'   ,
            'streets'  ,
            'numIden'   ,
            'numPhone'  ,
            'country'   ,
            'depart'    ,
            'gender'    ,
            'profileImg',
            'postal'    ,
            'birthday'  ,
        )

        labels = {
            'address'    :'Ciudad'               ,
            'streets'   :'Barrio'               ,
            'numIden'    :'N° de Identificacion' ,
            'numPhone'   :'N° de Telefono'       ,
            'country'    :'Pais'                 ,
            'depart'     :'Departamento'         ,
            'gender'     :'Tipo de Genero'       ,
            'profileImg' :'Imagen de Perfil'     ,
            'postal'     :'Codigo Postal'        ,
            'birthday'   :'Fecha de Nacimiento'  ,
        }

        widgets = {
            'address' : forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Ciudad',
                }
            ),
            'streets': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Barrio',
                }
            )  ,
            'numIden' : forms.NumberInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'N° de Identificacion',
                }
            )  ,
            'numPhone': forms.NumberInput(
                attrs ={
                    'class':'form-control input-border-radius',
                    'placeholder':'N° de Telefono',
                }
            )  ,
            'country' : forms.Select(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Pais',
                }
            )  ,
            'depart' : forms.Select(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Departamento',
                }
            )   ,
            'gender' : forms.Select(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Tipo de Genero',
                }
            )   ,
            'profileImg': forms.FileInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Imagen de Perfil',
                }
            ),
            'postal'  : forms.NumberInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'Codigo Postal',
                }
            )  ,
            'birthday' : forms.DateInput(
                attrs={
                    'class':'form-control input-border-radius',
                    'placeholder':'dd/mm/aaaa',
                }
            )  ,
        }
