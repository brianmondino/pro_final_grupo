from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    clave = models.CharField(max_length=20)
    perfilid = models.IntegerField(default=0)
    habilitado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='imagenes', blank=True)
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'