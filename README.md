# Guía 2 | Extracción y transformación a JSON con PokeAPI

Aplicación desarrollada en Python 3 usando la PokeAPI, orientada para ser ejecutada en Linux/Ubuntu.
Posee las siguientes funcionalidades:
- Recibe la ID del pokemón de interés y obtiene su información desde la PokeAPI.
- Transforma los datos de ese mismo pokemón en formato JSON 
- Compara la información entre dos Pokemón en una página HTML usando D3.js
- La comparativa se basa en las estadísticas base de dos Pokemón, en este caso Growlithe y Porygon.

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

Para que la aplicacion se conecte de forma correcta, debe instalar la librería de requests para que obtenga las consultas desde la página directamente.

```bash
pip install requests
```
La justificación de esta librería es porque se desarrolló en Python 3.10.12, por lo que la Pokepy no funcionaría correctamente, y se eligió desarrollarla sin la Pokebase.

## Ejecucion
Con los pasos anteriormente completados y ubicándose en la carpeta clonada, ejecute el siguiente comando en su terminal para iniciar la aplicación.

```bash
python3 main.py
```

Y podrá elegir la información a descargar del Pokemón en cuestión.

Finalmente, levante un servidor local

```bash
python3 -m http.server
```

Y abra el archivo charts.html para visualizar la comparativa.

Programado por [@CometArao](https://github.com/CometArao)
