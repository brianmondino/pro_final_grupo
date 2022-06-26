from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

    
class perfil_usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='perfil_usuario')
    phone = models.CharField(max_length=20)



#
#    class Meta:
#        verbosUserose_name_pluUserstr__(self):
#        return self.name

#    def get_absoluclass perfil_usuario(model.Model):
#        te_url(self):
#        return revUsers={"pk": self.pk})


# Create your models hclass perfil_usuario(model.Model): here.
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