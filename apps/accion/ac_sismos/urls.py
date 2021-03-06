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
from .views import ac_sismo, ac_sismo_post, ac_sismo_edit, ac_sismo_delete, ac_sismo_general_post, ac_sismo_general_edit, ac_sismo_general_delete

urlpatterns = [
    path('ac_sismo', ac_sismo, name='ac_sismo'),
    path('ac_sismo_post/', ac_sismo_post, name='ac_sismo_post'),
    path('ac_sismo_post/<int:pk>/edit', ac_sismo_edit, name='ac_sismo_edit'),
    path('ac_sismo_post/<int:pk>/delete', ac_sismo_delete, name='ac_sismo_delete'),


    path('ac_sismo_general_post/', ac_sismo_general_post, name='ac_sismo_general_post'),
    path('ac_sismo_general_post/<int:pk>/edit', ac_sismo_general_edit, name='ac_sismo_general_edit'),
    path('ac_sismo_general_post/<int:pk>/delete', ac_sismo_general_delete, name='ac_sismo_general_delete'),
]
