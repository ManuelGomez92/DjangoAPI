from django.shortcuts import render,redirect
from rest_framework.views import APIView
from . forms import UsuarioForm,EmpleadoForm, ProductoForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from . serializers import LoginSerializer, DepartmanentoSerializer, CategoriaSerializer, GeneroSerializer
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.core.mail import send_mail
import smtplib
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view




def model(request):    
    return render(request, 'loguear.html')

def loguear(request):
    return render(request, 'loguear.html')

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

def datosproductos(request):
    return render(request, 'inventario.html')


def graficos(request):
    return render(request, 'grafica.html')

def registroUsuarios(request):    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)        
        if form.is_valid():
            form.save()
            
    else:
        form = EmpleadoForm()
    return render(request, 'registro_usuarios.html', {'form':form})

def altaProductos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)        
        if form.is_valid():
            form.save()
            
    else:
        form = ProductoForm()
    return render(request, 'entrantes.html', {'form':form})



    
from rest_framework import generics
from .models import frecuencia_compras, Departamento, Categoria, Genero
from .serializers import FrecuenciaComprasSerializer, DepartmanentoSerializer, GeneroSerializer

class FrecuenciaComprasList(generics.ListCreateAPIView):
    queryset = frecuencia_compras.objects.all()
    serializer_class = FrecuenciaComprasSerializer

class AnilloChartView(APIView):
    def get(self, request):
        data = frecuencia_compras.objects.all().values('respuesta', 'num_respuestas')
        return Response(data)
    
@api_view(['GET'])
def DepartamentoListView(request):
    departamentos = Departamento.objects.all()
    serializer = DepartmanentoSerializer(departamentos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GeneroListView(request):
    generos = Genero.objects.all()
    serializer = GeneroSerializer(generos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CategoriaListView(request):
    datos = Categoria.objects.all()
    serializer = CategoriaSerializer(datos, many=True)
    return Response(serializer.data)

from .models import Empleado
from .serializers import EmpleadoSerializer
from django.db import connection

class EmpleadosDataView(APIView): 
    
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT a.id as id, a.nombre as nombre, a.paterno as paterno, a.materno as materno,
                a.telefono as telefono, a.fecha_ingreso as fecha_ingreso, b.tipogenero as sexo,
                c.descripcion as departamento
                FROM public.empleados a, public.generos b, public.departamentos c
                WHERE a.sexo_id=b.id AND c.id=a.departamento_id
                ORDER BY(a.id) ASC
            """)
            results = cursor.fetchall()

        data = [
            {
                'id': row[0],
                'nombre': row[1],
                'paterno': row[2],
                'materno': row[3],
                'telefono': row[4],
                'fecha_ingreso': row[5],
                'sexo': row[6],
                'departamento': row[7],
            }
            for row in results
        ]

        return Response(data)
    
class ProductosDataView(APIView): 
    
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT a.id as id, a.descripcion as descripcion, a.stock as stock, b.descripcion as departamento, a.precio as precio
	            FROM public.productos a, public.categorias b
	            WHERE b.id = a.idcategoria_id_id
            """)
            results = cursor.fetchall()

        data = [
            {
                'id': row[0],
                'descripcion': row[1],
                'stock': row[2],
                'departamento': row[3],
                'precio': row[4],                
            }
            for row in results
        ]

        return Response(data)

from .utils import authenticate_google_drive, upload_file_to_drive

class GoogleDriveView(APIView):
    def get(self, request):
        # Autenticar con Google Drive
        drive_service = authenticate_google_drive()

        # Subir un archivo de ejemplo
        file_id = upload_file_to_drive(drive_service, 'C:/Users/gmgv_/Downloads/Registros de PapelMágico.pdf')

        return Response({'file_id': file_id})
    
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.conf import settings
from googleapiclient.http import MediaFileUpload

class UploadToGoogleDrive(APIView):
    def get(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes GET si es necesario
        return Response({'message': 'GET request handled.'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Lógica para manejar solicitudes POST
        uploaded_file = request.FILES.get('papel_magico.pdf')

        if uploaded_file:
            credentials = Credentials.from_authorized_user_file(settings.GOOGLE_DRIVE_CREDENTIALS)
            drive_service = build('drive', 'v3', credentials=credentials)

            file_metadata = {'name': uploaded_file.name}
            media = MediaFileUpload(uploaded_file, mimetype=uploaded_file.content_type)
            file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            return Response({'file_id': file['id']}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)
