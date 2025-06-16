#----- librerias -----
import os
from game_of_life import GameOfLife
from animated_visual import animate_game, get_pattern
import benchmark


def clear_terminal(): #limpia la consola para evitar saturacion y pulir la interfaz
    os.system("cls" if os.name == "nt" else "clear")

def visual_menu(): # crear el patron de la visualizacion para el usuario
    clear_terminal()
    print("Visualización de Game of Life\n")
    print("Patrones disponibles: glider, blinker, toad")
    pattern = input("Escriba el patrón a mostrar: ").lower().strip()
    size = int(input("Tamaño de la grilla (ej. 32, 64, 128): ").strip())
    steps = int(input("Cantidad de pasos (frames): ").strip())

    try: #general el patron seleccionado
        initial_state = get_pattern(pattern, (size, size))
        game = GameOfLife(size, size, initial_state=initial_state)
        animate_game(game, steps=steps, interval=150, save_as=f"game_of_life_{pattern}.gif")
    except ValueError as e:
        print(f"Error: {e}")
        input("Presione Enter para continuar...")

def benchmark_menu():
    clear_terminal()
    print("Medición de Rendimiento de Game of Life\n")
    benchmark.run_benchmark()
    input("Presione Enter para continuar...")

def main(): #general un buckle que hace iteraciones de manera indefinida que le da al usuario 3 opciones 
    while True:
        clear_terminal()
        print("Juego de la Vida - Menú Principal")
        print("1. Visualizar animación")
        print("2. Ejecutar benchmark")
        print("3. Salir")

        choice = input("\nSeleccione una opción: ").strip() #lee las opciones y respecto a la elegida crea la visualizacion, el benchmark o termina el programa
        if choice == "1":
            visual_menu()
        elif choice == "2":
            benchmark_menu()
        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
