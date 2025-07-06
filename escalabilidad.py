import numpy as np
from joblib import Parallel, delayed
import time
import matplotlib.pyplot as plt
from game_of_life import upgrade

"""
FUNCION PARA DIVIDIR LA GRILLA EN BLOQUES
"""
def parallel_step(grid, num_blocks):

    rows, cols = grid.shape # SACA EL TAMANNO DE LA GRILLA
    block_tam = rows // num_blocks # TAMANNO DEL BLOQUE PARA CADA PROCESO
    results = Parallel(n_jobs=num_blocks)(
        delayed(upgrade)(grid[i * block_tam:(i + 1) * block_tam, :])  #HACE EL UPGRADE EN PARALELO PARA CADA BLOQUE DE LAS FILAS 
        for i in range(num_blocks)
    )
    return np.vstack(results) # JUNTA DE FORMA VERTICAL CADA BLOQUE ACTUALIZADO EN UNA 


def escal_fuerte():
    """
    Escalamiento fuerte:
    grilla fija 512x512
    variando procesos
    """
    sizes = [1, 2, 4, 8] # NUMERO DE PROCESOS PARA PROBAR
    rows, cols = 512, 512 # TAMADO DE LA GRILLA
    T1 = None # REFERENCIA PARA EL TIEMPO 
    speedups = [] # GUARDAR EL SPEEDUP
    effi = [] # LISTA QUE GUARDA EFICIENCIA
    times = [] # TIEMPOS TOTALES

    for p in sizes:
        grid = np.random.randint(0, 2, size=(rows, cols), dtype=np.int32)
        start = time.time() # MARCA INICIO 
        for _ in range(10): # HACE 10 GEN
            grid = parallel_step(grid, p) # HACE EL UPGRADE EN PARALELO CON EL NUM DE BLOQUES
        end = time.time() # FIN
        total_time = end - start 
        times.append(total_time)

        if p == 1:
            T1 = total_time # GURADA LA REFERENCIA
        speedup = T1 / total_time # CALCULA EL SPEEDUP
        efficiency = speedup / p # CALCULA LA ENFICIENCIA
        speedups.append(speedup) 
        effi.append(efficiency)

        print(f"[strong] {p} procesos: {total_time:.4f}s, speedup={speedup:.2f}, eficiencia={efficiency:.2f}")

    # gráficas
    plt.figure()
    plt.plot(sizes, speedups, marker='o') # EL SPEEDUP VS PROCESSOS
    plt.title("Escalamiento fuerte - Speedup")
    plt.xlabel("Número de procesos")
    plt.ylabel("Speedup")
    plt.grid()
    plt.savefig("strong_speedup.png")

    plt.figure()
    plt.plot(sizes, effi, marker='o') # EFICIENCIA VS PROCESOS
    plt.title("Escalamiento fuerte - Eficiencia")
    plt.xlabel("Número de procesos")
    plt.ylabel("Eficiencia")
    plt.grid()
    plt.savefig("strong_efficiency.png")


def escal_debil():
    """
    Escalamiento débil:
    100x100 por proceso
    """
    sizes = [1, 2, 4, 8] # CANT PROCESOS A PROBAR
    times = [] # TIEMPOS
    effi = [] # EFICIENCIA
    T1 = None # REFERENCIA PARA EL TIEMPO 

    for p in sizes:
        rows, cols = 100 * p, 100 * p # ESCALA LA GRILLA DE FORMA PROPORCIONAL
        grid = np.random.randint(0, 2, size=(rows, cols), dtype=np.int32)  # ESCOJE GRILLA RANDOM
        start = time.time() # INCIA
        for _ in range(10): # NUM DE GENERACIONES
            grid = parallel_step(grid, p) # UPGRADE DE FORMA PARALELA
        end = time.time() # FIN
        total_time = end - start
        times.append(total_time)

        if p == 1:
            T1 = total_time # GUARDA LA REFERENCIA SECUENCIAL
        efficiency = T1 / total_time # CALC DE LA ENFICIENCA
        effi.append(efficiency)

        print(f"[weak] {p} procesos: {total_time:.4f}s, eficiencia={efficiency:.2f}")

    # gráfica
    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.title("Escalamiento débil - Tiempo total") # TIEMPO TOTAL VS PROCESOS
    plt.xlabel("Número de procesos")
    plt.ylabel("Tiempo (s)")
    plt.grid()
    plt.savefig("weak_time.png")

    plt.figure()
    plt.plot(sizes, effi, marker='o')
    plt.title("Escalamiento débil - Eficiencia") # ENFICIENC VS PROCESOS
    plt.xlabel("Número de procesos")
    plt.ylabel("Eficiencia")
    plt.grid()
    plt.savefig("weak_efficiency.png")


if __name__ == "__main__":
    escal_debil()
    escal_fuerte()
