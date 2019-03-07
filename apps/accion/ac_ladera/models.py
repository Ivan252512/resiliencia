from django.db import models

# Create your models here.

class LaderaDefAc(models.Model):
    subtitulo = models.CharField(max_length=80)
    parrafo = models.CharField(max_length=800)

# Create your models here.
class PostAcLadera(models.Model):
    subtitulo = models.CharField(max_length=80, null=True, blank=True)
    parrafo = models.CharField(max_length=800, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to = 'image/', null=True, blank=True)
    video = models.FileField(upload_to = 'video/', null=True, blank=True)