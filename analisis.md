-------- Analisis de los resultados -------
1. grafico tiempo vs tamanno:

Para este grafico se muestra el tiempo promedidado por iteracion en donde este aumenta conforma crece el numero de celdas
por lo que podemos observar una escala lineal.
Cuando se observa la curva denominada empirica (linea azul) se puede ver que existe de forma casi lineal 
por lo que se coincide con la curve teorica o (O(n))
cuando se observan las curcas O(n log n ) y O(n^2) se observa una linea por encima de la curva o linea empirica
lo que significa que el algoritmo que se registra logra ser mas eficiente, esto puede estar relacionado a dierentes factores como la 
utilizacion de librerias que nos permiten automatizar ciertos flujos o acelerar el tiempo que el codigo dura en correr, comp numba.

2. El grafico de escala log-log lo que mide es la tendencia del crecimiento cuando se registra a grandes escalas,
en este mismo  tambien se encuetntra la curva empirica, espresada con el color azul, cuya pendiente se acerca a 1,
lo que en realidad, prueba la hipotesis de que el tiempo de la ejecucion escala como O(n)
en cuanto a la se;alizacion de crecimiento cuadratico (O(n^2)) no se presentan se;ales de este, lo que denota que el algoritmo presenta cualidades positivas.

---------------------------------------------------------------------------------------------------------------------
Como escala:

El escalamiento del juego se presenta de forma lineal respecto al numero se celdas.
por lo que se puede denotar que:

- si se toma el tiemp por iteracion, este aumenta de manera proporcional al area del tablero.

- en terminos de cuellos de botellam no se presentan grandes saltos en los tama;os que se presentaron, sin embargo, cuando se comenta de posibles limitacions
podemos encontrar: al ser lineal, si el numero de celdas del tablero crece, el tiempo aumenta por lo que se puede empezar a ver ciertas limitacions con la cantidad se nucleos en el CPU.
- al decdir usa numba: sin paralel=True, significa que solo decidimos utilizar un hilo de CPU, lo que limita el rendimiento de los sistemas al aplicarse en multinucleos.
- la medicion se enfoca en tiempo, por lo que no tenemos calculos de variavles como animacion, sin embargo, para efectos del proyecto no es necesario.
- al utilizar range y no prange en el class game of life numba no esta utilizando bucles.

