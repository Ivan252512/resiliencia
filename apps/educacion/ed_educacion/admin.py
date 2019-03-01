from django.contrib import admin
from apps.educacion.ed_educacion.models import Principal, Glosario, Referencia

# Register your models here.
admin.site.register(Principal)
admin.site.register(Glosario)
admin.site.register(Referencia)