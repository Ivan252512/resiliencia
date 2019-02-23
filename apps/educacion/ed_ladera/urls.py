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
from .views import ed_ladera, ed_ladera_post, ed_ladera_edit, ed_ladera_delete

urlpatterns = [
    path('ed_ladera', ed_ladera, name='ed_ladera'),
    path('ed_ladera_post/', ed_ladera_post, name='ed_ladera_post'),
    path('ed_ladera_post/<int:pk>/edit/', ed_ladera_edit, name='ed_ladera_edit'),
    path('ed_ladera_post/<int:pk>/delete/', ed_ladera_delete, name='ed_ladera_delete'),
]
