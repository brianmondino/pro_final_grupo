from django.urls import path
from paginas.views import listar_paginas, crear_pagina, buscar_pagina
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', listar_paginas, name = 'paginas'),
    path('crear-pagina/', crear_pagina, name = 'crear_pagina'),
    path('buscar-pagina/', buscar_pagina, name = 'buscar_pagina'),
]