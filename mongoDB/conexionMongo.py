import pymongo
import json

# URI de conexión
mongo_uri = "mongodb+srv://show_user:dPFCgteYb2gJPig6@bookstore.zby9nof.mongodb.net/?retryWrites=true&w=majority&appName=Bookstore"

# Conectar a MongoDB
client = pymongo.MongoClient(mongo_uri)

# Seleccionar la base de datos
db = client["Bookstore"]

# Seleccionar la colección (creará la colección si no existe)
collection = db["libros_mas_vendidos"]

# Cargar los datos desde el archivo JSON
with open('SetsDatos/limpios/libros_mas_vendidos_limpios.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Insertar los datos en la colección
if isinstance(data, list):
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Datos insertados correctamente en MongoDB")
