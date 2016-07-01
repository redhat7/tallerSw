from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import Usuario, Estudiante, Rol
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    template = loader.get_template('polls/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context,request))

def inicio(request):
    if request.user.is_authenticated():
        template = loader.get_template('polls/inicio.html')
        return HttpResponse(template.render(None,request))
    else:
        return HttpResponseRedirect(reverse('login')+"?next="+'inicio')

def login(request):
    if request.method == 'GET':
        template = loader.get_template('polls/login.html')
        context = {
            'mensaje' : '',
            'next' : request.GET.get('next',''),
        }
        return HttpResponse(template.render(context,request))
    elif request.method == 'POST':
        template = loader.get_template('polls/index.html')
        fUsername = request.POST['username']
        fPassword = request.POST['password']
        user = authenticate(username = fUsername, password = fPassword)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                next_page = request.GET.get('next','')
                if next_page == '':
                    return HttpResponseRedirect(reverse(next_page))
                else:
                    return HttpResponseRedirect(reverse('inicio'))
            else:
                template = loader.get_template('polls/login.html')
                context = {
                    'mensaje': 'Usuario no activo',
                }
                return HttpResponse(template.render(context,request))
        else:
            template = loader.get_template('polls/login.html')
            context = {
                'mensaje' : 'Datos incorrectos',
            }
            return HttpResponse(template.render(context,request))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))

def registro(request):
    if request.method == 'GET':
        template = loader.get_template('polls/registro.html')
        context = {
                'mensaje': '',
        }
        return HttpResponse(template.render(context,request))
    elif request.method == 'POST':
        template = loader.get_template('polls/registro.html')
        fCodigo = request.POST['codigo']
        try:
            e = Estudiante.objects.get(codigo=fCodigo)
        except Estudiante.DoesNotExist:
            context = {
                'mensaje': 'El estudiante no esta registrado',
            }
            return HttpResponse(template.render(context,request))                                
        fUsername = request.POST['username']
        try:
            u = User.objects.get(username=fUsername)
            context = {
                'mensaje': 'El usuario ya existe'
            }
            return HttpResponse(template.render(context,request))
        except User.DoesNotExist:
            fPassword = request.POST['password']
            fEmail = request.POST['email']
            user = User.objects.create_user(fUsername,fEmail,fPassword)
            user.save()
            r = Rol.objects.get(descripcion="estudiante")
            usuario = Usuario(username = fUsername, password = fPassword, email = fEmail, estudiante = e, rol = r)
            usuario.save()
            context = {
                'mensaje': 'Registro Exitoso'
            }
            return HttpResponse(template.render(context,request))
                            
        
        
                           
                


