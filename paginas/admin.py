from django.contrib import admin
from paginas.models import Paginas, Secciones

@admin.register(Paginas)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("identifier",)}
#admin.site.register(Paginas)

admin.site.register(Secciones)