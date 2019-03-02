from .forms import PostForm, PostAcInundacionForm
from .models import InundacionesDefAc, PostAcInundacion
from apps.crud import CRUD, vista, post, edit, delete

contexto = {'terminos' : InundacionesDefAc,
            'general' : PostAcInundacion}

inundacion = CRUD(InundacionesDefAc, 'accion/inundacion/', 'inundacion', PostForm, 'ac_', contexto)

ac_inundacion = lambda request : vista(request, inundacion)

ac_inundacion_post = lambda request : post(request, inundacion)

ac_inundacion_edit = lambda request, pk : edit(request, pk, inundacion)

ac_inundacion_delete = lambda request, pk : delete(request, pk, inundacion)




inundacion_general = CRUD(PostAcInundacion, 'accion/inundacion/', 'inundacion', PostAcInundacionForm, 'ac_', contexto)

ac_inundacion_general_post = lambda request : post(request, inundacion_general)

ac_inundacion_general_edit = lambda request, pk : edit(request, pk, inundacion_general)

ac_inundacion_general_delete = lambda request, pk : delete(request, pk, inundacion_general)