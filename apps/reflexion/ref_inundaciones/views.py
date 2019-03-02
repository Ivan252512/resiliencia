from .forms import PostForm, PostRefInundacionForm
from .models import InundacionesDefRef, PostRefInundacion
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : InundacionesDefRef,
            'general' : PostRefInundacion}

inundacion = CRUD(InundacionesDefRef, 'reflexion/inundacion/', 'inundacion', PostForm, 'ref_', contexto)

ref_inundacion = lambda request : vista(request, inundacion)

ref_inundacion_post = lambda request : post(request, inundacion)

ref_inundacion_edit = lambda request, pk : edit(request, pk, inundacion)

ref_inundacion_delete = lambda request, pk : delete(request, pk, inundacion)




inundacion_general = CRUD(PostRefInundacion, 'reflexion/inundacion/', 'inundacion', PostRefInundacionForm, 'ref_')

ref_inundacion_general_post = lambda request : post(request, inundacion_general)

ref_inundacion_general_edit = lambda request, pk : edit(request, pk, inundacion_general)

ref_inundacion_general_delete = lambda request, pk : delete(request, pk, inundacion_general)