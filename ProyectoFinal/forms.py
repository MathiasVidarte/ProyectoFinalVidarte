from django import forms
from .models import Equipo, Jugador, Camiseta

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'fundacion']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'equipo', 'fecha_nacimiento']

class CamisetaForm(forms.ModelForm):
    class Meta:
        model = Camiseta
        fields = ['nombre', 'equipo', 'talla', 'precio']
