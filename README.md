#  Conway’s Game of Life – Python Implementation

Este proyecto implementa el **Juego de la Vida** de John Conway utilizando **Python**, **NumPy**, **Numba** y **matplotlib**, con enfoque en **eficiencia computacional**, **visualización animada** y **benchmarking empírico**.

---

##  Estructura del Proyecto

```
GameLife/
├── game_of_life.py           # Lógica del juego (GameOfLife + upgrade)
├── animated_visual.py        # Visualización de patrones clásicos
├── benchmark.py              # Benchmark de rendimiento
├── profile_analysis.py       # script para análisis con cProfile
├── main.py                   # Menú interactivo para correr el juego
├── game_of_life.gif          # Ejemplo animado
├── benchmark_gol.png         # Gráfico de benchmark
├── README.md                 # Descripción del proyecto
└── requirements.txt          # Dependencias

```

---

##  Cómo ejecutar

Tener los paquetes necesarios:

```bash
pip install -r requirements.txt
```

---

###  Opción 1: Ejecutar todo desde el menú

```bash
python main.py
```

Desde el menú se puede:

- Visualizar un patrón clásico animado (`glider`, `blinker`, `toad`)
- Ejecutar el benchmark de rendimiento y guardar la gráfica

---

##  Visualización (`animated_visual.py`)

Se puede correr directamente para guardar un `.gif` de un patrón:

```bash
python animated_visual.py
```

Ejemplo de configuración en el script:

```python
rows, cols = 32, 32
initial_state = get_pattern("toad", (rows, cols))
```

---

##  Benchmark (`benchmark.py`)

Mide el tiempo promedio por iteración de `upgrade()` en grillas de distintos tamaños (`32x32` hasta `1024x1024`) y genera el gráfico `benchmark_gol.png` con curvas teóricas de comparación.

```bash
python benchmark.py
```

---

##  Optimización

La función `upgrade()` está optimizada con `@njit` de **Numba**, lo que permite ejecutar simulaciones a gran escala con excelente rendimiento. El uso de arrays de 32 bits y lógica toroidal mejora el consumo de memoria y la precisión de simulación.

---


##  Analisis

El Analisis realizado se encuentra en el analisis.txt

---


##  Autores

- **Andrea Arias**  
- **Axel Alvarado**  
