"""riesgocdmx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import *

urlpatterns = [
    
    #Principal
    path('ed_educacion/', ed_educacion, name='ed_educacion'),
    path('ed_educacion_post/', ed_educacion_post, name='ed_educacion_post'),
    path('ed_educacion_post/<int:pk>/edit_educacion', ed_educacion_edit, name='ed_educacion_edit'),
    path('ed_educacion_post/<int:pk>/delete_educacion', ed_educacion_delete, name='ed_educacion_delete'),
        
    #Glosario
    path('ed_educacion_post_glosario/', ed_glosario_post, name='ed_glosario_post'),
    path('ed_educacion_post_glosario/<int:pk>/edit_glosario', ed_glosario_edit, name='ed_glosario_edit'),
    path('ed_educacion_post_glosario/<int:pk>/delete_glosario', ed_glosario_delete, name='ed_glosario_delete'),

    #Referencia
    path('ed_educacion_post_referencia/', ed_referencia_post, name='ed_referencia_post'),
    path('ed_educacion_post_referencia/<int:pk>/edit_referencia', ed_referencia_edit, name='ed_referencia_edit'),
    path('ed_educacion_post_referencia/<int:pk>/delete_referencia', ed_referencia_delete, name='ed_referencia_delete'),
]
