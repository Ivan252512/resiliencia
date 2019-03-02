from .forms import PostForm, PostEdLaderaForm
from .models import LaderaDefEd, PostEdLadera
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : LaderaDefEd,
            'general' : PostEdLadera}

ladera = CRUD(LaderaDefEd, 'educacion/ladera/', 'ladera', PostForm, 'ed_', contexto)

ed_ladera = lambda request : vista(request, ladera)

ed_ladera_post = lambda request : post(request, ladera)

ed_ladera_edit = lambda request, pk : edit(request, pk, ladera)

ed_ladera_delete = lambda request, pk : delete(request, pk, ladera)



ladera_general = CRUD(PostEdLadera, 'educacion/ladera/', 'ladera', PostEdLaderaForm, 'ed_', contexto)

ed_ladera_general_post = lambda request : post(request, ladera_general)

ed_ladera_general_edit = lambda request, pk : edit(request, pk, ladera_general)

ed_ladera_general_delete = lambda request, pk : delete(request, pk, ladera_general)

