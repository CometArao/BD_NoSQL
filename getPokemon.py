import sys
import requests

def getPokemonInfo(pokemonId):
    # URL base de la PokeAPI
    baseURL = "https://pokeapi.co/api/v2/"

    # Endpoint para obtener información de un Pokémon específico
    pokeEndpoint = f"{baseURL}pokemon/{pokemonId}/"
    
    try:
        # Realizar la solicitud HTTP a la API
        response = requests.get(pokeEndpoint)

        if response.status_code == 200:
            # Extraer datos del JSON de respuesta
            pokemonData = response.json()

            # Imprimir información relevante
            print("Nombre:", pokemonData['name'])
            print("Altura:", pokemonData['height'])
            print("Peso:", pokemonData['weight'])
            print("Tipos:")
            for type_info in pokemonData['types']:
                print("-", type_info['type']['name'])
            print("Habilidades:")
            for ability_info in pokemonData['abilities']:
                print("-", ability_info['ability']['name'])
        else:
            # Imprimir mensaje de error si la solicitud no fue exitosa
            print("Error al obtener información de Pokémon:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error al conectarse a la PokeAPI:", e)

if __name__ == "__main__":
    print("Bienvenido al script de información de Pokémon!")
    pokemonId = input("Introduzca la ID del Pokémon que desea consultar: ")

    if len(pokemonId) == 0:
        print("No se ha ingresado una ID de Pokémon.")
        sys.exit(1)
    elif len(pokemonId) != 2:
        print("La ID de Pokémon debe tener 2 dígitos.")
        sys.exit(1)
    else:
        getPokemonInfo(pokemonId)
        print("Gracias por usar el script de información de Pokémon!")