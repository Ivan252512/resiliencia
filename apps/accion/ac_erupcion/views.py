from .forms import PostForm
from .models import VolcanDefAc
from apps.crud import CRUD, vista, edit, delete, post

volcan = CRUD(VolcanDefAc, 'accion/erupcion/', 'erupcion', PostForm, 'ac_')

ac_erupcion = lambda request : vista(request, volcan)

ac_erupcion_post = lambda request : post(request, volcan)

ac_erupcion_edit = lambda request, pk : edit(request, pk, volcan)

ac_erupcion_delete = lambda request, pk : delete(request, pk, volcan)

