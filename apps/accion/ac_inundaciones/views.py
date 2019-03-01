from .forms import PostForm
from .models import InundacionesDefAc
from apps.crud import CRUD, vista, post, edit, delete

inundacion = CRUD(InundacionesDefAc, 'accion/inundacion/', 'inundacion', PostForm, 'ac_')

ac_inundacion = lambda request : vista(request, inundacion)

ac_inundacion_post = lambda request : post(request, inundacion)

ac_inundacion_edit = lambda request, pk : edit(request, pk, inundacion)

ac_inundacion_delete = lambda request, pk : delete(request, pk, inundacion)
