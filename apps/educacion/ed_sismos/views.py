from .forms import PostForm, PostEdSismoForm
from .models import SismoDefEd, PostEdSismo
from apps.crud import CRUD, vista, post, edit, delete



contexto = {'terminos' : SismoDefEd,
            'general' : PostEdSismo}


sismo = CRUD(SismoDefEd, 'educacion/sismo/', 'sismo', PostForm, 'ed_', contexto)

ed_sismo = lambda request : vista(request, sismo)

ed_sismo_post = lambda request : post(request, sismo)

ed_sismo_edit = lambda request, pk : edit(request, pk, sismo)

ed_sismo_delete = lambda request, pk : delete(request, pk, sismo)



sismo_general = CRUD(PostEdSismo, 'educacion/sismo/', 'sismo', PostEdSismoForm, 'ed_')

ed_sismo_general_post = lambda request : post(request, sismo_general)

ed_sismo_general_edit = lambda request, pk : edit(request, pk, sismo_general)

ed_sismo_general_delete = lambda request, pk : delete(request, pk, sismo_general)


