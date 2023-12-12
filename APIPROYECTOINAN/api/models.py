from django.db import models

# Create your models here.

from django.db import models

class Genero(models.Model):    
    tipogenero = models.TextField(db_column='tipogenero')

    class Meta:
        db_table = 'generos'

    def __str__(self):
        return self.tipogenero

class Departamento(models.Model):    
    descripcion = models.CharField(max_length=100, db_column='descripcion')

    class Meta:
        db_table = 'departamentos'

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):    
    descripcion = models.CharField(max_length=100, db_column='descripcion')

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.descripcion

class Productos(models.Model):    
    descripcion = models.CharField(max_length=100, db_column='descripcion')
    stock = models.IntegerField(db_column='stock')
    idcategoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, db_column='precio')

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.descripcion

class Roles(models.Model):    
    descripcion = models.CharField(max_length=100, db_column='descripcion')

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, db_column='nombre')
    paterno = models.CharField(max_length=100, db_column='paterno')
    materno = models.CharField(max_length=100, db_column='materno')
    telefono = models.CharField(max_length=100, db_column='telefono')
    fecha_ingreso = models.DateField(db_column='fecha_ingreso')
    sexo = models.ForeignKey(Genero, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        db_table = 'empleados'

    def __str__(self):
        return f'{self.nombre} {self.paterno} {self.materno}'

class Usuario(models.Model):    
    nombre = models.CharField(max_length=100, db_column='nombre')
    paterno = models.CharField(max_length=100, db_column='paterno')
    materno = models.CharField(max_length=100, db_column='materno')
    correo = models.CharField(max_length=100, db_column='correo')
    alias = models.CharField(max_length=100, db_column='alias')
    password = models.CharField(max_length=100, db_column='password')           
    idempleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    idrol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return f'{self.nombre} {self.paterno} {self.materno}'

class UsuarioHasGenero(models.Model):
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='fk_usuario')
    fk_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='fk_genero')

    class Meta:
        db_table = 'usuario_has_genero'


        
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
    