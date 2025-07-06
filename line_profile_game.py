from game_of_life import GameOfLife  # importa la clase con la lógica del Juego de la Vida

def profile_run():
    # inicializa el juego con un tablero de 128x128 celdas aleatorias
    game = GameOfLife(rows=128, cols=128)
    
    # ejecuta 5 generaciones para medir el rendimiento (puedes ajustar el número)
    game.run(5)  # pocas iteraciones, pero suficientes para ver el profiling

if __name__ == "__main__":
    profile_run()  # ejecuta la función de prueba si se corre este script directamente
