import pymongo

# URI de conexión
mongo_uri = "mongodb+srv://show_user:dPFCgteYb2gJPig6@bookstore.zby9nof.mongodb.net/?retryWrites=true&w=majority&appName=Bookstore"

# Conectar a MongoDB
client = pymongo.MongoClient(mongo_uri)

# Seleccionar la base de datos y la colección
db = client["Bookstore"]
collection = db["libros_mas_vendidos"]

def consulta_libros_mas_vendidos():
    pipeline = [
        {
            "$group": {
                "_id": "$genre",
                "max_sales": { "$max": "$approximate_sales_in_millions" },
                "books": {
                    "$push": {
                        "book": "$book",
                        "author(s)": "$author(s)",
                        "sales": "$approximate_sales_in_millions"
                    }
                }
            }
        },
        {
            "$unwind": "$books"
        },
        {
            "$match": {
                "$expr": {
                    "$eq": ["$max_sales", "$books.sales"]
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "genre": "$_id",
                "book": "$books.book",
                "author(s)": "$books.author(s)",
                "sales": "$books.sales"
            }
        },
        {
            "$sort": { "genre": 1 }
        }
    ]

    result = collection.aggregate(pipeline)

    # Mostrar los resultados de forma legible
    for doc in result:
        print(f"Género: {doc['genre']}\n  Libro: {doc['book']}\n  Autor(es): {doc['author(s)']}\n  Ventas: {doc['sales']} millones\n")

def consulta_autores_mas_vendidos():
    pipeline = [
        {
            "$group": {
                "_id": {
                    "genre": "$genre",
                    "author": "$author(s)"
                },
                "total_sales": { "$sum": "$approximate_sales_in_millions" }
            }
        },
        {
            "$sort": { "_id.genre": 1, "total_sales": -1 }
        },
        {
            "$group": {
                "_id": "$_id.genre",
                "author": { "$first": "$_id.author" },
                "total_sales": { "$first": "$total_sales" }
            }
        },
        {
            "$sort": { "_id": 1 }
        },
        {
            "$project": {
                "_id": 0,
                "genre": "$_id",
                "author": "$author",
                "total_sales": "$total_sales"
            }
        }
    ]

    result = collection.aggregate(pipeline)

    # Mostrar los resultados de forma legible
    for doc in result:
        print(f"Género: {doc['genre']}\n  Autor(es): {doc['author']}\n  Ventas Totales: {doc['total_sales']} millones\n")

def consulta_idioma_mas_comun():
    pipeline = [
        {
            "$group": {
                "_id": "$original_language",
                "count": { "$sum": 1 }
            }
        },
        {
            "$sort": { "count": -1 }
        },
        {
            "$project": {
                "_id": 0,
                "idioma": "$_id",
                "count": "$count"
            }
        }
    ]

    result = list(collection.aggregate(pipeline))

    # Mostrar los resultados de forma legible
    print("Idiomas originales y sus contadores:")
    for doc in result:
        print(f"Idioma: {doc['idioma']}\n  Cantidad de Libros: {doc['count']}\n")

    # Obtener el idioma más común
    idioma_mas_comun = result[0]

    # Mostrar el idioma original más común
    print(f"Idioma Original Más Común: {idioma_mas_comun['idioma']}\n  Cantidad de Libros: {idioma_mas_comun['count']}")

def consulta_popularidad_generos():
    pipeline = [
        {
            "$group": {
                "_id": {
                    "genre": "$genre",
                    "year": "$first_published"
                },
                "total_sales": { "$sum": "$approximate_sales_in_millions" }
            }
        },
        {
            "$sort": { "_id.year": 1, "_id.genre": 1 }
        },
        {
            "$project": {
                "_id": 0,
                "genre": "$_id.genre",
                "year": "$_id.year",
                "total_sales": "$total_sales"
            }
        }
    ]

    result = collection.aggregate(pipeline)

    # Mostrar los resultados de forma legible
    print("Popularidad de los géneros a lo largo del tiempo basada en ventas:")
    for doc in result:
        print(f"Año: {doc['year']}, Género: {doc['genre']}, Ventas Totales: {doc['total_sales']} millones")

# Menú de opciones
menu = {
    "1": ("Consultar libros más vendidos en las categorías estudiadas", consulta_libros_mas_vendidos),
    "2": ("Consultar autores con más libros vendidos en cada género", consulta_autores_mas_vendidos),
    "3": ("Consultar idioma original más común entre los libros más vendidos", consulta_idioma_mas_comun),
    "4": ("Consultar cómo ha cambiado la popularidad de los géneros a lo largo del tiempo", consulta_popularidad_generos),
    "5": ("Salir", None)
}

def mostrar_menu():
    print("\nMenú de Consultas:")
    for key in menu:
        print(f"{key}. {menu[key][0]}")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "5":
        print("Saliendo del programa.")
        break
    elif opcion in menu:
        print(f"\n{menu[opcion][0]}")
        menu[opcion][1]()
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")

# Cerrar la conexión
client.close()
