from django.db import models

# Create your models here.

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True,db_column='idGenero')
    tipoGenero = models.TextField(db_column='tipoGenero')
    class Meta:
        db_table='Generos'

class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True,db_column='idDepartamento')
    descripcion = models.CharField(max_length=100,db_column='descripcion')
    class Meta:
        db_table='Departamentos'
        def __str__(self):
            return self.descripcion
        
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True,db_column='idUsuario')
    nombre = models.CharField(max_length=100,db_column='nombre')
    paterno = models.CharField(max_length=100,db_column='paterno')
    materno = models.CharField(max_length=100,db_column='materno')
    correo = models.CharField(max_length=100,db_column='correo')
    alias = models.CharField(max_length=100,db_column='alias')
    password = models.CharField(max_length=100,db_column='password')    
    class Meta:
        db_table='Usuarios'        
        def __str__(self):
            return f'{self.id}'
        
class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True,db_column='idEmpleado')
    nombre = models.CharField(max_length=100,db_column='nombre')
    paterno = models.CharField(max_length=100,db_column='paterno')
    materno = models.CharField(max_length=100,db_column='materno')
    telefono = models.CharField(max_length=100,db_column='telefono')
    fecha_ingreso = models.DateField(db_column='fecha_ingreso')
       
    class Meta:
        db_table='Empleados'        
        def __str__(self):
            return f'{self.id}'

class usuario_has_genero(models.Model):
    idusuario_has_genero = models.AutoField(primary_key=True,default=1,db_column='idalumno_has_genero')
    fk_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,db_column='fk_usuario')
    fk_genero = models.ForeignKey(Genero,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='usuario_has_genero'
        
""" Clases en base a las preguntas hechas en Google Forms """
        
class frecuencia_compras(models.Model):
    id= models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=255)
    num_respuestas = models.IntegerField(default=0)
    
        
class producto_frecuente(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)


        
class notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
    
        
class caracteristica_aplicacion(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
    
        
class sistema_operativo(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
   
        
class tipo_dispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
    
        
class elementos_app(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
    
        
class uso_app(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
    
        
class problemas_tecnicos(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
    
        
class facilidad_navegacion(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
          

        
class venta_equipo_oficina(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100)
    num_respuestas = models.IntegerField(default=0)
    