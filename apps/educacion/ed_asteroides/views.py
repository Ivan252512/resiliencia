from .forms import PostForm
from .models import AsteroidesDefEd
from apps.crud import CRUD, vista, post, edit, delete

asteroide = CRUD(AsteroidesDefEd, 'educacion/asteroide/', 'asteroide', PostForm)

ed_asteroide = lambda request : vista(request, asteroide)

ed_asteroide_post = lambda request : post(request, asteroide)

ed_asteroide_edit = lambda request, pk : edit(request, pk, asteroide)

ed_asteroide_delete = lambda request, pk : delete(request, pk, asteroide)
