from .forms import PostForm
from .models import VolcanDefRef
from apps.crud import CRUD, vista, edit, delete, post

volcan = CRUD(VolcanDefRef, 'reflexion/erupcion/', 'erupcion', PostForm, 'ref_')

ref_erupcion = lambda request : vista(request, volcan)

ref_erupcion_post = lambda request : post(request, volcan)

ref_erupcion_edit = lambda request, pk : edit(request, pk, volcan)

ref_erupcion_delete = lambda request, pk : delete(request, pk, volcan)

