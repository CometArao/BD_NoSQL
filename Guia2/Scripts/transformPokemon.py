import json

def transformPokemonInfo(pokemonData):
    if pokemonData:
        # Transformar a formato JSON
        pokemon_json = json.dumps(pokemonData, indent=4)

        # Guardar en un archivo
        with open(f"{pokemonData['name']}.json", "w") as json_file:
            json_file.write(pokemon_json)

        print(f"Datos de {pokemonData['name']} transformados y guardados en {pokemonData['name']}.json")
    else:
        print("No se pudo transformar la información debido a errores previos.")
