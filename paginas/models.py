from django.db import models

# Create your models here.
class Paginas(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    copete = models.CharField(max_length=255)
    cuerpo = models.CharField(max_length=2000)
    imagen = models.CharField(max_length=50)
    habilitada = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'