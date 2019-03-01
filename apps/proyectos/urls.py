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
from .views import proyectos, proyectos_post, proyectos_edit, proyectos_delete

urlpatterns = [
    path('proyectos', proyectos, name='proyectos'),
    path('proyectos_post/', proyectos_post, name='proyectos_post'),
    path('proyectos_post/<int:pk>/edit/', proyectos_edit, name='proyectos_edit'),
    path('proyectos_post/<int:pk>/delete/', proyectos_delete, name='proyectos_delete'),
]
