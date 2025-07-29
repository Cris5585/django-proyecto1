from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'mi_primer_app/home.html')


def hola_mundo(request):
    print("Hola Mundo")
    return HttpResponse("¡Hola, mundo!")

def crear_usuario(request, nombre):
    if nombre is not None:
        Usuario.objects.create(
            nombre=nombre, edad=25, fecha_nacimiento="1999-05-12")
    return render(request, 'mi_primer_app/crear-usuario.html', {"usuario": nombre})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'mi_primer_app/listar-usuarios.html', {"usuarios": usuarios})
