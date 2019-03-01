from django.db import models

# Create your models here.

class VolcanDefAc(models.Model):
    subtitulo = models.CharField(max_length=80)
    parrafo = models.CharField(max_length=800)

# Create your models here.
class PostAcVolcan(models.Model):
    subtitulo = models.CharField(max_length=80, null=True, blank=True)
    parrafo = models.CharField(max_length=800, null=True, blank=True)
    descripcionImagen = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to = 'image/', null=True, blank=True)