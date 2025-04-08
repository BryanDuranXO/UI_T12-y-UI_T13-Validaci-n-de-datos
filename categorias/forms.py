from django import forms
from .models import Categoria

class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',  
                    'placeholder': 'Nombre de la categoría',
                    'id': 'nom'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Imagen del producto'
                }
            ),
        }

        labels = {
            'nombre': 'Nombre de la categoría',
            'imagen': 'URL de la imagen',
        }

        # Mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El nombre de la categoría es requerido'
            },
        }
