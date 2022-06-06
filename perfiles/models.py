from django.db import models

# Create your models here.
class Perfiles(models.Model):
    nombre = models.CharField(max_length=100)
    habilitado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'