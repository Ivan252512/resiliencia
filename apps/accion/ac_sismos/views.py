from .forms import PostForm
from .models import SismoDefAc
from apps.crud import CRUD, vista, post, edit, delete

sismo = CRUD(SismoDefAc, 'accion/sismo/', 'sismo', PostForm, 'ac_')

ac_sismo = lambda request : vista(request, sismo)

ac_sismo_post = lambda request : post(request, sismo)

ac_sismo_edit = lambda request, pk : edit(request, pk, sismo)

ac_sismo_delete = lambda request, pk : delete(request, pk, sismo)

