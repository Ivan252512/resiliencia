from django.shortcuts import render

# Create your views here.
from .forms import PrincipalForm, GlosarioForm, ReferenciaForm
from .models import Principal, Glosario, Referencia
from apps.crud import CRUD, post, edit, delete, vista


contexto = {'terminos' : Principal,
            'glosarios' : Glosario,
            'referencias' : Referencia}


#Principal
educacion = CRUD(Principal, 'core/', 'educacion', PrincipalForm, 'ed_', contexto=contexto)

ed_educacion = lambda request : vista(request, educacion)

ed_educacion_post = lambda request : post(request, educacion)

ed_educacion_edit = lambda request, pk : edit(request, pk, educacion)

ed_educacion_delete = lambda request, pk : delete(request, pk, educacion)


#Glosario
glosario = CRUD(Glosario, 'core/', 'educacion', GlosarioForm, 'ed_')

ed_glosario_post = lambda request : post(request, glosario)

ed_glosario_edit = lambda request, pk : edit(request, pk, glosario)

ed_glosario_delete = lambda request, pk : delete(request, pk, glosario)


#Referencias
referencia = CRUD(Referencia, 'core/', 'educacion', ReferenciaForm, 'ed_')

ed_referencia_post = lambda request : post(request, referencia)

ed_referencia_edit = lambda request, pk : edit(request, pk, referencia)

ed_referencia_delete = lambda request, pk : delete(request, pk, referencia)

