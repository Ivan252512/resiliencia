from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def proyecto(request):
    return render(request, 'core/proyecto.html')
