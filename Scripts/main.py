import sys
from getPokemon import getPokemonInfo

def optionMenu():
    print("\nBienvenido al script de información de Pokémon!")

    while True:
        print("\nMenú de opciones:")
        print("1 -> Consultar información de un Pokémon por ID")
        print("2 -> Salir del programa")

        option = input("Ingrese el número de la opción que desea seleccionar: ")

        if option == '1':
            pokemonId = input("Introduzca la ID del Pokémon que desea consultar: ")
            getPokemonInfo(pokemonId)
        elif option == '2':
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    optionMenu()
