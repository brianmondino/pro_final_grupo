from django.shortcuts import render
from usuarios.models import Usuarios
from usuarios.forms import Usuario_form


# Create your views here.       
def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    context = {'usuarios':usuarios}
    return render(request, 'usuarios.html', context=context)

def crear_usuario(request):
    if request.method == 'GET':
        form = Usuario_form()
        context = {'form':form}
        return render(request, 'crear_usuario.html', context=context)
    elif request.method == 'POST':        
        form = Usuario_form(request.POST, request.FILES)
        if form.is_valid():
            nuevo_usuario = Usuarios.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                nickname = form.cleaned_data['nickname'],
                email = form.cleaned_data['email'],
                clave = form.cleaned_data['clave'],
                perfilid = form.cleaned_data['perfilid'],
                imagen = form.cleaned_data['imagen'],
                habilitado = form.cleaned_data['habilitado'],
            )
            context = {'nuevo_usuario':nuevo_usuario}
        else:
            context = {'errors':form.errors}
        return render(request, 'crear_usuario.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')