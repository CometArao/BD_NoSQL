import json
from neo4j import GraphDatabase

# Neo4j URI de conexión y credenciales
neo4j_uri = "bolt://localhost:7687"  # Reemplaza con tu URI de conexión
username = "neo4j"  # Reemplaza con tu nombre de usuario
password = "asd123asd"  # Reemplaza con tu contraseña

def get_driver():
    return GraphDatabase.driver(neo4j_uri, auth=(username, password))

def insertar_datos_desde_json():
    driver = get_driver()
    # Cargar los datos JSON desde el archivo
    with open('SetsDatos/limpios/libros_mas_vendidos_limpios.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Insertar los datos en Neo4j
    with driver.session() as session:
        for book in data:
            query = """
            CREATE (b:Book {
                title: $title,
                author: $author,
                original_language: $original_language,
                first_published: $first_published,
                approximate_sales_in_millions: $approximate_sales_in_millions,
                genre: $genre
            })
            """
            session.run(query, {
                'title': book['book'],
                'author': book['author(s)'],
                'original_language': book['original_language'],
                'first_published': book['first_published'],
                'approximate_sales_in_millions': book['approximate_sales_in_millions'],
                'genre': book['genre']
            })
    
    print("Datos insertados en Neo4j desde JSON.")
    driver.close()

# Ejecutar la función para insertar los datos
insertar_datos_desde_json()
