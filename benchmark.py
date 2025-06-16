# ------------------ librarias necesarias --------------
import numpy as np
import time
import matplotlib.pyplot as plt
from numba import njit
from game_of_life import upgrade

# ---- funcion para medir el rendimiento ---
def run_benchmark(): # tama;o de la matriz a partir de las instrucciones de la tarea
    sizes = [32, 64, 128, 256, 512, 1024]
    avg_times = []

    for size in sizes: # genera una matriz random tomando la variable size, con el ajuste  del dtype 
        grid = np.random.randint(0, 2, size=(size, size), dtype=np.int32)
        iterations = 10 # se setea la cantidad de iteraciones para hacer el benchmark
        upgrade(grid)

        start = time.time() # se define la funcion para tomar en cuenta el tiempo a ejecutar el upgrade 10 veces
        for _ in range(iterations):
            grid = upgrade(grid)
        end = time.time()

        avg_time = (end - start) / iterations
        avg_times.append(avg_time)
        print(f"{size}x{size}: {avg_time:.6f} sec/iteración") # calcula el promedio de la medicion y lo muestra en pantalla

    t = avg_times[0]
    num_cells = [s**2 for s in sizes]
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1) #grafico de tiempo promedio de iteracion por tama;o de celdas
    plt.plot(num_cells, avg_times, marker='o', label="Empírico")
    plt.plot(num_cells, [t / num_cells[0] * n for n in num_cells], '--', label="O(n)")
    plt.plot(num_cells, [t / (num_cells[0]*np.log2(num_cells[0])) * n*np.log2(n) for n in num_cells], '--', label="O(n log n)")
    plt.plot(num_cells, [t / (num_cells[0]**2) * (n**2) for n in num_cells], '--', label="O(n²)")
    plt.xlabel("Número de celdas (n)")
    plt.ylabel("Tiempo promedio por iteración (s)")
    plt.title("Tiempo vs tamaño")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2) #grafico de la escala logaritmica
    plt.loglog(num_cells, avg_times, marker='o', label="Empírico")
    plt.loglog(num_cells, [t / num_cells[0] * n for n in num_cells], '--', label="O(n)")
    plt.loglog(num_cells, [t / (num_cells[0]*np.log2(num_cells[0])) * n*np.log2(n) for n in num_cells], '--', label="O(n log n)")
    plt.loglog(num_cells, [t / (num_cells[0]**2) * (n**2) for n in num_cells], '--', label="O(n²)")
    plt.xlabel("log(Número de celdas)")
    plt.ylabel("log(Tiempo)")
    plt.title("Escala log-log")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("benchmark_gol.png")
    print("Gráfico guardado como 'benchmark_gol.png'")

'''plt.tight_layout()
plt.savefig("benchmark_gol.png")
plt.show()'''