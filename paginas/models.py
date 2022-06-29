from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Secciones(models.Model):
    nombre = models.CharField(max_length=100)
    habilitada = models.BooleanField(default=False)
    tstamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'seccion'
        verbose_name_plural = 'secciones'
    def __str__(self):
        return self.nombre

class Paginas(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    secciones = models.ManyToManyField(Secciones)
    fecha = models.DateTimeField()
    copete = models.CharField(max_length=500)
    cuerpo = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes', blank=True)
    imagen_epigrafe = models.CharField(max_length=50, blank=True, null=True)    
    habilitada = models.BooleanField(default=False)
    votos = models.IntegerField(default=0)
    puntaje = models.IntegerField(default=0)
    puntaje_promedio = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    tstamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
    def __str__(self):
        return self.titulo