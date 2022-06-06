from django.urls import path

from usuarios.views import listar_usuarios, crear_usuario

urlpatterns =[
    path('', listar_usuarios, name = 'usuarios'),
    path('crear-usuario/', crear_usuario, name = 'crear_usuario'),
]