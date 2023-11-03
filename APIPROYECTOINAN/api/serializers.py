# miapp/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import frecuencia_compras

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
    
from rest_framework import serializers
from .models import frecuencia_compras

class FrecuenciaComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = frecuencia_compras
        fields = ('id', 'respuesta', 'num_respuestas')
