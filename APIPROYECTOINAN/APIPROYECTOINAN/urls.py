"""APIPROYECTOINAN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from django.contrib.auth import views as auth_views
from api.views import enviarCorreo, FrecuenciaComprasList, DepartamentoListView, UploadToGoogleDrive, CategoriaListView, GeneroListView
from api.views import AnilloChartView, EmpleadosDataView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.model,name='login'),      
    path('altaUsuarios/',views.formulario,name='formulario'),
    path('en/inicio/',views.inicio2,name='inicio2'),
    path('inicio/',views.inicio,name='inicio'),
    path('login/',views.login,name='login'),
    path('entrantes/',views.altaProductos,name='entrantes'),
    path('registros/',views.datosgenerales,name='datos_generales'),    
    path('registroUsuarios/',views.registroUsuarios,name='reg_users'),
    path('graficos/',views.graficos,name='dashboard'),    
    path('enviarCorreo/', views.enviarCorreo,name='enviarCorreo'),
    path('frecuencia_compras/', FrecuenciaComprasList.as_view(), name='frecuencia_compras-data'),
    path('anillo-chart/', AnilloChartView.as_view(), name='anillo-chart'),
    path('upload-to-drive/', UploadToGoogleDrive.as_view(), name='upload-to-drive'),        
    path('departamentos/', DepartamentoListView, name='departamentos'),
    path('sexos/', GeneroListView, name='sexos'),
    path('categorias/', CategoriaListView, name='categorias'),
    path('empleados-data/', EmpleadosDataView.as_view(), name='empleados_data'),
    path('', include('django.contrib.auth.urls'))
]
