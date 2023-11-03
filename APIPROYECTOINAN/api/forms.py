from django import forms
from . models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'paterno',
            'materno',
            'correo',
            'alias',
            'password',            
        ]
        
