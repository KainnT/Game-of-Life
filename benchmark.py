import numpy as np
import time
import matplotlib.pyplot as plt
from numba import njit
from game_of_life import upgrade

def run_benchmark():
    sizes = [32, 64, 128, 256, 512, 1024]
    avg_times = []

    for size in sizes:
        grid = np.random.randint(0, 2, size=(size, size), dtype=np.int32)
        iterations = 10
        upgrade(grid)

        start = time.time()
        for _ in range(iterations):
            grid = upgrade(grid)
        end = time.time()

        avg_time = (end - start) / iterations
        avg_times.append(avg_time)
        print(f"{size}x{size}: {avg_time:.6f} sec/iteración")

    t = avg_times[0]
    num_cells = [s**2 for s in sizes]
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(num_cells, avg_times, marker='o', label="Empírico")
    plt.plot(num_cells, [t / num_cells[0] * n for n in num_cells], '--', label="O(n)")
    plt.plot(num_cells, [t / (num_cells[0]*np.log2(num_cells[0])) * n*np.log2(n) for n in num_cells], '--', label="O(n log n)")
    plt.plot(num_cells, [t / (num_cells[0]**2) * (n**2) for n in num_cells], '--', label="O(n²)")
    plt.xlabel("Número de celdas (n)")
    plt.ylabel("Tiempo promedio por iteración (s)")
    plt.title("Tiempo vs tamaño")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
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