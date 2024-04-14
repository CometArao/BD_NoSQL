import sys
import requests
from transformPokemon import transformPokemonInfo

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

            transformPokemonInfo(pokemonData)
        else:
            # Imprimir mensaje de error si la solicitud no fue exitosa
            print("Error al obtener información de Pokémon:", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print("Error al conectarse a la PokeAPI:", e)
        return None