from .forms import PostForm, PostAcAsteroideForm
from .models import AsteroidesDefAc, PostAcAsteroide
from apps.crud import CRUD, vista, post, edit, delete

contexto = {'terminos' : AsteroidesDefAc,
            'general' : PostAcAsteroide}

asteroide = CRUD(AsteroidesDefAc, 'accion/asteroide/', 'asteroide', PostForm, 'ac_', contexto=contexto)

ac_asteroide = lambda request : vista(request, asteroide)

ac_asteroide_post = lambda request : post(request, asteroide)

ac_asteroide_edit = lambda request, pk : edit(request, pk, asteroide)

ac_asteroide_delete = lambda request, pk : delete(request, pk, asteroide)



asteroide_general = CRUD(PostAcAsteroide, 'accion/asteroide/', 'asteroide', PostAcAsteroideForm, 'ac_')

ac_asteroide_general_post = lambda request : post(request, asteroide_general)

ac_asteroide_general_edit = lambda request, pk : edit(request, pk, asteroide_general)

ac_asteroide_general_delete = lambda request, pk : delete(request, pk, asteroide_general)
