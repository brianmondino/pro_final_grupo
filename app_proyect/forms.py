from django import forms
from app_proyect.models import Products

class Product_form(forms.ModelForm):
	class Meta:
		model = Products
		fields = '__all__'