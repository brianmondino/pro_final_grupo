from django.db import models

# Create your models here.
class Perfiles(models.Model):
    nombre = models.CharField(max_length=100)
    habilitado = models.BooleanField(default=False)
<<<<<<< HEAD
    tipo = models.CharField(max_length=1,blank=True)
=======
>>>>>>> 9e179c583b96e45c35c03d0ac44485d7d6f12437
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'