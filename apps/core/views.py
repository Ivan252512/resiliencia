from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from apps.crud import CRUD, post, edit, delete, vista
from .forms import  VideosForm


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def proyecto(request):
    return render(request, 'core/proyecto.html')



contexto = {'videos' : Video}

video = CRUD(Video, 'core/', 'index', VideosForm, '', contexto=contexto)

index = lambda request : vista(request, video)

video_post = lambda request : post(request, video)

video_edit = lambda request, pk : edit(request, pk, video)

video_delete = lambda request, pk : delete(request, pk, video)