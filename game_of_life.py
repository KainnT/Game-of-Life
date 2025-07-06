import numpy as np
from numba import njit
import matplotlib.pyplot as plt
import matplotlib.animation as animation


@njit #utilizacion de numba para agilizar procesos
# @profile  # habilitar profiling con kernprof (quitar @njit antes de usar)
def upgrade(grid): # definicion de funcion de upgrade que recide una matriz (1 = viva, 0 = muerta)
    rows, cols = grid.shape # forma el numero de filas y columnas dependiendo del tama;o de la matriz
    grid_updated = np.zeros((rows, cols), dtype = np.int32) # crea una matriz nueva de inicio uncamente con 0's
    for r in range (rows): # recorrido de cada fila
        for c in range(cols):# recorrido de cada columna
            alive= 0 # acumula el numero de vecinos por cada celda
            for dr in [-1,0,1]:
                for dc in [-1,0,1]: #recorrido de la matriz
                    if dr == 0 and dc == 0: # como en la matriz el centro esta en 0, se pide que si en su centro hay un 0, continue
                        continue
                    nr,nc = (r + dr) % rows, (c+dc) % cols #coordenadas del vecino nr = neighbour row, nc = neighbour column
                    alive += grid[nr, nc] # se suma el vecino al contador total
            if grid[r,c] == 1 and alive in [2,3]:
                grid_updated[r,c] = 1 # regla de supervivencia sobre la celda viva == 1
            elif grid[r,c] == 0 and alive == 3: # regla de reproduccion 
                grid_updated[r,c] = 1
    return grid_updated
                
#--------------- implementacion de clase game of lige -----------------------------
class GameOfLife:
    def __init__(self, rows, cols, initial_state=None): #metdo sugerido por el profesor 
        self.rows = rows # se aplica el metodo guardar filas y columnas 
        self.cols = cols
        if initial_state is not None: # se proporciona el inicial state que aplica si el juego es con un estado aleatorio o no
            self.grid = np.array(initial_state, dtype=np.int32) #data type seran entretos de 32 bits de 4 bytes por celda para compatibilidad con numba y menos  consumo de memoria
        else:
            self.grid = np.random.randint(0, 2, size=(rows, cols), dtype=np.int32) #si no se le da el initial state asumira uno aleatorio

    def get_state(self):
        return self.grid.copy() #genera una copia del estado actual

    def step(self):
        self.grid = upgrade(self.grid) # implementacio de las reglas del juego seteadas en la funcion upgrade

    def run(self, steps): #ejecuta el juego por cantidad de pasos 
        for _ in range(steps): # se utiliza _ ya que se acuerda que no existe necesidad de crear una funcion para ver por cual paso va el juego
            self.step()
        

if __name__ == "__main__":
    game = GameOfLife(rows=50, cols=50)
    game.run(10)
    estado_final = game.get_state()