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
from apps.core.views import index, nosotros, proyecto, video_post, video_edit, video_delete, send_email

urlpatterns = [
    path('', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('proyecto/', proyecto, name='proyecto'),
    path('video_post/', video_post, name='video_post'),
    path('video_post/<int:pk>/edit/', video_edit, name='video_edit'),
    path('video_post/<int:pk>/delete/', video_delete, name='video_delete'),
    path('contacto/', send_email, name='send_email'),
]
