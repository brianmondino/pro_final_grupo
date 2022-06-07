from django import forms
from perfiles.models import Perfiles

class Perfil_form(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = '__all__'