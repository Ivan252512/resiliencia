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
from .views import ref_sismo, ref_sismo_post, ref_sismo_edit, ref_sismo_delete

urlpatterns = [
    path('ref_sismo', ref_sismo, name='ref_sismo'),
    path('ref_sismo_post/', ref_sismo_post, name='ref_sismo_post'),
    path('ref_sismo_post/<int:pk>/edit', ref_sismo_edit, name='ref_sismo_edit'),
    path('ref_sismo_post/<int:pk>/delete', ref_sismo_delete, name='ref_sismo_delete'),
]
