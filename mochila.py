from os import sep
import sys
import time
import numpy as np
from numpy.lib.type_check import real
import pandas as pd

if (len(sys.argv)==5 or len(sys.argv)==2):
          if len(sys.argv)==2:
                    semilla = 1
                    tau = 1.4
                    ite = 100
                    entrada = sys.argv[1]
                    print(' <--- Valores --->\nSemilla: ', semilla,'\nTau: ', tau,'\nIteraciones: ', ite,'\nArchivo: ', entrada)         
          if len(sys.argv)==5:
                    semilla = int(sys.argv[1])
                    tau = float(sys.argv[2])
                    ite = int(sys.argv[3])
                    entrada = sys.argv[4]
                    print(' <--- Valores --->\nSemilla: ', semilla,'\nTau: ', tau,'\nIteraciones: ', ite,'\nArchivo: ', entrada)        
else:
          print("Error al ingresar los parametros.")
          sys.exit(0)

tiempo_proceso_ini = time.process_time()
np.random.seed(semilla)

def calculaPeso(data, cantidadElementos):
          peso = 0
          for i in range (cantidadElementos):
                    if(data[i][2]==1):
                              peso=peso+data[i][1]
          return peso

def calculaValor(data, cantidadElementos):
          valor = 0
          for i in range (cantidadElementos):
                    if(data[i][2]==1):
                              valor=valor+data[i][0]
          return valor

data = pd.read_csv(entrada,sep='\t',header=None).to_numpy()
nombreArchivo = data[0][0]
cantidadElementos = data[1][1]
capacidadMochila = data[2][1]
valorOptimo = data[3][1]
data = pd.read_csv(entrada,sep='\t',header=None, skiprows=5, skipfooter=1, engine='python')
data = data.drop(columns=0, axis=1).to_numpy()
cantidadElementos = data.shape[0]
#print(data)
print(' <---Datos leidos --->\nNombre Archivo: ', nombreArchivo,'\nCantidad elementos: ', cantidadElementos,'\nCapacidad mochila: ', capacidadMochila,'\nValor optimo: ',valorOptimo)
print('<-------------------------->\n\n')
for i in range(cantidadElementos):
          data[i][2] = 0

for i in range (cantidadElementos):
          numRandom = np.random.rand(1)
          if(numRandom<0.5):
                    data[i][2]=0
          else:
                    data[i][2]=1

mejorSolucion = data
mejorSolucionPeso = calculaPeso(data,cantidadElementos)
mejorSolucionValor = calculaValor(data,cantidadElementos)
mejorSolucionGeneracion = 0
print('Solucion inicial y mejor solucion: \n',data)
print('Valor solucion inicial: ',calculaValor(mejorSolucion,cantidadElementos))
print('Peso solucion inicial: ',calculaPeso(mejorSolucion,cantidadElementos))

if(mejorSolucionPeso > capacidadMochila):
          print('Solucion inicial no factible\n')
          #for i in range(cantidadElementos):
                    #mejorSolucion[i][2] = 0
          mejorSolucionPeso = 99999999
          mejorSolucionValor = 0
else:
          print('Solucion inicial factible')

