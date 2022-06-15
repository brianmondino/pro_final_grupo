from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from paginas.models import Paginas

from django.contrib.auth.forms import AuthenticationForm
#from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
#from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

#class CustomAuthenticationForm(AuthenticationForm):
#    class Meta:
#        model = User
#        fields = ['username', 'password']


def login_view(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'login/login.html',context=context)
        


def index(request):
    paginas = Paginas.objects.order_by('-fecha')
    context = {'paginas':paginas}
    return render(request, 'index.html', context=context)    