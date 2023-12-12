from django.test import TestCase
from api.models import Genero, Usuario, Empleado


# Create your tests here.

class GeneroTestCase(TestCase):
    def setUp(self):
        Genero.objects.create(idGenero=3, tipoGenero='Nuevo genero')

    def test_crearGenero(self):
        item = Genero.objects.get(idGenero=3)
        self.assertEqual(item.tipoGenero,'Nuevo genero')

    def test_actualizaGenero(self):
       item = Genero.objects.get(idGenero=3)
       item.tipoGenero='Genero actualizado'
       item.save()
       updated_item = Genero.objects.get(idGenero=3)
       self.assertEqual(updated_item.tipoGenero,'Genero actualizado') 

    def test_deleteGenero(self):
        item = Genero.objects.get(idGenero=3)
        item.delete()
        with self.assertRaises(Genero.DoesNotExist):
            Genero.objects.get(tipoGenero = 'Genero actualizado')

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nombre='Gerardo', paterno='Gomez', materno='Vazquez', correo='correo@correo.com.mx',alias='jerry', password='123')

    def test_crearUsuario(self):
        item = Usuario.objects.get(nombre='Gerardo')
        self.assertEqual(item.paterno,'Gomez')
        self.assertEqual(item.materno,'Vazquez')
        self.assertEqual(item.correo,'correo@correo.com.mx')
        self.assertEqual(item.alias,'jerry')
        self.assertEqual(item.password,'123')

    def test_actualizaUsuario(self):
       item = Usuario.objects.get(nombre='Gerardo')
       item.paterno='Gomez2'
       item.materno='Vazquez2'
       item.correo='micorreo'
       item.alias='gera'
       item.password='12345'
       item.save()
       updated_item = Usuario.objects.get(nombre='Gerardo')
       self.assertEqual(updated_item.paterno,'Gomez2') 
       self.assertEqual(updated_item.materno,'Vazquez2') 
       self.assertEqual(updated_item.correo,'micorreo') 
       self.assertEqual(updated_item.alias,'gera') 
       self.assertEqual(updated_item.password,'12345') 


    def test_deleteUsuario(self):
        item = Usuario.objects.get(nombre='Gerardo')
        item.delete()
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(nombre = 'Gerardo2')

class EmpleadoTestCase(TestCase):
    def setUp(self):
        Empleado.objects.create(nombre='Gerardo', paterno='Gomez', materno='Vazquez', telefono='5510305454',fecha_ingreso='2023-10-20')

    def test_crearEmpleado(self):
        item = Empleado.objects.get(nombre='Gerardo')
        self.assertEqual(item.paterno,'Gomez')
        self.assertEqual(item.materno,'Vazquez')
        self.assertEqual(item.telefono,'5510305454')
        self.assertEqual(item.fecha_ingreso,'2023-10-20')        

    def test_actualizaEmpleado(self):
       item = Empleado.objects.get(nombre='Gerardo Manuel')
       item.paterno='Gomez2'
       item.materno='Vazquez2'
       item.telefono='5545465665'
       item.fecha_ingreso='2023-10-21'       
       item.save()
       updated_item = Empleado.objects.get(nombre='Gerardo')
       self.assertEqual(updated_item.paterno,'Gomez2') 
       self.assertEqual(updated_item.materno,'Vazquez2') 
       self.assertEqual(updated_item.telefono,'5545465665') 
       self.assertEqual(updated_item.fecha_ingreso,'2023-10-21')        


    def test_deleteEmpleado(self):
        item = Empleado.objects.get(nombre='Gerardo')
        item.delete()
        with self.assertRaises(Empleado.DoesNotExist):
            Empleado.objects.get(nombre = 'Gerardo')

    
