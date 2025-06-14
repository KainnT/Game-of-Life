import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 
from game_of_life import GameOfLife


def animate_game(game, steps=100, interval=200, save_as=None):
    fig, ax = plt.subplots()
    img = ax.imshow(game.get_state(), cmap='binary')
    ax.set_title("Game of Life")
    ax.axis('off')

    def update(frame):
        game.step()
        img.set_data(game.get_state())
        return [img]

    ani = animation.FuncAnimation(
        fig, update, frames=steps, interval=interval, blit=True)

    if save_as:
        ani.save(save_as, writer='ffmpeg')
        print(f"Animación guardada como {save_as}")
    else:
        plt.show()



def get_pattern(pattern_name, grid_size):
    grid = np.zeros(grid_size, dtype=np.int32)
    mid_r, mid_c = grid_size[0] // 2, grid_size[1] // 2

    if pattern_name == "glider":
        pattern = [(0,1), (1,2), (2,0), (2,1), (2,2)]
    elif pattern_name == "blinker":
        pattern = [(0,1), (1,1), (2,1)]
    elif pattern_name == "toad":
        pattern = [(1,1), (1,2), (1,3), (2,0), (2,1), (2,2)]
    else:
        raise ValueError("Unsupported pattern")

    for dr, dc in pattern:
        grid[mid_r + dr, mid_c + dc] = 1

    return grid

'''
rows, cols = 32, 32
initial_state = get_pattern("toad", (rows, cols))
game = GameOfLife(rows, cols, initial_state=initial_state)
animate_game(game, steps=100, interval=150, save_as="game_of_life.gif")
'''