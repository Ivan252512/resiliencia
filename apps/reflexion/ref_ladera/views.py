from .forms import PostForm, PostRefLaderaForm
from .models import LaderaDefRef, PostRefLadera
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : LaderaDefRef,
            'general' : PostRefLadera}

ladera = CRUD(LaderaDefRef, 'reflexion/ladera/', 'ladera', PostForm, 'ref_', contexto)

ref_ladera = lambda request : vista(request, ladera)

ref_ladera_post = lambda request : post(request, ladera)

ref_ladera_edit = lambda request, pk : edit(request, pk, ladera)

ref_ladera_delete = lambda request, pk : delete(request, pk, ladera)




ladera_general = CRUD(PostRefLadera, 'reflexion/ladera/', 'ladera', PostRefLaderaForm, 'ref_')

ref_ladera_general_post = lambda request : post(request, ladera_general)

ref_ladera_general_edit = lambda request, pk : edit(request, pk, ladera_general)

ref_ladera_general_delete = lambda request, pk : delete(request, pk, ladera_general)

