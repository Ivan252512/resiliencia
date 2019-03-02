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
from .views import ref_asteroide, ref_asteroide_post, ref_asteroide_edit, ref_asteroide_delete, ref_asteroide_general_post, ref_asteroide_general_edit, ref_asteroide_general_delete

urlpatterns = [
    path('ref_asteroide', ref_asteroide, name='ref_asteroide'),
    path('ref_asteroide_post/', ref_asteroide_post, name='ref_asteroide_post'),
    path('ref_asteroide_post/<int:pk>/edit', ref_asteroide_edit, name='ref_asteroide_edit'),
    path('ref_asteroide_post/<int:pk>/delete', ref_asteroide_delete, name='ref_asteroide_delete'),


    path('ref_asteroide_general_post/', ref_asteroide_general_post, name='ref_asteroide_general_post'),
    path('ref_asteroide_general_post/<int:pk>/edit', ref_asteroide_general_edit, name='ref_asteroide_general_edit'),
    path('ref_asteroide_general_post/<int:pk>/delete', ref_asteroide_general_delete, name='ref_asteroide_general_delete'),
]
