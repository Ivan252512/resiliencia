from .forms import PostForm, PostAcLaderaForm
from .models import LaderaDefAc, PostAcLadera
from apps.crud import CRUD, vista, post, edit, delete


contexto = {'terminos' : LaderaDefAc,
            'general' : PostAcLadera}

ladera = CRUD(LaderaDefAc, 'accion/ladera/', 'ladera', PostForm, 'ac_', contexto)

ac_ladera = lambda request : vista(request, ladera)

ac_ladera_post = lambda request : post(request, ladera)

ac_ladera_edit = lambda request, pk : edit(request, pk, ladera)

ac_ladera_delete = lambda request, pk : delete(request, pk, ladera)




ladera_general = CRUD(PostAcLadera, 'accion/ladera/', 'ladera', PostAcLaderaForm, 'ac_')

ac_ladera_general_post = lambda request : post(request, ladera_general)

ac_ladera_general_edit = lambda request, pk : edit(request, pk, ladera_general)

ac_ladera_general_delete = lambda request, pk : delete(request, pk, ladera_general)

