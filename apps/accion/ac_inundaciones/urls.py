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
from .views import ac_inundacion, ac_inundacion_post, ac_inundacion_edit, ac_inundacion_delete, ac_inundacion_general_post, ac_inundacion_general_edit, ac_inundacion_general_delete

urlpatterns = [
    path('ac_inundacion', ac_inundacion, name='ac_inundacion'),
    path('ac_inundacion_post/', ac_inundacion_post, name='ac_inundacion_post'),
    path('ac_inundacion_post/<int:pk>/edit', ac_inundacion_edit, name='ac_inundacion_edit'),
    path('ac_inundacion_post/<int:pk>/delete', ac_inundacion_delete, name='ac_inundacion_delete'),


    path('ac_inundacion_general_post/', ac_inundacion_general_post, name='ac_inundacion_general_post'),
    path('ac_inundacion_general_post/<int:pk>/edit', ac_inundacion_general_edit, name='ac_inundacion_general_edit'),
    path('ac_inundacion_general_post/<int:pk>/delete', ac_inundacion_general_delete, name='ac_inundacion_general_delete'),
]
