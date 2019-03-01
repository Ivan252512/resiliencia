from .forms import PostForm
from .models import InundacionesDefRef
from apps.crud import CRUD, vista, post, edit, delete

inundacion = CRUD(InundacionesDefRef, 'reflexion/inundacion/', 'inundacion', PostForm, 'ref_')

ref_inundacion = lambda request : vista(request, inundacion)

ref_inundacion_post = lambda request : post(request, inundacion)

ref_inundacion_edit = lambda request, pk : edit(request, pk, inundacion)

ref_inundacion_delete = lambda request, pk : delete(request, pk, inundacion)
