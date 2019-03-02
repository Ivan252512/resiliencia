from .forms import PostForm, PostAcSismoForm
from .models import SismoDefAc, PostAcSismo
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : SismoDefAc,
            'general' : PostAcSismo}

sismo = CRUD(SismoDefAc, 'accion/sismo/', 'sismo', PostForm, 'ac_', contexto)

ac_sismo = lambda request : vista(request, sismo)

ac_sismo_post = lambda request : post(request, sismo)

ac_sismo_edit = lambda request, pk : edit(request, pk, sismo)

ac_sismo_delete = lambda request, pk : delete(request, pk, sismo)




sismo_general = CRUD(PostAcSismo, 'accion/sismo/', 'sismo', PostAcSismoForm, 'ac_')

ac_sismo_general_post = lambda request : post(request, sismo_general)

ac_sismo_general_edit = lambda request, pk : edit(request, pk, sismo_general)

ac_sismo_general_delete = lambda request, pk : delete(request, pk, sismo_general)

