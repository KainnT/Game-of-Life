import numpy as np
import time
import matplotlib.pyplot as plt
from numba import njit, prange


'''Este codigo tiene la misma logica programatica que el game_of_life.py, solamente que este esta hecho para probar diferentes combinaciones de njit, 
y encontrar dentro de un benchmark la mas eficiente'''


# ==== VERSIÓN 1: SIN NUMBA ====
def upgrade_plain(grid):
    rows, cols = grid.shape
    grid_updated = np.zeros((rows, cols), dtype=np.int32)
    for r in range(rows):
        for c in range(cols):
            alive = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = (r + dr) % rows, (c + dc) % cols
                    alive += grid[nr, nc]
            if grid[r, c] == 1 and alive in [2, 3]:
                grid_updated[r, c] = 1
            elif grid[r, c] == 0 and alive == 3:
                grid_updated[r, c] = 1
    return grid_updated

# ==== VERSIÓN 2: NUMBA SECUENCIAL ====
@njit
def upgrade_numba(grid):
    rows, cols = grid.shape
    grid_updated = np.zeros((rows, cols), dtype=np.int32)
    for r in range(rows):
        for c in range(cols):
            alive = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = (r + dr) % rows, (c + dc) % cols
                    alive += grid[nr, nc]
            if grid[r, c] == 1 and alive in [2, 3]:
                grid_updated[r, c] = 1
            elif grid[r, c] == 0 and alive == 3:
                grid_updated[r, c] = 1
    return grid_updated

# ==== VERSIÓN 3: NUMBA PARALELO ====
@njit(parallel=True)
def upgrade_parallel(grid):
    rows, cols = grid.shape
    grid_updated = np.zeros((rows, cols), dtype=np.int32)
    for r in prange(rows):
        for c in range(cols):
            alive = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = (r + dr) % rows, (c + dc) % cols
                    alive += grid[nr, nc]
            if grid[r, c] == 1 and alive in [2, 3]:
                grid_updated[r, c] = 1
            elif grid[r, c] == 0 and alive == 3:
                grid_updated[r, c] = 1
    return grid_updated

# ==== VERSIÓN 4: NUMBA PARALELO + FASTMATH ====
@njit(parallel=True, fastmath=True)
def upgrade_parallel(grid):
    rows, cols = grid.shape
    grid_updated = np.zeros((rows, cols), dtype=np.int32)
    for r in prange(rows):
        for c in range(cols):
            alive = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = (r + dr) % rows, (c + dc) % cols
                    alive += grid[nr, nc]
            if grid[r, c] == 1 and alive in [2, 3]:
                grid_updated[r, c] = 1
            elif grid[r, c] == 0 and alive == 3:
                grid_updated[r, c] = 1
    return grid_updated

# ==== VERSIÓN 5: NUMBA FASTMATH ====
@njit(fastmath=True)
def upgrade_fastmath(grid):
    rows, cols = grid.shape
    grid_updated = np.zeros((rows, cols), dtype=np.int32)
    for r in range(rows):
        for c in range(cols):
            alive = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = (r + dr) % rows, (c + dc) % cols
                    alive += grid[nr, nc]
            if grid[r, c] == 1 and alive in [2, 3]:
                grid_updated[r, c] = 1
            elif grid[r, c] == 0 and alive == 3:
                grid_updated[r, c] = 1
    return grid_updated

# ==== VERSIÓN 6: NUMBA CACHE ====
@njit(cache=True)
def upgrade_cache(grid):
    rows, cols = grid.shape
    grid_updated = np.zeros((rows, cols), dtype=np.int32)
    for r in range(rows):
        for c in range(cols):
            alive = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = (r + dr) % rows, (c + dc) % cols
                    alive += grid[nr, nc]
            if grid[r, c] == 1 and alive in [2, 3]:
                grid_updated[r, c] = 1
            elif grid[r, c] == 0 and alive == 3:
                grid_updated[r, c] = 1
    return grid_updated

# ==== VERSIÓN 7: NUMBA PARALELO + FASTMATH + CACHE ====
@njit(parallel=True, fastmath=True, cache=True)
def upgrade_all(grid):
    rows, cols = grid.shape
    grid_updated = np.zeros((rows, cols), dtype=np.int32)
    for r in prange(rows):
        for c in range(cols):
            alive = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = (r + dr) % rows, (c + dc) % cols
                    alive += grid[nr, nc]
            if grid[r, c] == 1 and alive in [2, 3]:
                grid_updated[r, c] = 1
            elif grid[r, c] == 0 and alive == 3:
                grid_updated[r, c] = 1
    return grid_updated

# ==== BENCHMARK ====
def run_benchmark(label, func, grid, steps=50):
    current = grid.copy()
    start = time.time()
    for _ in range(steps):
        current = func(current)
    elapsed = time.time() - start
    print(f"{label:<25}: {elapsed:.4f} segundos")
    return elapsed

# ==== EJECUCIÓN ====
if __name__ == "__main__":
    rows, cols = 300, 300
    steps = 50
    initial = np.random.randint(0, 2, size=(rows, cols), dtype=np.int32)

    # Pre-compilación de las funciones Numba
    upgrade_numba(initial)
    upgrade_parallel(initial)

    print("== Benchmark Game of Life ==")
    times = []
    labels = []

    t1 = run_benchmark("Sin Numba", upgrade_plain, initial, steps)
    times.append(t1)
    labels.append("Sin Numba")

    t2 = run_benchmark("Con Numba (Sec)", upgrade_numba, initial, steps)
    times.append(t2)
    labels.append("Numba Sec")

    t3 = run_benchmark("Numba Paralelo", upgrade_parallel, initial, steps)
    times.append(t3)
    labels.append("Numba Paralelo")

    t4 = run_benchmark("Numba Paralelo + Fastmath", upgrade_parallel, initial, steps)
    times.append(t4)
    labels.append("Numba Paralelo Fastman")
    
    t5 = run_benchmark("Numba Fastmath", upgrade_fastmath, initial, steps)
    times.append(t5)
    labels.append("Numba Fastmath")

    t6 = run_benchmark("Numba Cache", upgrade_cache, initial, steps)
    times.append(t6)
    labels.append("Numba Cache")

    t7 = run_benchmark("Numba Full Combo", upgrade_all, initial, steps)
    times.append(t7)
    labels.append("Numba Parallel + Fast + Cache")



    # ==== GRÁFICA ====
    plt.figure(figsize=(15, 10))
    bars = plt.bar(labels, times, color=["gray", "orange", "green", "red", "blue", "purple", "teal"])
    for bar, t in zip(bars, times):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.05, f"{t:.2f}s", ha='center', va='bottom')

    plt.title("Comparación de rendimiento - Game of Life")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("benchmark_gol.png")
    print("Gráfica guardada como benchmark_gol.png")
