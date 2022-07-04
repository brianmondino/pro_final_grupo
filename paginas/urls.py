from django.urls import path
from paginas.views import actualizar_pagina, listar_paginas, crear_pagina, buscar_pagina, detalle_pagina, borrar_pagina, valorar_pagina, listar_paginas2, actualiza_vista
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', listar_paginas, name = 'paginas'),
    path('<int:seccion_id>/', listar_paginas, name = 'paginas'),
    path('crear-pagina/', crear_pagina, name = 'crear_pagina'),
    path('buscar-pagina/', buscar_pagina, name = 'buscar_pagina'),
    path('detalle-pagina/<int:pk>/', detalle_pagina, name = 'detalle_pagina'),
    path('borrar-pagina/<int:pk>/', borrar_pagina, name = 'borrar_pagina'),
    path('actualizar-pagina/<int:pk>/', actualizar_pagina, name = 'actualizar_pagina'),
    path('valorar-pagina/', valorar_pagina, name = 'valorar_pagina'),
    path('listar-paginas2/', listar_paginas2, name = 'listar_paginas2'),
    path('actualiza-vista/<int:pk>/', actualiza_vista, name='actualiza_vista'),

]