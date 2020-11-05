from  django                    import forms
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models                    import Inmueble

#Formularios para agregar inmuebles 
class InmuebleForm(forms.ModelForm):
        """Form definition for Inmueble."""

        class Meta:
                """Meta definition for Inmuebleform."""

                model  = Inmueble
                fields = (
                        'propertyName',
                        'priceProperty',
                        'area',
                        'addressProperty',
                        'rooms',
                        'bath',
                        'garage',
                        'imagesRoom',
                        'typeProperty',
                        'countryProperty',
                        'departProperty',
                        'cityProperty',
                        'descrip',
                )
                        
                labels = {
                        'propertyName':'Inmueble',
                        'priceProperty':'Precio',
                        'area':'Area',
                        'addressProperty':'direccion',
                        'rooms':'N° Habitaciones',
                        'bath':'N° Baños',
                        'garage':'N° Garajes',
                        'imagesRoom':'Imagenes',
                        'typeProperty':'Tipo Propiedad',
                        'countryProperty':'Pais/Region',
                        'departProperty':'Departamento',
                        'cityProperty':'Ciudad',
                        'descrip':'Descipccion',               
                }

                widgets = {
                        'propertyName': forms.TextInput(
                                attrs ={
                                        'class':'form-control',
                                        'placeholder':'Nombre Propiedad',
                                        'id':'propertyName'
                                        }
                        ),

                        'priceProperty': forms.NumberInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Precio',
                                        'id':'priceProperty'
                                }
                        ),

                        'area': forms.NumberInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Precio',
                                        'id':'priceProperty'
                                }
                        ),

                        'addressProperty': forms.TextInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Direccion',
                                        'id':'addressProperty'
                                }
                        ),

                        'rooms': forms.NumberInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Precio',
                                        'id':'priceProperty'
                                }
                        ),

                        'bath': forms.NumberInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Precio',
                                        'id':'priceProperty'
                                }
                        ),

                        'garage': forms.NumberInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Precio',
                                        'id':'priceProperty'
                                }
                        ),

                        'imagesRoom': forms.FileInput(
                                attrs={
                                        'class':'custom-file-input',
                                        'placeholder':'Agregar imagenes',
                                        'id':'imagesRoom'
                                }
                        ),

                        'typeProperty': forms.Select(
                                attrs={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Tipo de Propiedad',
                                        'id':'typeProperty'
                                        }
                        ),

                        'countryProperty': forms.Select(
                                attrs={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Pais\Region',
                                        'id':'countryProperty'
                                }
                        ),

                        'departProperty': forms.Select(
                                attrs={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Departamento',
                                        'id':'departProperty',
                                        'data-size':'5',
                                }
                        ),

                        'cityProperty': forms.TextInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Ciudad',
                                        'id':'cityProperty'
                                }
                        ),

                        'descrip': forms.Textarea(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Descripcion',
                                        'id':'descrip'
                                }
                        ),
                }
