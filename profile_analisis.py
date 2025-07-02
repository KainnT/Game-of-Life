# -------------------- requirements -------

import cProfile
import pstats
import shutil
import subprocess
from game_of_life import GameOfLife

#-------- simulacion definida ----------

def simulation(rows=512, cols=512, steps=100): #funcion predefinida que toma la cantidad definida de filas y columnas para el juego gameoflife
    game = GameOfLife(rows, cols)
    game.run(steps)
    

def main(): #la funcion main corre la simulacion con la libreria cprofile para el analisis de rendimiento
    profiler = cProfile.Profile() # este es un objeto que se crea con la intencion de medir el rendimiento del codigo
    profiler.enable() #se da inicio a la recoleccion de datos
    
    simulation() #ejecuta la simulacion de game of like previamente creada
    
    profiler.disable() #detiene la simulacion y recolecta los datos en un archivo de texto
    profiler.dump_stats("Output.pstats")
    
    with open("output.txt", "w") as f: #este objeto se crea para analizar los datos que saca el perfilador
        stats = pstats.Stats(profiler, stream=f)
        stats.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats()
        
    if shutil.which("snakeviz"): #este if se crea para garantizar que el usuarip que corra este codigo tenga la libreria necesaria de snakeviz
        print("Visualizacion en curso") #si lo esta, crea el output file que genera la visualizacion
        subprocess.run(["snakeviz", "output.pstats"])
    else: 
        print("Instalar snakeviz con pip install...")


if __name__ == "__main__": #ejecuta la funcion que recolecta y visualiza los datos
    main()
