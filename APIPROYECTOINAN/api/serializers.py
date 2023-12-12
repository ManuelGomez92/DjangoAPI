# miapp/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import frecuencia_compras, Departamento, Categoria, Productos, Genero, Empleado

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()
    


class FrecuenciaComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = frecuencia_compras
        fields = ['respuesta', 'num_respuestas']


class DepartmanentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'



class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'