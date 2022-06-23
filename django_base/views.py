from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from paginas.models import Paginas, Secciones

def index(request):
    paginas = Paginas.objects.order_by('-fecha')
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    context = {'paginas':paginas, 'secciones':secciones}
    return render(request, 'index.html', context=context)