from django.db import models

# Create your models here.
class Perfiles(models.Model):
    nombre = models.CharField(max_length=100)
    habilitado = models.BooleanField(default=False)
    tipo = models.CharField(max_length=1,blank=True)
    imagen = models.ImageField(upload_to='imagenes', blank=True)
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'