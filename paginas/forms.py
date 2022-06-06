from django import forms
from paginas.models import Paginas

class Pagina_form(forms.ModelForm):
    class Meta:
        model = Paginas
        fields = '__all__'