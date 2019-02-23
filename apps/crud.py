from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required  

class CRUD(object):
    
    def __init__(self, modelo, dirPrincipal, nombrePrincipal, PostForm):
        self.modelo = modelo
        self.dirPrincipal = dirPrincipal #Formato path/ con diagonal al final
        self.nombrePrincipal = nombrePrincipal #Formato path sin diagonal
        self.PostForm = PostForm

# Create your views here.
def vista(request, crud_object):
    termino = crud_object.modelo.objects.all()
    contexto = {'terminos':termino}
    return render(request, crud_object.dirPrincipal + crud_object.nombrePrincipal + '.html', contexto)

@login_required
def post(request, crud_object):
    if request.method == "POST":
        form = crud_object.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ed_' + crud_object.nombrePrincipal) 
    else:
        form = crud_object.PostForm()
    return render(request, 'educacion/base/agregarTermino.html', {'form': form})

@login_required
def edit(request, pk, crud_object):
    if not request.user.is_authenticated:
        termino = crud_object.modelo.objects.all()
        contexto = {'terminos':termino}
        return render(request, crud_object.dirPrincipal + crud_object.nombrePrincipal + '.html', contexto)
    post = get_object_or_404(crud_object.modelo, pk=pk)
    if request.method == "POST":
        form = crud_object.PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ed_' + crud_object.nombrePrincipal)
    else:
        form = crud_object.PostForm(instance=post)
    return render(request, 'educacion/base/agregarTermino.html', {'form': form})

def delete(request, pk, crud_object):
    termino = crud_object.modelo.objects.all()
    contexto = {'terminos':termino}
    if request.user.is_authenticated:
        post = get_object_or_404(crud_object.modelo, pk=pk)
        post.delete()
    return render(request, crud_object.dirPrincipal + crud_object.nombrePrincipal + '.html', contexto)
