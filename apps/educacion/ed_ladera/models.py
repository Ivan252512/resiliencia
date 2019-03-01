from django.db import models

# Create your models here.

class LaderaDefEd(models.Model):
    termino = models.CharField(max_length=30)
    definicion = models.CharField(max_length=300)

# Create your models here.
class PostEdLadera(models.Model):
    subtitulo = models.CharField(max_length=80, null=True, blank=True)
    parrafo = models.CharField(max_length=800, null=True, blank=True)
    descripcionImagen = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to = 'image/', null=True, blank=True)