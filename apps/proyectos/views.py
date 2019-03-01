from django.shortcuts import render

# Create your views here.
from .forms import PostForm
from .models import PostProyecto
from apps.crud import CRUD, post, edit, delete, vista

proyecto = CRUD(PostProyecto, 'proyectos/', 'proyectos', PostForm, '')

proyectos = lambda request : vista(request, proyecto)

proyectos_post = lambda request : post(request, proyecto)

proyectos_edit = lambda request, pk : edit(request, pk, proyecto)

proyectos_delete = lambda request, pk : delete(request, pk, proyecto)

