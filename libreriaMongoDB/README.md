# Proyecto | Librerìa MongoDB

Aplicación desarrollada en Python 3 con MongoDB, orientada para ser ejecutada en Linux/Ubuntu. La aplicación posee funcionalidades CRUD en una librerìa.

Posee las siguientes funcionalidades:
- Crear un libro (Nombre, autor)
- Obtener todos los libros registrados
- Obtener un libro por ID
- Actualizar los datos del libro
- Eliminar un libro por ID

## Base de Datos MongoDB

La conexión a la base de datos se hará automáticamente con el programa ejecutable, ya que se asignó un usuario de prueba exclusivo en la BD y la colección mencionada (tryUser).

# Instalación

Para clonar y probar el funcionamiento del trabajo desarrollado, siga los siguientes pasos:
- Cree un nuevo directorio/carpeta
- Inicialice un repositorio en git con el siguiente comando:
```bash
git init
```

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
