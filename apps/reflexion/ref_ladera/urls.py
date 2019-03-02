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
from .views import ref_ladera, ref_ladera_post, ref_ladera_edit, ref_ladera_delete, ref_ladera_general_post, ref_ladera_general_edit, ref_ladera_general_delete

urlpatterns = [
    path('ref_ladera', ref_ladera, name='ref_ladera'),
    path('ref_ladera_post/', ref_ladera_post, name='ref_ladera_post'),
    path('ref_ladera_post/<int:pk>/edit/', ref_ladera_edit, name='ref_ladera_edit'),
    path('ref_ladera_post/<int:pk>/delete/', ref_ladera_delete, name='ref_ladera_delete'),


    path('ref_ladera_general_post/', ref_ladera_general_post, name='ref_ladera_general_post'),
    path('ref_ladera_general_post/<int:pk>/edit/', ref_ladera_general_edit, name='ref_ladera_general_edit'),
    path('ref_ladera_general_post/<int:pk>/delete/', ref_ladera_general_delete, name='ref_ladera_general_delete'),
]
