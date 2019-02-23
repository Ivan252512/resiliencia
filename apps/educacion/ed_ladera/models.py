from django.db import models

# Create your models here.

class LaderaDefEd(models.Model):
    termino = models.CharField(max_length=30)
    definicion = models.CharField(max_length=300)
