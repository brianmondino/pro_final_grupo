from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='perfiles')
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80,default="")
    tipo = models.CharField(max_length=15,blank=True)
    imagen = models.ImageField(upload_to='imagenes', blank=True)
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'