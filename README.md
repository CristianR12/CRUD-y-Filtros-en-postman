# API para el registro de personas y tareas

## Información general:
El proyecto trata de una aplicación en la cual se pueden realizar las acciones básicas de una base de datos (CRUD) para registrar personas con su número de documento y que a estas personas puedan registrar tareas que tengan pendientes, con su respectiva fecha de entraga; esta información del documento y la fecha de entrega permite realizar diferentes filtrados de búsqueda.

El proyecto se desarorllo en el lenguaje de programación Pyhton, y actualmente el proyecto se encuentra desarrollado como un backend, cuyos endpoints pueden ser probados con Postman, en el enlace mostrado al final del documento.

## Herramientas utilizadas:
- PostgreSQL: Se utilivó la versión  para la creación de la base de datos relacional donde son almacenadas las personas y las tareas.
- Django REST Framework: Se utilizó este framework para poder realizar una aplicación web que siguiera el Modelo-Vista-Controlador (MVC) de forma eficiente.
- Postman: El software permitió probar los endpoints realizados para la API, que corresponden a las acciones de get, post, put y delete, tanto para personas como para tareas, de una forma rápida y fácil de documentar.

## Instalación/Prueba
Para la instalación o prueba de este proyecto, se puede realizar de dos formas:
### 1. Clonando el repositorio de GitHub:
Una vez se tenga una carpeta abierta en el IDE de preferencia, se puede abrir una terminal donde se ejecuten los siguientes comandos uno por uno:
git init
git clone https://github.com/CristianR12/CRUD-y-Filtros-en-postman.git
cd CRUD-y-Filtros-en-Postman/api_project/api_app
pip install -r requirements.txt
py manage.py runserver

### 2. Ingresando al enlace de documentación generado por Postman
En la página de documentación, se presiona el botón naranja que aparece en la parte superior derecha de la pantalla, el cual dice "Run in Postman."

Al abrir el programa, será posible importar los endpoints del proyecto para realizar pruebas del backend.

* [Enlace a la página de documentación](https://documenter.getpostman.com/view/43047808/2sB3HjM1qH)

## Sobre el desarrollo
Los archivos más importantes del royecto son models.py, serializers.py, urls.py y views.py; los cuales se encuentran en la ruta api_project/api_app, y serán explicados a continuación:
### models.py:
En este archivo se crea el modelo de tablas para la base de datos que almacenarán a las personas y las tareas; para ello se crearon los siguientes campos para cada entidad, las cuales tienen una relación de uno a muchos:
#### Persona (T001Persona):
- id_persona (Llave primaria)
- nombre
- apellido
- documento
- email
#### Tarea (T002Tarea):
- id_tarea (Llave primaria)
- titulo
- descripcion
- fecha_limite
- persona (Llave foranea)

Los cambios realizados en este archivo se ejecutaron para la creación de la base de datos en PostgreSQL con los comandos:
python manage.py makemigrations api_app
python manage.py migrate

### serializers.py
Permite trabsformar el formato en el cual se almacena la información, de modo que no hayan incompatibilidades en ningún apartado de la API.

### urls.py
En este archivo se manejan todas las rutas de los endpoints en los cuales se realizan las diferentes acciones básicas para una base de datos; dichas rutas permiten encontrar automáticamente el archivo y la clase de la cual se debe realizar una instancia, ya sea para registrar a una persona/tarea, buscarla o filtrarla, editarla o borrarla.

### views.py
Este es el archivo que permite ejecutar todas las acciones de la API, ya que es en este archivo donde se declara una clase para cada acción que se realiza, ya sea para personas o para tareas.A estas acciones se les refiere como Vistas.
#### Vistas para Persona
**- PersonaList:** Lista todas las personas y permite crear nuevas.
**- CrearPersona:** Registra una nueva persona en la base de datos.
**- ActualizarPersona:** Actualiza los datos de una persona por id (número de documento) e incluye una validación para evitar duplicados en el campo email.
**- EliminarPersona:** Elimina una persona según su id.
**- PersonaByDocumento:** Busca y devuelve una persona a partir de su número de documento.

#### Vistas para Tarea
Tarea tiene vistas similares para la lectura, creación, modificación y eliminación de datos, que son **TareaList, CrearTarea, ActualizarTarea** y **EliminarTarea**; sin emnargo, para la búsqueda de elementos, se crean clases con diferentes resultados al usar get, que son: 
**- TareaByFecha:** Filtra las tareas por una fecha límite específica para el tipo de dato date (que tiene un formato __YYYY-MM-DD__).
**- TareaByRangoFechas:** Filtra las tareas entre dos fechas dadas, validando el rango.
**- TareaByPersona** Devuelve todas las tareas asignadas a una persona específica.

Cabe mencionar que cada tarea tiene un manejo de errores en caso de no se encuentren registros en las tablas de la base de datos para ambas entidades.


## Creadores
- Cristian Alejandro Rodriguez Rodriguez
- Sharon Ariadna Rincón Guerrero



