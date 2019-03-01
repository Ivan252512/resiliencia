from .forms import PostForm
from .models import LaderaDefRef
from apps.crud import CRUD, vista, post, edit, delete

ladera = CRUD(LaderaDefRef, 'reflexion/ladera/', 'ladera', PostForm, 'ref_')

ref_ladera = lambda request : vista(request, ladera)

ref_ladera_post = lambda request : post(request, ladera)

ref_ladera_edit = lambda request, pk : edit(request, pk, ladera)

ref_ladera_delete = lambda request, pk : delete(request, pk, ladera)

