#  Conway’s Game of Life – Python Implementation

Este proyecto implementa el **Juego de la Vida** de John Conway utilizando **Python**, **NumPy**, **Numba**, **Joblib** y **matplotlib**, con enfoque en **eficiencia computacional**, **visualización animada**, **benchmarking empírico** y **diferentes tipos de analisis**.

---

#  Analisis

Tarea 1
    
    El primer Analisis realizado se encuentra en el analisis.md 

Tarea 2 
    
    Y el Perfomance Analisis se encuentra en Performance_analisis.md

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
├── requirements.txt          # Dependencias
├── line_profile_game.py      # Análisis con line_profiler
├── line_profile_game.py.lprof.py      # Resultado de analisis con line_profiler
├── escalabilidad.py          # Analisis de escalabilidad fuerte y debil
├── strong_efficiency.png     # Grafico de analisis de escalabilidad
├── strong_speedup.png        # Grafico de analisis de escalabilidad
├── weak_efficiency.png       # Grafico de analisis de escalabilidad
├── weak_time.png             # Grafico de analisis de escalabilidad
├── profile_analisis.py       # Analisis con CProfile
├── Output.pstats             # Resultado de Analisis con CProfile
└── output.txt                # Resultado de Analisis con CProfile

└── analisis.md               # CONCLUSIONES TAREA 1
└── Peromance_analisis.md     # CONCLUSIONES TAREA 2

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

```bash
python
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

## Analisis line_profiler (`line_profile_game.py`)

## Instalación
Primero, instala line_profiler en tu entorno virtual o instala el requirements.

```bash
pip install line_profiler
```

## Preparar la función a medir
Desactiva el decorador @njit de la función a estudiar (por ejemplo upgrade) comentándolo y Añade el decorador especial @profile (sin importarlo) para que kernprof lo reconozca:

```bash
# @njit
@profile
def upgrade(grid):
```


## Ejecutar line_profiler
Usando kernprof (instalado junto a line_profiler), corre en la terminal:

```bash
kernprof -l -v line_profile_game.py

```
Esto va a generar un archivo con la extensión .lprof y además mostrar el resumen en consola.

Si querés verlo después explícitamente:

```bash
python -m line_profiler line_profile_game.py.lprof

```

## Restaurar 
Cuando termines el análisis:

Comentar @profile
Descomentar @njit

para mantener la versión optimizada.

## Análisis de Escalabilidad (`escalabilidad.py`)

## Instalación
Primero, instala joblib en tu entorno virtual o instala el requirements.

```bash
pip install numpy matplotlib joblib
```

## Ejeccutarlo (escalabilidad.py)

Solo corre:

```bash
python escalabilidad.py
```


El coidgo:

    mide escalamiento fuerte manteniendo una grilla de 512×512 y variando procesos

    mide escalamiento débil manteniendo 100×100 celdas por proceso, escalando proporcionalmente la grilla

    guarda las gráficas en el mismo directorio:

        strong_speedup.png

        strong_efficiency.png

        weak_time.png

        weak_efficiency.png

los resultado en la terminal se muestran como:

    tiempo total

    speedup

    eficiencia


## Análisis de Rendimiento con cProfile (`profile_analisis.py`)


## Instalación
Primero, instala snakeviz en tu entorno virtual o instala el requirements.

```bash
pip install snakeviz
```

## Ejeccutarlo (escalabilidad.py)

Solo corre:

```bash
python profile_analisis.py

```
El coidgo:

    Ejecuta una simulación del Juego de la Vida en una grilla de 512×512 durante 100 pasos

    Utiliza cProfile para capturar estadísticas de rendimiento detalladas

    Genera dos archivos de salida:

    output.pstats: datos en formato binario

    output.txt: resumen en texto legible ordenado por tiempo acumulado

    
## 

##  Autores

- **Andrea Arias**  
- **Axel Alvarado**  
