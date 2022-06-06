from django.urls import path

from paginas.views import listar_paginas, crear_pagina

urlpatterns =[
    path('', listar_paginas, name = 'paginas'),
    path('crear-pagina/', crear_pagina, name = 'crear_pagina'),
]