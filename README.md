# Guía 1 | CRUD en Python con MongoDB

Aplicación desarrollada en Python 3 con MongoDB, orientada para ser ejecutada en Linux/Ubuntu. La aplicación posee funcionalidades CRUD para un sistema de secciones de estudiantes.

Posee las siguientes funcionalidades:
- Crear un estudiante (Nombre, Edad, Curso)
- Obtener todos los estudiantes registrados
- Obtener un estudiante por ID
- Actualizar los datos del estudiante (Nombre, Edad, Curso)
- Eliminar un estudiante por ID

## Base de Datos MongoDB

La conexión a la base de datos se hará automáticamente con el programa ejecutable, ya que se asignó un usuario de prueba exclusivo en la BD y la colección mencionada (tryUser).

Cada estudiante cuenta con una ID automática, además de un nombre, una edad y un curso. Además, posee pequeñas verificaciones, como que el nombre y el curso debe poseer al menos una letra junto la edad sea entre 18 a 100 años.

# Instalación

Recuerda inicialmente clonar el repositorio con Git clone.

## Dependencias

Para ejecutar correctamente la aplicación, debe contar con Python 3.

```bash
sudo apt install python3
```
Además, instale Python3-pip para instalar drivers basados en Python de forma más óptima.

```bash
sudo apt install python3-pip
```

## Drivers

Para que la aplicacion se conecte de forma correcta con la base de datos en MongoDB, ademas de poder usar la ID para las funciones CRUD, es necesario instalar _pymongo_. Asi se podran utilizar las librerias de Mongo y bson.

```bash
pip install pymongo
```

## Ejecucion
Con los pasos anteriormente completados y ubicándose en la carpeta clonada, ejecute el siguiente comando en su terminal para iniciar la aplicación.

```bash
python3 appControlSeccion.py
```

Programado por [@CometArao](https://github.com/CometArao)
