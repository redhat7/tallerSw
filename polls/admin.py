from django.contrib import admin
from .models import Estudiante, Usuario, Rol, EstadoPrestamo, TipoArticulo, EstadoArticulo, Articulo, Editorial, Categoria, Autor, Libro,Tesis,Asesor

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(EstadoPrestamo)
admin.site.register(TipoArticulo)
admin.site.register(EstadoArticulo)
admin.site.register(Articulo)
admin.site.register(Editorial)
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Tesis)
admin.site.register(Asesor)
