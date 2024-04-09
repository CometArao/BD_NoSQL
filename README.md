# Lab1 | CRUD en Python con MongoDB

Aplicacion desarrollada en Python 3 con MongoDB, orientada para ser ejecutada en Linux/Ubuntu. La aplicacion posee funcionalidades CRUD para un sistema de secciones de estudiantes.

Posee las siguientes funcionalidades:
- Crear un estudiante (Nombre, Edad, Curso)
- Obtener todos los estudiantes registrados
- Obtener un estudiante por ID
- Actualizar los datos del estudiante (Nombre, Edad, Curso)
- Eliminar un estudiante por ID

## Dependencias

```bash
sudo apt install python3
```

```bash
sudo apt install python3-pip
```

## Drivers

Para que la aplicacion se conecte de forma correcta con la base de datos en MongoDB, ademas de poder usar la ID para las funciones CRUD, es necesario instalar _pymongo_. Asi se podran utilizar las librerias de Mongo y bson.

```bash
pip install pymongo
```


## Ejecucion
Para ejecutar la aplicacion, ejecute el siguiente comando en su terminal.

```bash
python3 appControlSeccion.py
```

Programado por [@CometArao](https://github.com/CometArao)
