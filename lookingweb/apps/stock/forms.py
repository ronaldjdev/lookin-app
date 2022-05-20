from  django                    import forms
from .models                    import Inmueble

#Formularios para agregar inmuebles 
class InmuebleForm(forms.ModelForm):
        """definicion Form para Inmueble."""

        class Meta:
                """definicion Meta para Inmuebleform."""

                model  = Inmueble
                fields = (
                        'propertyName'   ,
                        'priceProperty'  ,
                        'area'           ,
                        'addressProperty',
                        'rooms'          ,
                        'bath'           ,
                        'garage'         ,
                        'imagesRoom'     ,
                        'typeProperty'   ,
                        'countryProperty',
                        'departProperty' ,
                        'cityProperty'   ,
                        'descrip'        ,
                )
                        
                labels = {

                        'propertyName'   :'Inmueble'       ,
                        'priceProperty'  :'Precio'         ,
                        'area'           :'Area'           ,
                        'addressProperty':'direccion'      ,
                        'rooms'          :'N° Habitaciones',
                        'bath'           :'N° Baños'       ,
                        'garage'         :'N° Garajes'     ,
                        'imagesRoom'     :'Imagenes'       ,
                        'typeProperty'   :'Tipo Propiedad' ,
                        'countryProperty':'Pais/Region'    ,
                        'departProperty' :'Departamento'   ,
                        'cityProperty'   :'Ciudad'         ,
                        'descrip'        :'Descipccion'    ,               
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
                                        'id':'typeProperty',
                                        'title':'Tipo',
                                        'multiple':'',
                                        'data-selected-text-format':'count',
                                        }
                        ),

                        'countryProperty': forms.Select(
                                attrs={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Pais\Region',
                                        'id':'countryProperty',
                                        'title':'Pais',
                                        'multiple':'',
                                        'data-selected-text-format':'count',
                                }
                        ),

                        'departProperty': forms.Select(
                                attrs={
                                        'class':'selectpicker show-tick',
                                        'placeholder':'Departamento',
                                        'id':'departProperty',
                                        'data-size':'5',
                                        'title':'Departamento',
                                        'multiple':'',
                                        'data-selected-text-format':'count',
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
