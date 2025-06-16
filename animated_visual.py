#-----------------------librerias necesarias ---------------------
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 
from game_of_life import GameOfLife

#-----------------funcion animate_game------------
def animate_game(game, steps=100, interval=200, save_as=None):
    fig, ax = plt.subplots()# se crean figuras y ejes para el grafico
    img = ax.imshow(game.get_state(), cmap='binary') #muestra el estado actual del juego
    ax.set_title("Game of Life") #establece el titulo
    ax.axis('off') #alinea los ejes y los oculta para que le visualizacion sea mas limpia

    def update(frame): # el juego se actualiza con el nuevo paso y el nuevo estado
        game.step()
        img.set_data(game.get_state())
        return [img]

    ani = animation.FuncAnimation(
        fig, update, frames=steps, interval=interval, blit=True) # creacion de la animacion usando varialbes update por cada cuadro y paso

    if save_as: #itera sobre la definicion de que si el juego esta definido, se guarda la animacion como gif, si no lo muestra en la pantalla
        ani.save(save_as, writer='ffmpeg')
        print(f"Animación guardada como {save_as}")
    else:
        plt.show()



def get_pattern(pattern_name, grid_size): #devuelve un arreglo con el atron inicial especifico
    grid = np.zeros(grid_size, dtype=np.int32) #crea la matriz que toma como medida el input
    mid_r, mid_c = grid_size[0] // 2, grid_size[1] // 2

    if pattern_name == "glider": #define las cordenadas del patron
        pattern = [(0,1), (1,2), (2,0), (2,1), (2,2)]
    elif pattern_name == "blinker":
        pattern = [(0,1), (1,1), (2,1)]
    elif pattern_name == "toad":
        pattern = [(1,1), (1,2), (1,3), (2,0), (2,1), (2,2)]
    else:
        raise ValueError("Unsupported pattern")

    for dr, dc in pattern: #coloca la celula viva dentro del lugar especifico del tablero
        grid[mid_r + dr, mid_c + dc] = 1

    return grid

'''
rows, cols = 32, 32
initial_state = get_pattern("toad", (rows, cols))
game = GameOfLife(rows, cols, initial_state=initial_state)
animate_game(game, steps=100, interval=150, save_as="game_of_life.gif")
'''