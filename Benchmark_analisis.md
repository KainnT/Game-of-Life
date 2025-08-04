| Variante                          | Tiempo (s) |
| --------------------------------- | ---------- |
| **Sin Numba**                     | 7.2594     |
| **Numba Secuencial (`@njit`)**    | 0.1149     |
| **Numba Paralelo**                | 0.1144     |
| **Paralelo + Fastmath**           | 0.0307     |
| **Solo Fastmath**                 | 0.2790     |
| **Solo Cache**                    | 0.2491     |
| **Full Combo (Par + FM + Cache)** | 1.0944     |



1. @njit vs sin Numba

    Pasar de sin Numba a @njit mejora el rendimiento más de 60x.

    Esto demuestra lo poderoso que es Numba incluso sin paralelismo.

2. Paralelismo solo (@njit(parallel=True)) no mejoró

    Tiempo: 0.1144s ≈ igual a secuencial

    En este caso, el uso de prange no dio ventaja porque:

        Puede que tu CPU tenga pocos núcleos usables en Python.

        O la operación es demasiado rápida ya, y el overhead de paralelismo anula los beneficios.

3. Fastmath con Paralelismo fue el gran ganador

    Tiempo: 0.0307s → el más rápido con diferencia (~4x más rápido que @njit)

    El uso de fastmath=True permite que Numba aplique optimizaciones matemáticas agresivas (por ejemplo, reordenar sumas o multiplicaciones).

    Esto sugiere que hay operaciones optimizables incluso con enteros.

4. fastmath o cache por sí solos no ayudan

    fastmath: 0.2790s

    cache: 0.2491s

    Esto muestra que por sí solos no mejoran nada en tiempo de ejecución (cache es útil si corrés muchas veces el mismo script, no para acelerar un solo run).

5. La combinación completa fue la peor 

    Tiempo: 1.0944s (más lento que todos)

    Probablemente el uso combinado de cache=True y parallel=True generó algún overhead de compilación o ejecución no óptimo en este contexto.

    No siempre "todo activado" es mejor.