from django.shortcuts import render
from paginas.models import Paginas, Secciones
from paginas.forms import Pagina_form
from django.http import HttpResponse
from perfiles.models import Perfiles
#from usuarios.models import Usuarios


# Create your views here.       
def listar_paginas(request):
    paginas = Paginas.objects.order_by('-fecha')
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    context = {'paginas':paginas, 'secciones':secciones}
    return render(request, 'paginas.html', context=context)


def detalle_pagina(request, pk):
    try:
        pagina = Paginas.objects.get(id=pk)
        context = {'pagina':pagina}
        return render(request, 'detalle_pagina.html', context=context)
    except:
        context = {'error':'El Producto no existe'}
        return render(request, 'paginas.html', context=context)



def crear_pagina(request):
    if request.method == 'GET':
        form = Pagina_form()
        secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
        context = {'form':form, 'secciones':secciones}
        return render(request, 'crear_pagina.html', context=context)
    elif request.method == 'POST':        
        form = Pagina_form(request.POST, request.FILES)
        secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
        if form.is_valid():
            nueva_pagina = Paginas.objects.create(
                titulo = form.cleaned_data['titulo'],
                autor = form.cleaned_data['autor'],
                fecha = form.cleaned_data['fecha'],
                copete = form.cleaned_data['copete'],
                cuerpo = form.cleaned_data['cuerpo'],
                imagen = form.cleaned_data['imagen'], 
                imagen_epigrafe = form.cleaned_data['imagen_epigrafe'],                
                habilitada = form.cleaned_data['habilitada'],
            )
            context = {'nueva_pagina':nueva_pagina, 'secciones':secciones}
        else:
            context = {'errors':form.errors, 'secciones':secciones}
        return render(request, 'crear_pagina.html', context = context)

    else:
        return redirect('login')

def borrar_pagina(request, pk):
    try:
        if request.method == 'GET':
            pagina = Paginas.objects.get(id=pk)
            context = {'pagina':pagina}
        else:
            pagina = Paginas.objects.get(id=pk)
            pagina.delete()
            context = {'message':'Pagina eliminada correctamente'}
        return render(request, 'borrar_pagina.html', context=context)
    except:
        context = {'error':'El Producto no existe'}
        return render(request, 'borrar_pagina.html', context=context)


def actualizar_pagina(request, pk):
    try:
        if request.method == 'GET':
            pagina = Paginas.objects.get(id=pk)
            context = {'pagina':pagina}
        else:
            pagina = Paginas.objects.get(id=pk)
            pagina.update()
            context = {'message':'La pagina ha sido actualizada'}
        return render(request, 'actualizar_pagina.html', context=context)
    except:
        context = {'error':'Pagina NO actualizada'}
        return render(request, 'actualizar_pagina.html', context=context)


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