from django.urls import path
<<<<<<< HEAD

from paginas.views import listar_paginas, crear_pagina, buscar_pagina
=======
from paginas.views import listar_paginas, crear_pagina, buscar_pagina
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 9e179c583b96e45c35c03d0ac44485d7d6f12437

urlpatterns =[
    path('', listar_paginas, name = 'paginas'),
    path('crear-pagina/', crear_pagina, name = 'crear_pagina'),
    path('buscar-pagina/', buscar_pagina, name = 'buscar_pagina'),
]