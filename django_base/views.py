from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from paginas.models import Paginas,Secciones
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django_base.forms import Creacion_deUsuario

def modal(request):
    return render(request,'login/modal.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                paginas=Paginas.objects.all()
                secciones=Secciones.objects.all()
                context = {'message': 'Bienvenido!!','paginas':paginas,'secciones':secciones}
                return render(request,'index.html',context = context)
            else:
                context = {'error': 'Usuario no encontrado'}
                form : AuthenticationForm()
                return render(request,'login/login.html',context = context)                
        else:
            error = form.errors
            form : AuthenticationForm()
            context = {'error':error,'form':form}
            return render(request,'login/login.html',context = context)             
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'login/login.html',context=context)
        
def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = Creacion_deUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            paginas=Paginas.objects.all()
            context = {'message':'Usuario creado!','paginas':paginas}
            return render(request, 'index.html', context=context)
        else:
            error = form.errors.items
            form = Creacion_deUsuario()
            context = {'errors':error,'form':form}
            return render(request,'login/register.html',context=context)


    else:
        form=Creacion_deUsuario()
        context = {'form':form}
        return render(request,'login/register.html',context=context)

    

def index(request):
    paginas = Paginas.objects.order_by('-fecha')
    secciones = Secciones.objects.filter(habilitada=True).order_by('nombre')
    context = {'paginas':paginas, 'secciones':secciones}
    return render(request, 'index.html', context=context)