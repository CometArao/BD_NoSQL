from neo4j import GraphDatabase

# Neo4j URI de conexión y credenciales
neo4j_uri = "bolt://localhost:7687"  # Reemplaza con tu URI de conexión
username = "neo4j"  # Reemplaza con tu nombre de usuario
password = "asd123asd"  # Reemplaza con tu contraseña

def get_driver():
    return GraphDatabase.driver(neo4j_uri, auth=(username, password))

# Función para consultar los libros más vendidos en cada categoría
def consulta_libros_mas_vendidos():
    driver = get_driver()
    query = """
    MATCH (b:Book)
    WITH b.genre AS genre, MAX(b.approximate_sales_in_millions) AS max_sales
    MATCH (b:Book {genre: genre, approximate_sales_in_millions: max_sales})
    RETURN b.genre AS genero, b.title AS libro, b.author AS autor, b.approximate_sales_in_millions AS ventas
    ORDER BY genero
    """
    with driver.session() as session:
        result = session.run(query)
        # Mostrar los resultados de forma legible
        for record in result:
            print(f"Género: {record['genero']}\n  Libro: {record['libro']}\n  Autor(es): {record['autor']}\n  Ventas: {record['ventas']} millones\n")
    driver.close()

# Función para consultar los autores con más libros vendidos en cada género
def consulta_autores_mas_vendidos():
    driver = get_driver()
    query = """
    MATCH (b:Book)
    WITH b.genre AS genre, b.author AS author, SUM(b.approximate_sales_in_millions) AS total_sales
    ORDER BY genre, total_sales DESC
    WITH genre, COLLECT({author: author, sales: total_sales}) AS authors
    RETURN genre, authors[0].author AS autor, authors[0].sales AS ventas_totales
    ORDER BY genre
    """
    with driver.session() as session:
        result = session.run(query)
        # Mostrar los resultados de forma legible
        for record in result:
            print(f"Género: {record['genre']}\n  Autor(es): {record['autor']}\n  Ventas Totales: {record['ventas_totales']} millones\n")
    driver.close()

# Función para consultar el idioma original más común entre los libros más vendidos
def consulta_idioma_mas_comun():
    driver = get_driver()
    query = """
    MATCH (b:Book)
    WITH b.original_language AS idioma, COUNT(*) AS count
    RETURN idioma, count
    ORDER BY count DESC
    """
    with driver.session() as session:
        result = session.run(query)
        # Mostrar los resultados de forma legible
        print("Idiomas originales y sus contadores:")
        idiomas = []
        for record in result:
            idiomas.append(record)
            print(f"Idioma: {record['idioma']}\n  Cantidad de Libros: {record['count']}\n")

        if idiomas:
            # Obtener el idioma más común
            idioma_mas_comun = idiomas[0]
            print(f"Idioma Original Más Común: {idioma_mas_comun['idioma']}\n  Cantidad de Libros: {idioma_mas_comun['count']}")
        else:
            print("No se encontraron idiomas.")
    driver.close()

# Función para consultar cómo ha cambiado la popularidad de los géneros a lo largo del tiempo basada en ventas
def consulta_popularidad_generos():
    driver = get_driver()
    query = """
    MATCH (b:Book)
    WITH b.genre AS genre, b.first_published AS year, SUM(b.approximate_sales_in_millions) AS total_sales
    RETURN genre, year, total_sales
    ORDER BY year, genre
    """
    with driver.session() as session:
        result = session.run(query)
        # Mostrar los resultados de forma legible
        print("Popularidad de los géneros a lo largo del tiempo basada en ventas:")
        for record in result:
            print(f"Año: {record['year']}, Género: {record['genre']}, Ventas Totales: {record['total_sales']} millones")
    driver.close()

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
