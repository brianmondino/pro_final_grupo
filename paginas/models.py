from django.db import models

# Create your models here.
class Paginas(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    copete = models.CharField(max_length=255)
    cuerpo = models.CharField(max_length=2000)
<<<<<<< HEAD
    imagen = models.CharField(max_length=50)
=======
    imagen = models.ImageField(upload_to='imagenes', blank=True)
    imagen_epigrafe = models.CharField(max_length=50, blank=True, null=True)    
>>>>>>> 9e179c583b96e45c35c03d0ac44485d7d6f12437
    habilitada = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'