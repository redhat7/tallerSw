import datetime
from django.db import models
from django.utils import timezone
    
class Estudiante(models.Model):
    codigo = models.CharField(primary_key=True,max_length=15)
    nombre = models.CharField(max_length=50,default=None)
    apellidos = models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.codigo

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion
    def __unicode__(self):
        return self.id
        

class Usuario(models.Model):
    username = models.CharField(primary_key=True,max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100,default=None)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    def __unicode__(self):
        return self.username

class EstadoPrestamo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion
    def __unicode__(self):
        return self.id

class TipoArticulo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion
    def __unicode__(self):
        return self.id

class EstadoArticulo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion
    def __unicode__(self):
        return self.id

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)    
    cantidad = models.IntegerField(default=0)
    estado = models.ForeignKey(EstadoArticulo)
    tipo = models.ForeignKey(TipoArticulo)
    def __str__(self):
        return self.id
    def __unicode__(self):
        return self.id

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoPrestamo,on_delete=models.CASCADE)
    articulos = models.ManyToManyField(Articulo)
    def __str__(self):
        return self.id
    def __unicode__(self):
        return self.id

class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.id

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion
    def __unicode__(self):
        return self.id

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.id

class Libro(models.Model):
    id = models.OneToOneField(Articulo,primary_key=True)
    argumento = models.CharField(max_length=1000)
    titulo = models.CharField(max_length=200)
    editorial = models.ForeignKey(Editorial)
    categoria = models.ForeignKey(Categoria)
    edicion = models.CharField(max_length=20)
    autores = models.ManyToManyField(Autor)
    anio_publicacion = models.CharField(max_length=4)
    fecha_ingreso = models.DateTimeField()
    def __str__(self):
        return self.titulo
    def __unicode__(self):
        return self.id

class Asesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.id

class Tesis(models.Model):
    id = models.OneToOneField(Articulo,primary_key=True)
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=1000)
    autor = models.OneToOneField(Estudiante)
    asesor = models.ForeignKey(Asesor)
    anio_publicacion = models.CharField(max_length=4)
    fecha_ingreso = models.DateTimeField()
    def __str__(self):
        return self.titulo
    def __unicode__(self):
        return self.id
