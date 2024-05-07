# Proyecto Django

Este es un proyecto Django para gestionar productos y categorías.

## Instalación

1. Clona el repositorio de GitHub:
  - git clone git@github.com:Lautaro-Palacios/proyect_Django.git
2. Instala las dependencias del proyecto:
  - pip install -r requirements.txt
3. Realiza las migraciones de la base de datos:
  -python manage.py migrate
4. Inicia el servidor de desarrollo:
  -python manage.py runserver

## Entorno virtual

Es recomendable utilizar un entorno virtual para este proyecto. Sigue estos pasos para crear y activar uno:

1. Instala `virtualenv` si aún no lo tienes:
  - pip install virtualenv

2. Crea un nuevo entorno virtual en el directorio del proyecto:

  -virtualenv venv


3. Activa el entorno virtual:

- En Windows:
  venv\Scripts\activate

  
- En macOS y Linux:
  source venv/bin/activate




## Estructura del proyecto

- `manage.py`: Archivo principal de gestión del proyecto Django.
- `product/`: Aplicación Django para la gestión de productos.
- `category/`: Aplicación Django para la gestión de categorías.
- `templates/`: Directorio para las plantillas HTML.
- `static/`: Directorio para archivos estáticos como CSS, JavaScript, etc.
- `db.sqlite3`: Base de datos SQLite para el proyecto.

## Funcionalidades

### Productos

- Listar todos los productos
- Ver detalles de un producto específico
- Crear un nuevo producto
- Actualizar un producto existente
- Eliminar un producto

### Categorías

- Listar todas las categorías
- Ver detalles de una categoría específica
- Crear una nueva categoría
- Actualizar una categoría existente
- Eliminar una categoría

## Tecnologías utilizadas

- Django: Framework web de Python
- SQLite: Sistema de gestión de bases de datos
- HTML/CSS: Para la presentación de las páginas web
- Bootstrap: Framework de CSS para el diseño responsive

## Contribuir

Si quieres contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`)
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Créditos

Desarrollado por Palacios Lautaro

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.


