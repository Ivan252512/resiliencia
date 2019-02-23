from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def proyecto(request):
    return render(request, 'core/proyecto.html')

def educacion(request):
    return render(request, 'core/educacion.html')

def reflexion(request):
    return render(request, 'core/reflexion.html')

def contacto(request):
    return render(request, 'core/contacto.html')