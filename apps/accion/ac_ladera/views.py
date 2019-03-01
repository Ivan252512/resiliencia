from .forms import PostForm
from .models import LaderaDefAc
from apps.crud import CRUD, vista, post, edit, delete

ladera = CRUD(LaderaDefAc, 'accion/ladera/', 'ladera', PostForm, 'ac_')

ac_ladera = lambda request : vista(request, ladera)

ac_ladera_post = lambda request : post(request, ladera)

ac_ladera_edit = lambda request, pk : edit(request, pk, ladera)

ac_ladera_delete = lambda request, pk : delete(request, pk, ladera)

