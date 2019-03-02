from .forms import PostForm, PostEdAsteroidesForm
from .models import AsteroidesDefEd, PostEdAsteroides
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : AsteroidesDefEd,
            'general' : PostEdAsteroides}


asteroide = CRUD(AsteroidesDefEd, 'educacion/asteroide/', 'asteroide', PostForm, 'ed_', contexto)

ed_asteroide = lambda request : vista(request, asteroide)

ed_asteroide_post = lambda request : post(request, asteroide)

ed_asteroide_edit = lambda request, pk : edit(request, pk, asteroide)

ed_asteroide_delete = lambda request, pk : delete(request, pk, asteroide)




asteroide_general = CRUD(PostEdAsteroides, 'educacion/asteroide/', 'asteroide', PostEdAsteroidesForm, 'ed_')


ed_asteroide_general_post = lambda request : post(request, asteroide_general)

ed_asteroide_general_edit = lambda request, pk : edit(request, pk, asteroide_general)

ed_asteroide_general_delete = lambda request, pk : delete(request, pk, asteroide_general)
