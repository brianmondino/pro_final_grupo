from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from paginas.models import Paginas

def index(request):
    paginas = Paginas.objects.order_by('-fecha')
    context = {'paginas':paginas}
    return render(request, 'index.html', context=context)    