from .forms import PostForm
from .models import SismoDefRef
from apps.crud import CRUD, vista, post, edit, delete

sismo = CRUD(SismoDefRef, 'reflexion/sismo/', 'sismo', PostForm, 'ref_')

ref_sismo = lambda request : vista(request, sismo)

ref_sismo_post = lambda request : post(request, sismo)

ref_sismo_edit = lambda request, pk : edit(request, pk, sismo)

ref_sismo_delete = lambda request, pk : delete(request, pk, sismo)

