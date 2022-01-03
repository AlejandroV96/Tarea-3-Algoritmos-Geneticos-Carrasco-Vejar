# Problema de la mochila a través del metodo de Extremal Optimisation.
Alejandro Vejar Henriquez,
Kevin Carrasco Zenteno

Acá se presenta la implementación en Python de la solución para el problema de la mochila mediante la implementación de Extremal Optimisation.
El problema consiste en modelar una situación análoga al llenar una mochila, incapáz de soportar más de un peso determinado, con todo o parte de un conjunto de objetos, cada uno con un peso y valor específicos. Los objetos colocados en la mochila deben maximizar el valor total sin exceder el peso máximo.

Parámetros utilizados por el programa.

Semilla: Este parámetro representa el valor de semilla del programa, a partir de este número se generan los valores aleatorios, este valor está representado por un número entero. Ejemplo: 3

Valor de Tau: Este parámetro sirve para calcular la posibilidad del i-esimo elemento de ser seleccionado según la formula : Pi = i^−τ  , ∀i 1 ≤ i ≤ n . Esta representado por un número real positivo. Ejemplo: 2.2

Cantidad de iteraciones: Este parámetro representa la cantidad de iteraciones que tendrá el sistema, esta representado por un valor entero.

Archivo de entrada: Archivo de entrada de la mochila que posee todos los elementos con sus respectivos valores, pesos y estado si se encuentra o no dentro de la mochila, también posee la cantidad de elementos, el valor ideal de la mejor solución y el peso ideal de la mejor solución a la cual se debe llegar.

El algoritmo utiliza valores por defecto para las variables: semilla, tau y cantidad de iteraciones, en caso que los parámetros no sean especificados al ejecutarlo. Estos valores por defecto son:
  Semilla = 1
  Tau = 1.4
  Iteraciones = 100

Instrucciones para correr el programa en Linux con los parámetros base.

> $ git clone https://github.com/kevincarrascoz/Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar.git

> $ cd Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar

> $ python3 .\mochila.py small50.txt

Instrucciones para correr el programa en Linux con los parámetros ingresados por el usuario. El orden de los parámetros corresponde al nombre del archivo, semilla, tau, iteraciones y nombre del fichero a leer respectivamente.

> $ git clone https://github.com/kevincarrascoz/Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar.git

> $ cd Tarea-3-Algoritmos-Geneticos-Carrasco-Vejar

> $ python3 .\mochila.py 1 1.4 300 small50.txt
