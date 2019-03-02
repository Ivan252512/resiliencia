from .forms import PostForm, PostAcVolcanForm
from .models import VolcanDefAc, PostAcVolcan
from apps.crud import CRUD, vista, edit, delete, post

contexto = {'terminos' : VolcanDefAc,
            'general' : PostAcVolcan}


volcan = CRUD(VolcanDefAc, 'accion/erupcion/', 'erupcion', PostForm, 'ac_', contexto)

ac_erupcion = lambda request : vista(request, volcan)

ac_erupcion_post = lambda request : post(request, volcan)

ac_erupcion_edit = lambda request, pk : edit(request, pk, volcan)

ac_erupcion_delete = lambda request, pk : delete(request, pk, volcan)


volcan_general = CRUD(PostAcVolcan, 'accion/erupcion/', 'erupcion', PostAcVolcanForm, 'ac_')

ac_erupcion_general_post = lambda request : post(request, volcan_general)

ac_erupcion_general_edit = lambda request, pk : edit(request, pk, volcan_general)

ac_erupcion_general_delete = lambda request, pk : delete(request, pk, volcan_general)
