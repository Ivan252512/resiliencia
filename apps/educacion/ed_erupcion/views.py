from .forms import PostForm
from .models import VolcanDefEd
from apps.crud import CRUD, vista, edit, delete, post

volcan = CRUD(VolcanDefEd, 'educacion/erupcion/', 'erupcion', PostForm, 'ed_')

ed_erupcion = lambda request : vista(request, volcan)

ed_erupcion_post = lambda request : post(request, volcan)

ed_erupcion_edit = lambda request, pk : edit(request, pk, volcan)

ed_erupcion_delete = lambda request, pk : delete(request, pk, volcan)

