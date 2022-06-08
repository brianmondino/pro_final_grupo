#Superusuario
#usuario: proyectofinal
#password: abc123


## Instalacion:
    * pip install -r requirements.txt
    * python manage.py migrate
    * python manage.py runserver
    * python -m pip install Pillow

## Uso y funcionalidad
Todos los templates heredan caracteristicas de base.html (carpeta templates)

Inicio

	Landing page del proyecto - index.html (carpeta templates)


Usuarios

	Listado de los usuarios - usuarios.html (carpeta templates) 
		presenta los usuarios existentes en la tabla de usuarios de la BD

			generada desde la vista listar_usuarios (views.py en la carpeta usuarios)
			usando los campos del modelo Usuarios (models.py en la carpeta usuarios)
		


Nuevo Usuario

	Formato de entrada de usuarios - crear_usuario.html (carpeta templates) 
		presenta la forma de entrada de datos para la tabla de usuarios de la BD

			generada y validada desde la vista crear_usuario (views.py en la carpeta usuarios)
			usando los campos del modelo Usuarios (models.py en la carpeta usuarios)


Paginas

	Listado de los usuarios - paginas.html (carpeta templates) 
		presenta las paginas existentes en la tabla de paginas de la BD

			generada desde la vista listar_pagina (views.py en la carpeta paginas)
			usando los campos del modelo Paginas (models.py en la carpeta paginas)


Nueva Pagina

	Formato de entrada de paginas - crear_pagina.html (carpeta templates) 
		presenta la forma de entrada de datos para la tabla de paginas de la BD

			generada y validada desde la vista crear_pagina (views.py en la carpeta paginas)
			usando los campos del modelo Paginas (models.py en la carpeta paginas)


Perfiles

	Listado de los perfiles - perfiles.html (carpeta templates) 
		presenta los perfiles existentes en la tabla de paginas de la BD

			generada desde la vista listar_perfiles (views.py en la carpeta perfiles)
			usando los campos del modelo Perfiles (models.py en la carpeta perfiles)


Nuevo Perfil

	Formato de entrada de perfiles - crear_perfil.html (carpeta templates) 
		presenta la forma de entrada de datos para la tabla de perfiles de la BD

			generada y validada desde la vista crear_perfil (views.py en la carpeta perfiles)
			usando los campos del modelo Perfiles (models.py en la carpeta perfiles)


Search

	La funcionalidad del boton de SEACH del navbar del template base.html (carpeta templates)
	esta basada en la vista buscar_pagina (views.py en la carpeta paginas)
		La vista busca el texto introducido en las 3 tablas (paginas, perfiles y usuarios)
		
		si la busqueda en paginas es exitosa se presenta el resultado en buscar_paginas.html (carpeta templates)
		si no es exitosa, se verifica si la busqueda en perfiles es exitosa, si es asi se presenta el resultado en buscar_perfil.html (carpeta templates)
		si no es exitosa, se verifica si la busqueda en usuarios es exitosa, si es asi se presenta el resultado en buscar_usuario.html (carpeta templates)
		si no es exitosa, se presenta un error generico en buscar_paginas.html (carpeta templates)