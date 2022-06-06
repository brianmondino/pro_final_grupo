from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    clave = models.CharField(max_length=20)
    habilitado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'