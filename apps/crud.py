from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required  

class CRUD(object):
    
    def __init__(self, modelo, dirPrincipal, nombrePrincipal, PostForm, prefijo, contexto={}):
        self.modelo = modelo
        self.dirPrincipal = dirPrincipal #Formato path/ con diagonal al final
        self.nombrePrincipal = nombrePrincipal #Formato path sin diagonal
        self.PostForm = PostForm
        self.prefijo = prefijo
        if contexto=={}:
            self.contexto = {'terminos':self.modelo}
        else:
            self.contexto = contexto

# Create your views here.
def vista(request, crud_object):
    context = {}
    for i in crud_object.contexto.keys():
        context.update({i:crud_object.contexto.get(i).objects.all()})
    return render(request, crud_object.dirPrincipal + crud_object.nombrePrincipal + '.html', context)

@login_required
def post(request, crud_object):
    if request.method == "POST":
        form = crud_object.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(crud_object.prefijo + crud_object.nombrePrincipal) 
    else:
        form = crud_object.PostForm()
    return render(request, 'base/agregarTermino.html', {'form': form})

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
            return redirect(crud_object.prefijo + crud_object.nombrePrincipal)
    else:
        form = crud_object.PostForm(instance=post)
    return render(request, 'base/agregarTermino.html', {'form': form})

@login_required
def delete(request, pk, crud_object):
    termino = crud_object.modelo.objects.all()
    contexto = {'terminos':termino}
    if request.user.is_authenticated:
        post = get_object_or_404(crud_object.modelo, pk=pk)
        post.delete()
        return redirect(crud_object.prefijo + crud_object.nombrePrincipal)
    return render(request, crud_object.dirPrincipal + crud_object.nombrePrincipal + '.html', contexto)
