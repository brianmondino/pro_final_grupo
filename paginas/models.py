from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Paginas(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Users, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    copete = models.CharField(max_length=500)
    cuerpo = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes', blank=True)
    imagen_epigrafe = models.CharField(max_length=50, blank=True, null=True)    
    habilitada = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'