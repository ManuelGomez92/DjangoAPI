from django.shortcuts import render,redirect
from rest_framework.views import APIView
from . forms import UsuarioForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from . serializers import LoginSerializer
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.core.mail import send_mail
import smtplib
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView



def model(request):    
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def formulario(request):    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form':form})

def enviarCorreo(request):
    try:
        mensaje = request.GET.get('mensaje')
        correo_electronico = request.GET.get('correo')
        asunto = request.GET.get('asunto')

        body = 'Subject: {}\n\n{}'.format(asunto, mensaje)
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
        server.login('gg204872@gmail.com','eowtbsideqvrkhst')
        server.sendmail('gg204872@gmail.com', correo_electronico, body)
        server.quit()
        return JsonResponse({'status': True, 'mensaje': 'Correo enviado exitosamente'})
    except Exception as e:
        return JsonResponse({'status': False, 'mensaje': 'Ocurrio un error al momento de enviar el correo', 'error': str(e)})

@login_required
def inicio(request):    
    return render(request, 'inicio.html')

def inicio2(request):    
    return render(request, 'inicio-en.html')
    

def datosgenerales(request):
    return render(request, 'datos-generales.html')


def graficos(request):
    return render(request, 'grafica.html')



    
from rest_framework import generics
from .models import frecuencia_compras
from .serializers import FrecuenciaComprasSerializer

class FrecuenciaComprasList(generics.ListCreateAPIView):
    queryset = frecuencia_compras.objects.all()
    serializer_class = FrecuenciaComprasSerializer

class AnilloChartView(APIView):
    def get(self, request):
        data = frecuencia_compras.objects.all().values('respuesta', 'num_respuestas')
        return Response(data)
    