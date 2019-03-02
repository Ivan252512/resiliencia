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
from .views import ref_inundacion, ref_inundacion_post, ref_inundacion_edit, ref_inundacion_delete, ref_inundacion_general_post, ref_inundacion_general_edit, ref_inundacion_general_delete

urlpatterns = [
    path('ref_inundacion', ref_inundacion, name='ref_inundacion'),
    path('ref_inundacion_post/', ref_inundacion_post, name='ref_inundacion_post'),
    path('ref_inundacion_post/<int:pk>/edit', ref_inundacion_edit, name='ref_inundacion_edit'),
    path('ref_inundacion_post/<int:pk>/delete', ref_inundacion_delete, name='ref_inundacion_delete'),


    path('ref_inundacion_general_post/', ref_inundacion_general_post, name='ref_inundacion_general_post'),
    path('ref_inundacion_general_post/<int:pk>/edit', ref_inundacion_general_edit, name='ref_inundacion_general_edit'),
    path('ref_inundacion_general_post/<int:pk>/delete', ref_inundacion_general_delete, name='ref_inundacion_general_delete'),
]
