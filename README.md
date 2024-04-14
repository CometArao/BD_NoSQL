# Guía 2 | Extracción y transformación a JSON con PokeAPI

Aplicación desarrollada en Python 3 con MongoDB, orientada para ser ejecutada en Linux/Ubuntu. La aplicación posee funcionalidades CRUD para un sistema de secciones de estudiantes.

Posee las siguientes funcionalidades:
- Recibe la ID del pokemón a estudiar
- Transforma los datos de ese mismo pokemón en formato JSON
- Los modela

# Instalación

Para clonar y probar el funcionamiento del trabajo desarrollado, siga los siguientes pasos:
- Cree un nuevo directorio/carpeta
- Inicialice un repositorio en git con el siguiente comando:
```bash
git init
```
- Luego, copie el comando de la guía correspondiente para clonar el repositorio.

```bash
git clone --branch Guia2 https://github.com/CometArao/BD_NoSQL
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
python3 main.py
```

Programado por [@CometArao](https://github.com/CometArao)
