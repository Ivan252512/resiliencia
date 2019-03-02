from .forms import PostForm, PostRefSismoForm
from .models import SismoDefRef, PostRefSismo
from apps.crud import CRUD, vista, post, edit, delete



contexto = {'terminos' : SismoDefRef,
            'general' : PostRefSismo}

sismo = CRUD(SismoDefRef, 'reflexion/sismo/', 'sismo', PostForm, 'ref_', contexto)

ref_sismo = lambda request : vista(request, sismo)

ref_sismo_post = lambda request : post(request, sismo)

ref_sismo_edit = lambda request, pk : edit(request, pk, sismo)

ref_sismo_delete = lambda request, pk : delete(request, pk, sismo)





sismo_general = CRUD(PostRefSismo, 'reflexion/sismo/', 'sismo', PostRefSismoForm, 'ref_')

ref_sismo_general_post = lambda request : post(request, sismo_general)

ref_sismo_general_edit = lambda request, pk : edit(request, pk, sismo_general)

ref_sismo_general_delete = lambda request, pk : delete(request, pk, sismo_general)

