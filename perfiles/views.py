from django.shortcuts import render
from perfiles.models import Perfiles
from perfiles.forms import Perfil_form
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here. 
@login_required
def listar_perfiles(request):
    perfiles = Perfiles.objects.all()
    context = {'perfiles':perfiles}
    return render(request, 'perfiles.html', context=context)

@login_required
def crear_perfil(request):
    if request.method == 'GET':
        form = Perfil_form()
        context = {'form':form}
        return render(request, 'crear_perfil.html', context=context)
    elif request.method == 'POST':        
        form = Perfil_form(request.POST, request.FILES)
        if form.is_valid():
            nuevo_perfil = Perfiles.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellidos = form.cleaned_data['apellidos'],
                habilitado = form.cleaned_data['habilitado'],
                tipo = form.cleaned_data['tipo'],
                imagen = form.cleaned_data['imagen'], 
            )
            context = {'nuevo_perfil':nuevo_perfil}
        else:
            context = {'errors':form.errors}
        return render(request, 'crear_perfil.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')