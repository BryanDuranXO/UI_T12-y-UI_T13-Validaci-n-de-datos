#Define los formularios de los modelos en esta App

from django import forms
from .models import Alumno

#Se debe crear una clase para cada modelo

class AlumnoForm(forms.ModelForm):
    #Meta es la clase que define la meta-informacion del formulario
    class Meta:
        #De que modelo se basa este formulario
        model = Alumno

        #Que campos se van a ver en el formulario
        fields = ['nombre', 'apellido','edad', 'matricula', 'correo']

        #Personalizar la apariencia del formulario(widgets)

        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Nombre'
                }
            ),
            'apellido': forms.TextInput(
            attrs= {
                   'class': 'form-input',
                'placeholder': 'Apellido'
                 }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Edad'
                }
            ),
            'matricula': forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Matrícula'
                }
            ),
               'correo': forms.EmailInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Correo electronico'
                }
            ),
        }

        #Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'matricula': 'Matrícula del alumno',
            'correo': 'Correo del alumno'
        }

        #Mensajes de error
        error_messages = {
            'nombre':{
                'required': 'El nombre es requerido'
            },
            'precio':{
                'required': 'El  precio no puede estar vacío',
                'invalid': 'Ingresa un número válido'

            }
        }