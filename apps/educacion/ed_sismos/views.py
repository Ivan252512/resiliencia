from .forms import PostForm
from .models import SismoDefEd
from apps.crud import CRUD, vista, post, edit, delete

sismo = CRUD(SismoDefEd, 'educacion/sismo/', 'sismo', PostForm, 'ed_')

ed_sismo = lambda request : vista(request, sismo)

ed_sismo_post = lambda request : post(request, sismo)

ed_sismo_edit = lambda request, pk : edit(request, pk, sismo)

ed_sismo_delete = lambda request, pk : delete(request, pk, sismo)

