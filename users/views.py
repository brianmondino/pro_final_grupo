from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
#from platformdirs import user_cache_path

from users.models import UserProfile

from .forms import UserLoginForm, UserSignUpForm, UserChangePassword


def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, 'Has iniciado sesion correctamente')
            return redirect('index')
        else:
            messages.warning(
                request, 'Correo Electronico o Contraseña invalida')
            return redirect('index')

    messages.error(request, 'Formulario Invalido')
    return redirect('index')


def signup_view(request):
    signup_form = UserSignUpForm(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        first_name = signup_form.cleaned_data.get('first_name')
        last_name = signup_form.cleaned_data.get('last_name')
        password = signup_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            return redirect('index')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})

    messages.warning(request, 'Las Contraseñas no coinciden')
    return redirect('index')

def changepassword(request):
    ChangePassword = UserChangePassword(request.POST or None)
    if ChangePassword.is_valid():
        old_password = ChangePassword.cleaned_data.get('old_password')
        new_password = ChangePassword.cleaned_data.get('new_password')
        reenter_password   = ChangePassword.cleaned_data.get('reenter_password')
        try:
            user = get_user_model().objects.update(
                password=make_password(new_password),
            )
            messages.success(request, 'Contraseña cambiada, ingresa nuevamente')
            #login(request, user)
            return redirect('index')
        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})
    messages.warning(request, 'Las Contraseñas no coinciden')
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='index')
def profile_view(request):
    return render(request, 'user/profile.html')

@login_required(login_url='index')
def user_list(request): 
    usuarios = UserProfile.objects.all
    context = {'users':usuarios}
    return render(request,'user/user_list.html',context=context)    


def user_detail(request, slug):
    user_detail = get_object_or_404(get_user_model(), slug=slug)
    if not request.user.is_authenticated:
        messages.warning(request, 'Debes iniciar sesion')

    return render(request, 'user/user_detail.html', {'user_detail': user_detail})


@login_required(login_url='index')
def follow(request, slug):
    to_follow = get_object_or_404(get_user_model(), slug=slug)
    if to_follow.is_follower(request.user):
        to_follow.followers.remove(request.user)
    else:
        to_follow.followers.add(request.user)
    to_follow.save
    return redirect(to_follow)