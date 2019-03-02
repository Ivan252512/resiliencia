from .forms import PostForm, PostEdInundacionForm
from .models import InundacionesDefEd, PostEdInundacion
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : InundacionesDefEd,
            'general' : PostEdInundacion}

inundacion = CRUD(InundacionesDefEd, 'educacion/inundacion/', 'inundacion', PostForm, 'ed_', contexto)

ed_inundacion = lambda request : vista(request, inundacion)

ed_inundacion_post = lambda request : post(request, inundacion)

ed_inundacion_edit = lambda request, pk : edit(request, pk, inundacion)

ed_inundacion_delete = lambda request, pk : delete(request, pk, inundacion)


inundacion_general = CRUD(PostEdInundacion, 'educacion/inundacion/', 'inundacion', PostEdInundacionForm, 'ed_')

ed_inundacion_general_post = lambda request : post(request, inundacion_general)

ed_inundacion_general_edit = lambda request, pk : edit(request, pk, inundacion_general)

ed_inundacion_general_delete = lambda request, pk : delete(request, pk, inundacion_general)