generacion = 0
while generacion < ite:

          cantidadValoresDentroMochila = 0
          elementosDentroMochila = []

          cantidadValoresFueraMochila = 0
          elementosFueraMochila = []

          if(calculaPeso(data,cantidadElementos)>capacidadMochila):
                    for i in range(cantidadElementos):
                              if(data[i][2] == 1):
                                        cantidadValoresDentroMochila=cantidadValoresDentroMochila + 1     
                                        elementosDentroMochila.append([i, data[i][0]/data[i][1]])
                    ##print('cantidad elementos dentro de la mochila: ',cantidadValoresDentroMochila)    
                    ##print('lista elementos dentro de la mochila',elementosDentroMochila)   
                      
                    #vector probabilidades dentro while
                    vectorProbabilidades = np.full((cantidadValoresDentroMochila),fill_value=-1,dtype=float)
                    sumVectorProbabilidades = 0
                    for i in range(cantidadValoresDentroMochila):
                              vectorProbabilidades[i] = (i+1)** -tau
                              sumVectorProbabilidades = sumVectorProbabilidades+((i+1)** -tau)
                    #print('Vector probabilidades dentro iteracion:\n',vectorProbabilidades)

                    #vector de proporciones dentro while
                    vectorProporciones = np.full((cantidadValoresDentroMochila),fill_value=-1,dtype=float)
                    sumVectorProporciones = 0
                    for i in range(cantidadValoresDentroMochila):
                              vectorProporciones[i]=vectorProbabilidades[i]/sumVectorProbabilidades
                              #sumVectorProporciones = sumVectorProporciones+vectorProbabilidades[i]/sumVectorProbabilidades
                    #print('Vector proporciones dentro iteracion:\n',vectorProporciones)
                    #print(sumVectorProporciones)

                    #vector ruleta dentro while
                    vectorRuleta = np.full((cantidadValoresDentroMochila),fill_value=-1,dtype=float)
                    for i in range(cantidadValoresDentroMochila):
                              if(i==0):
                                        vectorRuleta[i]=vectorProporciones[i]
                              else:
                                        vectorRuleta[i] = vectorRuleta[i-1]+vectorProporciones[i]
                    #print('Ruleta dentro iteracion: \n',vectorRuleta)

                    elementosDentroMochila = sorted(elementosDentroMochila, key=lambda fitness : fitness[1])
                    ##print('lista ordenada: ',elementosDentroMochila)

                    #fitness dentro while
                    #vectorFitness = np.full((cantidadValoresDentroMochila),fill_value=-1,dtype=float)
                    #for i in range(cantidadValoresDentroMochila):
                    #          vectorFitness[i] = data[elementosDentroMochila[i]][0]/data[elementosDentroMochila[i]][1]
                    #print('Vector fitness dentro iteracion: \n', vectorFitness)

                    #fitness ordenado dentro while
                    #vectorFitnessOrdenado = vectorFitness
                    #vectorFitnessOrdenado =  np.sort(vectorFitnessOrdenado)
                    #vectorFitnessOrdenado = np.flip(vectorFitnessOrdenado)
                    #print('Vector fitness ordenado dentro iteracion: \n', vectorFitnessOrdenado)

                    #seleccion ruleta
                    numRandom = np.random.rand(1)
                    for i in range(vectorRuleta.shape[0]):
                              if(numRandom <= vectorRuleta[i]):
                                        seleccion = i
                                        break
                    #print('numero aleatorio: ',numRandom,'indice de ruleta seleccionado: ',seleccion)

                    #print(data[elementosDentroMochila[seleccion]][2])
                    ##print('elemnto dentro seleccion: ',elementosDentroMochila[seleccion])
                    ##print('elemnto dentro seleccion: ',elementosDentroMochila[seleccion][0])

                    
                    
                    data[elementosDentroMochila[seleccion][0]][2]=0
                    #for i in range(cantidadElementos):
                    #          if (vectorFitnessOrdenado[seleccion]==data[i][0]/data[i][1]):
                                        #print('encontro coincidencia', vectorFitnessOrdenado[seleccion], '              ', data[i][0]/data[i][1])
                    #                    indice=i
                    #                    break
                    #print('el indice es: ', indice)
                    #data[indice][2] =0 
                    ##print("se cambio el valor : ", elementosDentroMochila[seleccion]," por: ",0)

                    ##print('nueva sol: ', data)
          
          
          else:
                    for i in range(cantidadElementos):
                              if(data[i][2] == 0):
                                        cantidadValoresFueraMochila=cantidadValoresFueraMochila + 1     
                                        elementosFueraMochila.append([i,data[i][0]/data[i][1]]) 
                    ##print('elementos fuera de la mochila: ',cantidadValoresFueraMochila)

                    #vector probabilidades dentro while
                    vectorProbabilidades = np.full((cantidadValoresFueraMochila),fill_value=-1,dtype=float)
                    sumVectorProbabilidades = 0
                    for i in range(cantidadValoresFueraMochila):
                              vectorProbabilidades[i] = (i+1)** -tau
                              sumVectorProbabilidades = sumVectorProbabilidades+((i+1)** -tau)
                   # print('Vector probabilidades dentro iteracion else:\n',vectorProbabilidades)

                    #vector de proporciones dentro while
                    vectorProporciones = np.full((cantidadValoresFueraMochila),fill_value=-1,dtype=float)
                    sumVectorProporciones = 0
                    for i in range(cantidadValoresFueraMochila):
                              vectorProporciones[i]=vectorProbabilidades[i]/sumVectorProbabilidades
                              #sumVectorProporciones = sumVectorProporciones+vectorProbabilidades[i]/sumVectorProbabilidades
                    #print('Vector proporciones dentro iteracion else:\n',vectorProporciones)
                    #print(sumVectorProporciones)

                    #vector ruleta dentro while
                    vectorRuleta = np.full((cantidadValoresFueraMochila),fill_value=-1,dtype=float)
                    for i in range(cantidadValoresFueraMochila):
                              if(i==0):
                                        vectorRuleta[i]=vectorProporciones[i]
                              else:
                                        vectorRuleta[i] = vectorRuleta[i-1]+vectorProporciones[i]
                    #print('Ruleta dentro iteracion else: \n',vectorRuleta)

                    elementosFueraMochila = sorted(elementosFueraMochila, key=lambda fitness : fitness[1],reverse=True)
                    ##print('lista ordenada: ',elementosFueraMochila)

                    #fitness dentro while
                    #vectorFitness = np.full((cantidadValoresFueraMochila),fill_value=-1,dtype=float)
                    #for i in range(cantidadValoresFueraMochila):
                    #          vectorFitness[i] = data[elementosFueraMochila[i]][0]/data[elementosFueraMochila[i]][1]
                    #print('Vector fitness dentro iteracion else: \n', vectorFitness)

                    #fitness ordenado dentro while
                    #vectorFitnessOrdenado = vectorFitness
                   # vectorFitnessOrdenado =  np.sort(vectorFitnessOrdenado)
                    #vectorFitnessOrdenado = np.flip(vectorFitnessOrdenado)
                    #print('Vector fitness ordenado dentro iteracion else: \n', vectorFitnessOrdenado)

                    #seleccion ruleta
                    numRandom = np.random.rand(1)
                    for i in range(vectorRuleta.shape[0]):
                              if(numRandom <= vectorRuleta[i]):
                                        seleccion = i
                                        break
                    #print('numero aleatorio: ',numRandom,'indice de ruleta seleccionado: ',seleccion)

                    
                    data[elementosFueraMochila[seleccion][0]][2]=1
                    #for i in range(cantidadElementos):
                    #          if (vectorFitnessOrdenado[seleccion]==data[i][0]/data[i][1]):
                                        #print('encontro coincidencia', vectorFitnessOrdenado[seleccion], '              ', data[i][0]/data[i][1])
                    #                    indice=i
                    #                    break
                    #print('el indice es: ', indice)
                    #data[indice][2] =1 
                    ##print("se cambio el valor : ", elementosFueraMochila[seleccion]," por: ",1)

                    



         
          
          print('Generacion: ',generacion)
          #print(data)
          ##print('Valor: ',calculaValor(data,cantidadElementos))
          ##print('Peso: ',calculaPeso(data,cantidadElementos))

          if(calculaPeso(data,cantidadElementos)<=capacidadMochila and calculaValor(data,cantidadElementos) >= mejorSolucionValor):
                    mejorSolucion=data
                    mejorSolucionPeso= calculaPeso(mejorSolucion,cantidadElementos)
                    mejorSolucionValor = calculaValor(mejorSolucion, cantidadElementos)
                    print('Se actualizo mejor solucion')
                    print('Peso: ',mejorSolucionPeso)
                    print('Valor: ',mejorSolucionValor)
                    mejorSolucionGeneracion  = generacion

          if(mejorSolucionValor == valorOptimo):
                    print('Se alcanzo la mejor solucion')
                    generacion = ite
          generacion+=1

tiempo_proceso_fin =time.process_time()
print('\n\n<--- Terminado --->')
print('Tiempo de Procesamiento: %f segundos' % (tiempo_proceso_fin - tiempo_proceso_ini))
print('Resultados')
print('Mejor solucion: \n',mejorSolucion)
print('Peso mejor solucion: ', mejorSolucionPeso)
print('Valor mejor solucion: ', mejorSolucionValor)
print('Iteracion mejor solucion: ', mejorSolucionGeneracion)
print('Valor ideal: ', valorOptimo)
print('Proceso terminado')
print('<--------------------------->')




#print('Solucion inicial y a la vez la mejor solucion: \n',data)
#print('Peso mejor solucion: ',mejorSolucionPeso)
#print('Valor mejor solucion: ', mejorSolucionValor)
#if(mejorSolucionPeso<=capacidadMochila):
#          print('Es una solucion valida')
#else:
#          print('No es una solucion valida')
