from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
		return HttpResponse('Bienvenidos al inicio del Proyecto Final')

def index(request):
    return render(request, 'index.html')