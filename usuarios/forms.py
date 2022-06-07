from django import forms
from usuarios.models import Usuarios

class Usuario_form(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'