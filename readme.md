#Superusuario
#usuario: coderhouse@mail.com
#password: coder123


## Presentación
Tech Yes! es un pagina web joven creada por tres entusiastas de la programación. El sitio está basado en un backend the python y framework de django y cuyo propósito es poder representar en una base practica los contenidos transmitidos a través de las lecciones de CoderHouse. 
Confiamos en que lo observado en el sitio pueda satisfacer sus expectativas! 
Agradecemos especialmente a Luca Citta Giordano y a Ramiro Peidro por su asistencia en el proyecto.
Muchas Gracias.



## Instalacion:
    * pip install -r requirements.txt
    * python manage.py makemigrations
	* python manage.py migrate
    * python manage.py runserver
    * python -m pip install Pillow

## Uso y funcionalidad
Dependiendo de la forma de presentacion los templates heredan caracteristicas de base.html o de base_backoffice.html (carpeta templates)
Se precarga en esos templates los archivos de CSS y de JS que estan en la carpera static


Inicio

	Landing page del proyecto - index.html (carpeta templates)


INICIAR SESION / REGISTRARSE

	Ventana modal con los formularios de LOGIN y REGISTRO - login.html ( carpeta templates/users) 
		un template con doble funcion que permite al usuario LOGEARSE o REGISTRARSE en la pagina (BD User Profiles)

			generada y validada desde las vistas signup_view y login_view (views.py en la carpeta usuarios)
			usando los campos del modelo UserProfile (models.py en la carpeta users)


MENU

	Opciones que permiten filtrar las publicaciones realizadas segun la seccion a la que pertenecen tales publicaciones.
	La opcion HOME, siempre regresa a la pagina principal
	Las siguientes opciones son dinamicas, se generan a partir de la tabla SECCIONES, filtrando solo aquellas que esten habilitadas
	Una opcion MAS, aparece solo cuando el usuario esta logueado y dentro de esta, habra otras opciones, algunas seran visibles solo si el usuario es SUPERUSER
		Paginas
			Listar paginas - template listar_paginas2.html (tabla que lista las paginas y permite hacer un mantenimiento de las mismas)
			Crear pagina - template crear_pagina.html (formato que permite ingresar una nueva publicacion)

		Secciones
			Listar secciones - template listar_seccion.html (tabla que lista todas las seccion y permite hacer un mantenimiento de las mismas)
			Crear seccion - template crear_seccion.html (formato para ingresar una nueva seccion a la bd )

		Usuarios
			Listar usuarios - template user/user_list.html (tabla que lista todas los usuarios y permite hacer un mantenimiento de las mismos)
			Crear usuario - se usa la misma ventana modal de registro de usuario mencionada anteriormente



Search

	La funcionalidad del boton de SEACH del navbar del template base.html (carpeta templates)
	esta basada en la vista buscar_pagina (views.py en la carpeta paginas)
		La vista busca el texto introducido en la tabla (paginas)
		
		si la busqueda en paginas es exitosa se presenta el resultado en buscar_paginas.html (carpeta templates)

# Carpetas y archivos
media

	Carpeta que contiene todas las imagenes que se integran a los registros de la BD


paginas

	Archivos

		__init__.py
		admin.py
		apps.py
		forms.py
		models.py
		urls.py
		views.py


users

	Archivos

		__init__.py
		admin.py
		apps.py
		context_processors.py
		forms.py
		models.py
		tests.py
		urls.py
		views.py


templates

	Archivos
		user
			borrar_usuario.html
			change_password.html
			login.html
			profile.html
			user_detail.html
			user_edit.html
			user_edit2-html
			user_list.html
		actualiza_vista.html
		base_backoffice.html	
		base.html
		borrar_pagina.html
		buscar_paginas.html
		crear_pagina.html
		detalle_pagina.html
		header.html
		index.html
		listar_paginas2.html
		listar_seccion.html
		menu_celulares.html
		menu.html
		noticias.html
		pie.html
		sobrenosotros.html