from django.urls import path
from app_proyect.views import products, create_product, search_product_view

urlpatterns = [
	path('', products, name = 'products'),
	path('create-product/', create_product, name ='create_product'),
	path('search-product-view/', search_product_view, name = 'search_product_view'),
]