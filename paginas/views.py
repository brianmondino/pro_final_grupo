from django.shortcuts import render
from paginas.models import Paginas
from paginas.forms import Pagina_form
from django.http import HttpResponse


# Create your views here.       
def listar_paginas(request):
    paginas = Paginas.objects.all()
    context = {'paginas':paginas}
    return render(request, 'paginas.html', context=context)

def crear_pagina(request):
    if request.method == 'GET':
        form = Pagina_form()
        context = {'form':form}
        return render(request, 'crear_pagina.html', context=context)
    elif request.method == 'POST':        
        form = Pagina_form(request.POST)
        if form.is_valid():
            nueva_pagina = Paginas.objects.create(
                titulo = form.cleaned_data['titulo'],
                copete = form.cleaned_data['copete'],
                cuerpo = form.cleaned_data['cuerpo'],
                fecha = form.cleaned_data['fecha'],
                habilitada = form.cleaned_data['habilitada'],
            )
            context = {'nueva_pagina':nueva_pagina}
        else:
            context = {'errors':form.errors}
        return render(request, 'crear_pagina.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')

def buscar_pagina(request):
    paginas = Paginas.objects.filter(titulo__icontains=request.GET['buscar'])
    if paginas.exists():
        context = {'paginas':paginas}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'buscar_paginas.html', context = context)