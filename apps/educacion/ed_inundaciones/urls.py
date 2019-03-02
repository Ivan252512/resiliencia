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
from .views import ed_inundacion, ed_inundacion_post, ed_inundacion_edit, ed_inundacion_delete, ed_inundacion_general_post, ed_inundacion_general_edit, ed_inundacion_general_delete

urlpatterns = [
    path('ed_inundacion', ed_inundacion, name='ed_inundacion'),
    path('ed_inundacion_post/', ed_inundacion_post, name='ed_inundacion_post'),
    path('ed_inundacion_post/<int:pk>/edit', ed_inundacion_edit, name='ed_inundacion_edit'),
    path('ed_inundacion_post/<int:pk>/delete', ed_inundacion_delete, name='ed_inundacion_delete'),


    path('ed_inundacion_general_post/', ed_inundacion_general_post, name='ed_inundacion_general_post'),
    path('ed_inundacion_general_post/<int:pk>/edit', ed_inundacion_general_edit, name='ed_inundacion_general_edit'),
    path('ed_inundacion_general_post/<int:pk>/delete', ed_inundacion_general_delete, name='ed_inundacion_general_delete'),
]
