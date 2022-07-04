from django.urls import path
from paginas.views import listar_paginas, crear_pagina, buscar_pagina, detalle_pagina, borrar_pagina, listar_paginas2, update_view, detail_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', listar_paginas, name = 'paginas'),
    path('<int:seccion>/', listar_paginas, name = 'paginas'),
    path('crear-pagina/', crear_pagina, name = 'crear_pagina'),
    path('buscar-pagina/', buscar_pagina, name = 'buscar_pagina'),
    path('detalle-pagina/<int:pk>/', detalle_pagina, name = 'detalle_pagina'),
    path('borrar-pagina/<int:pk>/', borrar_pagina, name = 'borrar_pagina'),
    path('listar-paginas2/', listar_paginas2, name = 'listar_paginas2'),
    path('update-view/<int:pk>/', update_view, name='update_view'),
    path('<int:pk>/', detail_view ),
]