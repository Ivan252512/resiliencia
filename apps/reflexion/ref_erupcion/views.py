from .forms import PostForm, PostRefVolcanForm
from .models import VolcanDefRef, PostRefVolcan
from apps.crud import CRUD, vista, edit, delete, post


contexto = {'terminos' : VolcanDefRef,
            'general' : PostRefVolcan}

volcan = CRUD(VolcanDefRef, 'reflexion/erupcion/', 'erupcion', PostForm, 'ref_', contexto)

ref_erupcion = lambda request : vista(request, volcan)

ref_erupcion_post = lambda request : post(request, volcan)

ref_erupcion_edit = lambda request, pk : edit(request, pk, volcan)

ref_erupcion_delete = lambda request, pk : delete(request, pk, volcan)





volcan_general = CRUD(PostRefVolcan, 'reflexion/erupcion/', 'erupcion', PostRefVolcanForm, 'ref_')

ref_erupcion_general_post = lambda request : post(request, volcan_general)

ref_erupcion_general_edit = lambda request, pk : edit(request, pk, volcan_general)

ref_erupcion_general_delete = lambda request, pk : delete(request, pk, volcan_general)

