from django.shortcuts import redirect, render
from paginas.models import Paginas
from paginas.forms import Pagina_form
from django.http import HttpResponse
from perfiles.models import Perfiles
from usuarios.models import Usuarios


# Create your views here.       
def listar_paginas(request):
    paginas = Paginas.objects.order_by('-fecha')
    context = {'paginas':paginas}
    return render(request, 'paginas.html', context=context)

def crear_pagina(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = Pagina_form()
            context = {'form':form}
            return render(request, 'crear_pagina.html', context=context)
        elif request.method == 'POST':        
            form = Pagina_form(request.POST, request.FILES)
            if form.is_valid():
                nueva_pagina = Paginas.objects.create(
                titulo = form.cleaned_data['titulo'],
                fecha = form.cleaned_data['fecha'],
                copete = form.cleaned_data['copete'],
                cuerpo = form.cleaned_data['cuerpo'],
                imagen = form.cleaned_data['imagen'], 
                imagen_epigrafe = form.cleaned_data['imagen_epigrafe'],                
                habilitada = form.cleaned_data['habilitada'],)
                context = {'nueva_pagina':nueva_pagina}
            else:
                context = {'errors':form.errors}
                return render(request, 'crear_pagina.html', context = context)
        else:
            return HttpResponse('Only GET and POST methods are allowed')
    else:
        return redirect('login')

def buscar_pagina(request):
    palabra_busqueda = request.GET['buscar']
    paginas = Paginas.objects.filter(titulo__icontains = palabra_busqueda)
    perfil_buscar = Perfiles.objects.filter(nombre__icontains = palabra_busqueda)
    perfil_usuario = Usuarios.objects.filter(nombre__icontains = palabra_busqueda)
    
    if paginas.exists():
        context = {'paginas':paginas}
        return render(request, 'buscar_paginas.html', context = context)

    elif perfil_buscar.exists():
            context = {'perfil_buscar':perfil_buscar}
            return render(request, 'buscar_perfil.html', context = context)
    elif perfil_usuario.exists():
            context = {'perfil_usuario':perfil_usuario}
            return render(request, 'buscar_usuario.html', context = context)
    else:
        context = {'errors':'No se encontro el valor correcto'}
    return render(request, 'buscar_paginas.html', context = context)