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
from .views import ac_erupcion, ac_erupcion_post, ac_erupcion_edit, ac_erupcion_delete, ac_erupcion_general_post, ac_erupcion_general_edit, ac_erupcion_general_delete

urlpatterns = [
    path('ac_erupcion', ac_erupcion, name='ac_erupcion'),
    path('ac_erupcion_post/', ac_erupcion_post, name='ac_erupcion_post'),
    path('ac_erupcion_post/<int:pk>/edit/', ac_erupcion_edit, name='ac_erupcion_edit'),
    path('ac_erupcion_post/<int:pk>/delete/', ac_erupcion_delete, name='ac_erupcion_delete'),


    path('ac_erupcion_general_post/', ac_erupcion_general_post, name='ac_erupcion_general_post'),
    path('ac_erupcion_general_post/<int:pk>/edit/', ac_erupcion_general_edit, name='ac_erupcion_general_edit'),
    path('ac_erupcion_general_post/<int:pk>/delete/', ac_erupcion_general_delete, name='ac_erupcion_general_delete'),
]
