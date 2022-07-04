from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from paginas.models import Paginas, Secciones
from paginas.forms import Pagina_form
from django.http import HttpResponse
from perfiles.models import Perfiles
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#@login_required       
def listar_paginas(request, seccion=""):
    if seccion == "":
        paginas = Paginas.objects.filter(habilitada=True).order_by('-fecha')
    else:
        paginas = Paginas.objects.filter(habilitada=True, secciones__id=seccion).order_by('-fecha')
    pagina = request.GET.get('page', 1)
    paginador = Paginator(paginas, 1)
    try:
        paginas = paginador.page(pagina)
    except PageNotAnInteger:
        paginas = paginador.page(1)
    except EmptyPage:
        paginas = paginador.page(paginador.num_pages)
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    context = {'paginas':paginas, 'secciones':secciones}
    return render(request, 'paginas.html', context=context)

def detalle_pagina(request, pk):
    try:
        pagina = Paginas.objects.get(id=pk)
        pagina.valoracion = pagina.puntaje / pagina.votos
        secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
        context = {'pagina':pagina, 'secciones':secciones}
        return render(request, 'detalle_pagina.html', context=context)
    except:
        context = {'error':'La página no existe'}
        return render(request, 'paginas.html', context=context)

###############################################################
@login_required
def listar_paginas2(request): # borré seccion=""
    paginas = Paginas.objects.all # saque order_by('-fecha')
    context = {'paginas':paginas}
    return render(request, 'listar_paginas2.html', context=context)


















def detail_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["data"] = Paginas.objects.get(id = pk)
    return render(request, "detail_view.html", context)

# update view for details
def update_view(request, pk):
    obj = get_object_or_404(Paginas, id = pk)
    form = Pagina_form(request.POST or None, instance = obj)
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    context = {'form':form, 'secciones':secciones}
    if form.is_valid():
        form.save()
    return render(request, "update_view.html", context)


################################################################

@login_required
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

def buscar_pagina(request):
    palabra_busqueda = request.GET['buscar']
    paginas = Paginas.objects.filter(titulo__icontains = palabra_busqueda)
    perfil_buscar = Perfiles.objects.filter(nombre__icontains = palabra_busqueda)
    if paginas.exists():
        context = {'paginas':paginas}
        return render(request, 'buscar_paginas.html', context = context)
    elif perfil_buscar.exists():
            context = {'perfil_buscar':perfil_buscar}
            return render(request, 'buscar_perfil.html', context = context)
    else:
        context = {'errors':'No se encontro el valor correcto'}
    return render(request, 'buscar_paginas.html', context = context)


