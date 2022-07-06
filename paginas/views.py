from sqlite3 import TimestampFromTicks
from django.shortcuts import render, get_object_or_404, redirect
from paginas.models import Paginas, Secciones
from paginas.forms import Pagina_form, Seccion_form
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
#@login_required       
def listar_paginas(request, seccion_id=""):
    if seccion_id == "":
        paginas = Paginas.objects.filter(habilitada=True).order_by('-fecha')
    else:
        paginas = Paginas.objects.filter(habilitada=True, secciones__id=seccion_id).order_by('-fecha')
        seccion = Secciones.objects.get(id=seccion_id)
    pagina = request.GET.get('page', 1)
    paginador = Paginator(paginas, 4)
    try:
        paginas = paginador.page(pagina)
    except PageNotAnInteger:
        paginas = paginador.page(1)
    except EmptyPage:
        paginas = paginador.page(paginador.num_pages)
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    if seccion_id == "":
        context = {'paginas':paginas, 'secciones':secciones}
    else:
        context = {'paginas':paginas, 'secciones':secciones, 'seccion':seccion}
    return render(request, 'paginas.html', context=context)

@login_required
def listar_paginas2(request): # borré seccion=""
    paginas = Paginas.objects.all # saque order_by('-fecha')
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    context = {'paginas':paginas, 'secciones':secciones}
    return render(request, 'listar_paginas2.html', context=context)    


def detalle_pagina(request, pk):
    try:
        pagina = Paginas.objects.get(id=pk)
        if pagina.votos > 0:
            pagina.valoracion = pagina.puntaje / pagina.votos
        else: 
            pagina.valoracion = 0
        secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
        context = {'pagina':pagina, 'secciones':secciones}
        return render(request, 'detalle_pagina.html', context=context)
    except:
        context = {'error':'La página no existe'}
        return render(request, 'paginas.html', context=context)

def valorar_pagina(request):
    puntaje=request.POST.get('puntaje')
    id=request.POST.get('id')
    pagina = Paginas.objects.get(id=id)
    votos = pagina.votos
    nuevos_votos = votos + 1
    nuevo_puntaje = pagina.puntaje + int(puntaje)
    pagina.votos = nuevos_votos
    pagina.puntaje = nuevo_puntaje
    pagina.save()

    print(puntaje, id)
    return JsonResponse({'texto': 'Su valoracion fue recibida. Muchas gracias.'})



###############################################################
@login_required
def listar_paginas2(request): # borré seccion=""
    paginas = Paginas.objects.all # saque order_by('-fecha')
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    context = {'paginas':paginas, 'secciones':secciones}
    return render(request, 'listar_paginas2.html', context=context)



# update view for details
def actualiza_vista(request, pk):
    obj = get_object_or_404(Paginas, id = pk)
    if request.method == "POST":
        form = Pagina_form(request.POST, request.FILES, instance = obj)
        if form.is_valid():
            form.save()
            return redirect("/paginas/listar-paginas2/")
    else:
        pagina = Paginas.objects.get(id=pk)
        secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
        form = Pagina_form(instance = pagina)
        context = {'form':form,'id':pk, 'secciones':secciones}
        return render(request, 'actualiza_vista.html',context)




################################################################
class crear_pagina(LoginRequiredMixin, CreateView):
    model = Paginas
    template_name = 'crear_pagina.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')


def borrar_pagina(request, pk):
    try:
        if request.method == 'GET':
            pagina = Paginas.objects.get(id=pk)
            context = {'pagina':pagina}
            return render(request, 'borrar_pagina.html', context=context)
        else:
            pagina = Paginas.objects.get(id=pk)
            pagina.delete()
            paginas = Paginas.objects.filter(habilitada=True).order_by('-fecha')
            secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
            context = {'paginas':paginas, 'secciones':secciones}
            return render(request, 'listar_paginas2.html', context=context)
        
    except:
        context = {'error':'La pagina no existe'}
        return render(request, 'borrar_pagina.html', context=context)

# def buscar_pagina(request):
#     palabra_busqueda = request.GET['buscar']
#     paginas = Paginas.objects.filter(titulo__icontains = palabra_busqueda)
#     if paginas.exists():
#         print(1)
#         context = {'paginas':paginas}
#         return render(request, 'buscar_paginas.html', context = context)
#     else:
#         print(2)
#         context = {'errors':'No se encontro el valor correcto'}
#     return render(request, 'buscar_paginas.html', context = context)

def buscar_pagina(request):
    paginas = Paginas.objects.filter(titulo__icontains=request.GET['buscar'])
    if paginas.exists():
        context = {'paginas':paginas}
    else:
        context = {'errors':'No se encontro la página'}
    return render(request, 'buscar_paginas.html', context = context)

###################################################################
###################################################################
###################################################################
#secciones // crear seccion // listar seccion 

@login_required
def crear_seccion(request):
    if request.method == 'GET':
        form = Seccion_form()
        #secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
        context = {'form':form}
        return render(request, 'crear_seccion.html', context=context)
    elif request.method == 'POST':        
        form = Seccion_form(request.POST, request.FILES)
        secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
        if form.is_valid():
            nueva_seccion = Secciones.objects.create(
                nombre = form.cleaned_data['nombre'],
                habilitada = form.cleaned_data['habilitada'],
                #tstamp = form.cleaned_data['tstamp'],
            )
            context = {'nueva_seccion':nueva_seccion, 'secciones':secciones}
        else:
            context = {'errors':form.errors, 'secciones':secciones}
        return render(request, 'crear_seccion.html', context = context)

    else:
        return redirect('login')




@login_required
def listar_seccion(request): # borré seccion=""
    secciones = Secciones.objects.all
    context = {'secciones':secciones}
    return render(request, 'listar_seccion.html', context=context)


###################################################################
###################################################################
###################################################################