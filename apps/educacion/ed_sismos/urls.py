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
from .views import ed_sismo, ed_sismo_post, ed_sismo_edit, ed_sismo_delete

urlpatterns = [
    path('ed_sismo', ed_sismo, name='ed_sismo'),
    path('ed_sismo_post/', ed_sismo_post, name='ed_sismo_post'),
    path('ed_sismo_post/<int:pk>/edit', ed_sismo_edit, name='ed_sismo_edit'),
    path('ed_sismo_post/<int:pk>/delete', ed_sismo_delete, name='ed_sismo_delete'),
]
