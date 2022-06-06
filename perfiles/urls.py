from django.urls import path

from perfiles.views import listar_perfiles, crear_perfil

urlpatterns =[
    path('', listar_perfiles, name = 'perfiles'),
    path('crear-perfil/', crear_perfil, name = 'crear_perfil'),
]