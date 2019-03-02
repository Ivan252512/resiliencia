from .forms import PostForm, PostRefAsteroideForm
from .models import AsteroidesDefRef, PostRefAsteroide
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : AsteroidesDefRef,
            'general' : PostRefAsteroide}

asteroide = CRUD(AsteroidesDefRef, 'reflexion/asteroide/', 'asteroide', PostForm, 'ref_', contexto)

ref_asteroide = lambda request : vista(request, asteroide)

ref_asteroide_post = lambda request : post(request, asteroide)

ref_asteroide_edit = lambda request, pk : edit(request, pk, asteroide)

ref_asteroide_delete = lambda request, pk : delete(request, pk, asteroide)



asteroide_general = CRUD(PostRefAsteroide, 'reflexion/asteroide/', 'asteroide', PostRefAsteroideForm, 'ref_')

ref_asteroide_general_post = lambda request : post(request, asteroide_general)

ref_asteroide_general_edit = lambda request, pk : edit(request, pk, asteroide_general)

ref_asteroide_general_delete = lambda request, pk : delete(request, pk, asteroide_general)

