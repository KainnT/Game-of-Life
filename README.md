Conway’s Game of Life – Python Implementation

Este proyecto implementa el famoso Juego de la Vida de John Conway utilizando Python, NumPy, Numba y matplotlib, con enfoque en eficiencia computacional, visualización animada y benchmarking empírico.
 Estructura del Proyecto

GameLife/
├── game_of_life.py          # Lógica del juego (clase GameOfLife + función upgrade)
├── animated_visual.py       # Visualización de patrones clásicos (glider, blinker, toad)
├── benchmark.py             # Medición de rendimiento vs tamaño de grilla
├── main.py                  # Menú interactivo para correr visualización o benchmark
├── game_of_life.gif         # Ejemplo de animación generada
├── benchmark_gol.png        # Gráfica de rendimiento generada
├── README.md                # (este archivo)

 Cómo ejecutar

Asegurate de tener los paquetes necesarios:

pip install -r requirements.txt

 Opción 1: Ejecutar todo desde el menú

python main.py

Allí podés:

    Visualizar un patrón clásico animado (glider, blinker, toad)

    Ejecutar el benchmark de rendimiento y guardar la gráfica

📺 Visualización (animated_visual.py)

Podés correrlo directamente para guardar un .gif de un patrón:

python animated_visual.py

Ejemplo de configuración en el script:

rows, cols = 32, 32
initial_state = get_pattern("toad", (rows, cols))

 Benchmark (benchmark.py)

Mide el tiempo promedio por iteración de upgrade() en grillas de distintos tamaños (32x32 hasta 1024x1024) y genera el gráfico benchmark_gol.png con curvas teóricas de comparación.

python benchmark.py

 Sobre la optimización


 Autores

Andrea Arias
Axel Alvarado
Ingeniería en Ciencia de Datos – Lead University
Proyecto académico con enfoque en visualización, simulación y análisis empírico de complejidad.
