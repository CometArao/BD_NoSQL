import pprint
from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure
import sys # Para usar sys.exit()

# Conexión a la base de datos
uri = "mongodb+srv://tryUser:K6BbJ3sQ7DQp5CCE@clusternosql.7u9hbqf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterNOSQL"

# Se crea un cliente para establecer la conexión

client = MongoClient(uri)

try:
    # El método server_info() se ejecuta para verificar que la conexión se realizó correctamente
    client.admin.command('ping')
    print("Conexión exitosa")
except ConnectionFailure:
    print("No se pudo conectar a la base de datos:")
    sys.exit()

# Seleccionar la base de datos
db = client['Lab1']

# Seleccionar la colección
collection = db['Students']

def exit_p():
    print("Cerrando el programa...")
    sys.exit()

# Listar todos los datos 
def findStudents():
    students = collection.find({})
    for student in students:
        pprint.pprint(student)


   # Menú de opciones
def menu():
    options = {
        "1": findStudents,
        "6": exit_p
    }

    while True:
        print("\nSelecciona una opción:")
        print("1. Crear datos de mascota")
        print("2. Buscar mascotas")
        print("3. Buscar una mascota")
        print("4. Actualizar datos de mascota")
        print("5  Eliminar datos de mascota")
        print("6. Salir")


        opcion = input("Ingrese el número de la opción: ")

        selected_option = options.get(opcion)
        if selected_option:
            selected_option()
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
 menu()