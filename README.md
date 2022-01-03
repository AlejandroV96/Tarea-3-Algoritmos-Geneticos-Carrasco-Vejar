# Problema de la mochila a través del metodo de Extremal Optimisation.
Alejandro Vejar Henriquez
Kevin Carrasco Zenteno

Aca se presenta la implementación en Python de la solución para el problema de las mochila mediante la implementación del Extremal Optimisation.
El problema consisten en modelar una situación análoga al llenar una mochila, incapaz de soportar más de un peso determinado, con todo o parte de un conjunto de objetos, cada uno con un peso y valor específicos. Los objetos colocados en la mochila deben maximizar el valor total sin exceder el peso máximo.

Parametros utilizados por el programa.

Semilla: Este parametro representa el valor de semilla del programa, a partir de este numero se generan los valores aleatorios, se debe ingresar un numero entero. Ejemplo: 3

Cantidad de iteraciones: Este parametro representa la cantidad de iteraciones (generaciones) que tendra el sistema, se debe ingresar un valor entero mayor o igual 1.

Valor de Tau: 

Archivo de entrada: Archivo de entrada de la mochila que posee todos los elementos con sus respectivos valores, pesos y estado si se encuentra o no dentro de la mochila, tambien posee la cantidad de elementos, el valor ideal de la mejor solución y el peso de la mejor solución.

Instrucciones para correr el programa en Linux con los parametros base.

> $ git clone https://github.com/kevincarrascoz/Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar.git

> $ cd Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar

> $ python3 .\mochila.py small50.txt

Instrucciones para correr el programa en Linux con los parametros ingresados por el usuario.

> $ git clone https://github.com/kevincarrascoz/Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar.git

> $ cd Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar

> $ python3 .\mochila.py 1 1.4 300 small50.txt
