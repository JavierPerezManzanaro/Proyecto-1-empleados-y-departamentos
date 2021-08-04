from django import forms
from django.forms import widgets

from .models import Pruebabbdd



class PruebaFormulario(forms.ModelForm):

    class Meta:
        model = Pruebabbdd
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',)
        widgets = {'titulo': forms.TextInput(
            attrs= {
                'placeholder' : 'Ingrese un texto aquí'
            }
        )}

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Inglese un númoer mayor de 10')
        return cantidad
