from .forms import PostForm
from .models import AsteroidesDefAc
from apps.crud import CRUD, vista, post, edit, delete

asteroide = CRUD(AsteroidesDefAc, 'accion/asteroide/', 'asteroide', PostForm, 'ac_')

ac_asteroide = lambda request : vista(request, asteroide)

ac_asteroide_post = lambda request : post(request, asteroide)

ac_asteroide_edit = lambda request, pk : edit(request, pk, asteroide)

ac_asteroide_delete = lambda request, pk : delete(request, pk, asteroide)
