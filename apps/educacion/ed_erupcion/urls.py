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
from .views import ed_erupcion, ed_erupcion_post, ed_erupcion_edit, ed_erupcion_delete

urlpatterns = [
    path('ed_erupcion', ed_erupcion, name='ed_erupcion'),
    path('ed_erupcion_post/', ed_erupcion_post, name='ed_erupcion_post'),
    path('ed_erupcion_post/<int:pk>/edit/', ed_erupcion_edit, name='ed_erupcion_edit'),
    path('ed_erupcion_post/<int:pk>/delete/', ed_erupcion_delete, name='ed_erupcion_delete'),
]
