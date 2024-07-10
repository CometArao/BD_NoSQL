# Librerias necesarias para la conexión a la base de datos
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import ObjectId # Permite utilizar el tipo de dato ObjectId para la ID
import sys # Permite utilizar sys.exit() para salir del programa

# Conexión a la base de datos
uri = "mongodb+srv://tryUser:K6BbJ3sQ7DQp5CCE@clusternosql.7u9hbqf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterNOSQL"
client = MongoClient(uri)