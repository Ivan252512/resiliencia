from .forms import PostForm
from .models import AsteroidesDefRef
from apps.crud import CRUD, vista, post, edit, delete

asteroide = CRUD(AsteroidesDefRef, 'reflexion/asteroide/', 'asteroide', PostForm, 'ref_')

ref_asteroide = lambda request : vista(request, asteroide)

ref_asteroide_post = lambda request : post(request, asteroide)

ref_asteroide_edit = lambda request, pk : edit(request, pk, asteroide)

ref_asteroide_delete = lambda request, pk : delete(request, pk, asteroide)
