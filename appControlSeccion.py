# Librerias necesarias para la conexión a la base de datos
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import ObjectId # Permite utilizar el tipo de dato ObjectId para la ID
import sys # Permite utilizar sys.exit() para salir del programa

# Conexión a la base de datos
uri = "mongodb+srv://tryUser:K6BbJ3sQ7DQp5CCE@clusternosql.7u9hbqf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterNOSQL"

# Se crea un cliente para establecer la conexión

client = MongoClient(uri)

try:
    # El método server_info() se ejecuta para verificar que la conexión se realizó correctamente
    client.admin.command('ping')
    print("Usuario comprobado | Conexión exitosa a la base de datos.")
except ConnectionFailure:
    print("No se pudo conectar a la base de datos.")
    sys.exit()

# Seleccionar la base de datos
db = client['Lab1']
# Seleccionar la colección
collection = db['Students']


# Funciones para las opciones del menú

# Función para insertar datos de un estudiante
def createNewStudent():
    nameStudent = input("Ingrese el nombre del estudiante: ")
    

    # Si el nombre no es una cadena de texto, se solicita nuevamente
    while not nameStudent.isalpha():
        print("El nombre del estudiante debe contener solo letras.")
        nameStudent = input("Ingrese el nombre del estudiante: ")

    ageStudent = input("Ingrese la edad del estudiante: ")

    # Si la edad no es mayor a 18 ni menor de 100, se solicita nuevamente
    while not ageStudent.isdigit() or int(ageStudent) <= 18 or int(ageStudent) >= 100:
        print("La edad del estudiante debe tener entre 18 y 100 años.")
        ageStudent = input("Ingrese la edad del estudiante: ")
    
    courseStudent = input("Ingrese el curso del estudiante: ")

    # Si el curso no contiene letras, se solicita nuevamente
    while not courseStudent.isalpha():
        print("El curso del estudiante debe contener solo letras.")
        courseStudent = input("Ingrese el curso del estudiante: ")

    studentData = {
        "Name": nameStudent,
        "Age": ageStudent,
        "Course": courseStudent
    }

    # Se insertan los datos del estudiante en la colección
    result = collection.insert_one(studentData)
    print("Datos del estudiante insertados con éxito. ID del estudiante ingresado:", result.inserted_id)
    print("\n")  # Agrega una línea


# Función para buscar todos los estudiantes
def ReadAllStudents():
    students = collection.find({})
    for student in students:
        print("ID:", student["_id"])
        if "Name" in student:
            print("Nombre:", student["Name"])
        if "Age" in student:
            print("Edad:", student["Age"])
        if "Course" in student:
            print("Curso:", student["Course"])
        print("\n")  # Agrega una línea


# Función para buscar un estudiante por ID
def ReadStudentById():
    student_id = input("Ingrese el ID del estudiante: ")
    print("\n")  # Agrega una línea

    try:
        student = collection.find_one({"_id": ObjectId(student_id)})
        if student:
            print("ID:", student["_id"])
            if "Name" in student:
                print("Nombre:", student["Name"])
            if "Age" in student:
                print("Edad:", student["Age"])
            if "Course" in student:
                print("Curso:", student["Course"])
            print("\n")  # Agrega una línea
        else:
            print("No se encontró ningún estudiante con ese ID.\n")
    except Exception as e:
        print("Error:", e)
        print("\n")  # Agrega una línea



# Función para actualizar los datos de un estudiante
def updateStudent():
    while True:
        studentId = input("Ingrese el ID del estudiante que desea actualizar: ")
        try:
            studentId = ObjectId(studentId)
            newName = input("Ingrese el nuevo nombre del estudiante: ")

            # Validación: Si el nuevo nombre no es una cadena de texto
            if not newName.isalpha():
                print("El nuevo nombre del estudiante debe contener solo letras.")
                continue

            newAge = input("Ingrese la nueva edad del estudiante: ")

            # Validación: Si la nueva edad no es un número válido (mayor a 18 y menor a 100)
            if not newAge.isdigit() or int(newAge) <= 18 or int(newAge) >= 100:
                print("La nueva edad del estudiante debe ser mayor a 18 años.")
                continue

            newCourse = input("Ingrese el nuevo curso del estudiante: ")

            # Validación: Si el nuevo curso no contiene letras
            if not newCourse.isalpha():
                print("El nuevo curso del estudiante debe contener solo letras.")
                continue

            updatedData = {
                "$set": {
                    "Name": newName,
                    "Age": newAge,
                    "Course": newCourse
                }
            }

            result = collection.update_one({"_id": studentId}, updatedData)
            if result.modified_count:
                print("Datos del estudiante actualizados correctamente.")
            else:
                print("No se encontró ningún estudiante con ese ID.")
            break  # Salir del bucle while si todos los datos son válidos
        except Exception as e:
            print("Error:", e)

# Función para eliminar los datos de un estudiante
def deleteStudent():
    studentId = input("Ingrese el ID del estudiante que desea eliminar: ")
    try:
        studentId = ObjectId(studentId)
        result = collection.delete_one({"_id": studentId})
        if result.deleted_count:
            print("Datos del estudiante eliminados correctamente.")
        else:
            print("No se encontró ningún estudiante con ese ID.")
    except Exception as e:
        print("Error:", e)

# Función para salir del programa
def exit_p():
    print("Cerrando el programa...")
    sys.exit()

   # Menú de opciones
def optionMenu():
    options = {
        "1": createNewStudent,
        "2": ReadAllStudents,
        "3": ReadStudentById,
        "4": updateStudent,
        "5": deleteStudent,
        "6": exit_p
    }

    print("\nBienvenido al administrador de secciones de estudiantes")

    while True:
        
        print("\nSelecciona una opción:")
        print("1 -> CREAR datos de estudiantes.")
        print("2 -> MOSTRAR datos de todos los estudiantes.")
        print("3 -> MOSTRAR datos de un estudiante por ID.")
        print("4 -> ACTUALIZAR datos de un estudiante.")
        print("5 -> ELIMINAR datos de un estudiante.")
        print("6 -> Salir de la app.")

        option = input("Ingrese el número de la opción: ")

        optionSelected = options.get(option)
        if optionSelected:
            print()
            optionSelected()
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    optionMenu()