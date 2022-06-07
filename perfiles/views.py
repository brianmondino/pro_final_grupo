from django.shortcuts import render
from perfiles.models import Perfiles
from perfiles.forms import Perfil_form
from django.http import HttpResponse


# Create your views here.       
def listar_perfiles(request):
    perfiles = Perfiles.objects.all()
    context = {'perfiles':perfiles}
    return render(request, 'perfiles.html', context=context)

def crear_perfil(request):
    if request.method == 'GET':
        form = Perfil_form()
        context = {'form':form}
        return render(request, 'crear_perfil.html', context=context)
    elif request.method == 'POST':        
        form = Perfil_form(request.POST)
        if form.is_valid():
            nuevo_perfil = Perfiles.objects.create(
                nombre = form.cleaned_data['nombre'],
                habilitado = form.cleaned_data['habilitado'],
                tipo = form.cleaned_data['tipo'],
            )
            context = {'nuevo_perfil':nuevo_perfil}
        else:
            context = {'errors':form.errors}
        return render(request, 'crear_perfil.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')