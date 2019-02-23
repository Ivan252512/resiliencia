from .forms import PostForm
from .models import LaderaDefEd
from apps.crud import CRUD, vista, post, edit, delete

ladera = CRUD(LaderaDefEd, 'educacion/ladera/', 'ladera', PostForm)

ed_ladera = lambda request : vista(request, ladera)

ed_ladera_post = lambda request : post(request, ladera)

ed_ladera_edit = lambda request, pk : edit(request, pk, ladera)

ed_ladera_delete = lambda request, pk : delete(request, pk, ladera)

