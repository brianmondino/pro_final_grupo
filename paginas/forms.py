from django import forms
from paginas.models import Paginas, Secciones

class Pagina_form(forms.ModelForm):
    class Meta:
        model = Paginas
        fields = '__all__'
#        secciones = forms.ModelMultipleChoiceField(queryset=Secciones.objects.all())


class Seccion_form(forms.ModelForm):
    class Meta:
        model = Secciones
        fields = '__all__'