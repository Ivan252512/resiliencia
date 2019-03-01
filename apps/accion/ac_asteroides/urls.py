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
from .views import ac_asteroide, ac_asteroide_post, ac_asteroide_edit, ac_asteroide_delete

urlpatterns = [
    path('ac_asteroide', ac_asteroide, name='ac_asteroide'),
    path('ac_asteroide_post/', ac_asteroide_post, name='ac_asteroide_post'),
    path('ac_asteroide_post/<int:pk>/edit', ac_asteroide_edit, name='ac_asteroide_edit'),
    path('ac_asteroide_post/<int:pk>/delete', ac_asteroide_delete, name='ac_asteroide_delete'),
]
