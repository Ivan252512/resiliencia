from .forms import PostForm, PostEdVolcanForm
from .models import VolcanDefEd, PostEdVolcan
from apps.crud import CRUD, vista, edit, delete, post


contexto = {'terminos' : VolcanDefEd,
            'general' : PostEdVolcan}

volcan = CRUD(VolcanDefEd, 'educacion/erupcion/', 'erupcion', PostForm, 'ed_', contexto)

ed_erupcion = lambda request : vista(request, volcan)

ed_erupcion_post = lambda request : post(request, volcan)

ed_erupcion_edit = lambda request, pk : edit(request, pk, volcan)

ed_erupcion_delete = lambda request, pk : delete(request, pk, volcan)


volcan_general = CRUD(PostEdVolcan, 'educacion/erupcion/', 'erupcion', PostEdVolcanForm, 'ed_')

ed_erupcion_general_post = lambda request : post(request, volcan_general)

ed_erupcion_general_edit = lambda request, pk : edit(request, pk, volcan_general)

ed_erupcion_general_delete = lambda request, pk : delete(request, pk, volcan_general)

