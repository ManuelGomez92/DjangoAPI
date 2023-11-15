from django import forms
from . models import Usuario, Empleado

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
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'paterno',
            'materno',
            'telefono',
            'fecha_ingreso',                       
        ]
