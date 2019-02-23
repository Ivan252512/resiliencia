from .forms import PostForm
from .models import InundacionesDefEd
from apps.crud import CRUD, vista, post, edit, delete

inundacion = CRUD(InundacionesDefEd, 'educacion/inundacion/', 'inundacion', PostForm)

ed_inundacion = lambda request : vista(request, inundacion)

ed_inundacion_post = lambda request : post(request, inundacion)

ed_inundacion_edit = lambda request, pk : edit(request, pk, inundacion)

ed_inundacion_delete = lambda request, pk : delete(request, pk, inundacion)
