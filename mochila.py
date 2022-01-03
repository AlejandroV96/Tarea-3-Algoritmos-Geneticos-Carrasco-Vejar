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
                      
                    #vector probabilidades
                    vectorProbabilidades = np.full((cantidadValoresDentroMochila),fill_value=-1,dtype=float)
                    sumVectorProbabilidades = 0
                    for i in range(cantidadValoresDentroMochila):
                              vectorProbabilidades[i] = (i+1)** -tau
                              sumVectorProbabilidades = sumVectorProbabilidades+((i+1)** -tau)
                    
                    #vector de proporciones
                    vectorProporciones = np.full((cantidadValoresDentroMochila),fill_value=-1,dtype=float)
                    sumVectorProporciones = 0
                    for i in range(cantidadValoresDentroMochila):
                              vectorProporciones[i]=vectorProbabilidades[i]/sumVectorProbabilidades
                    
                    #vector ruleta
                    vectorRuleta = np.full((cantidadValoresDentroMochila),fill_value=-1,dtype=float)
                    for i in range(cantidadValoresDentroMochila):
                              if(i==0):
                                        vectorRuleta[i]=vectorProporciones[i]
                              else:
                                        vectorRuleta[i] = vectorRuleta[i-1]+vectorProporciones[i]
                   
                    #list ordenada de acuerdo al fitness
                    elementosDentroMochila = sorted(elementosDentroMochila, key=lambda fitness : fitness[1])
                    
                     #seleccion ruleta
                    numRandom = np.random.rand(1)
                    for i in range(vectorRuleta.shape[0]):
                              if(numRandom <= vectorRuleta[i]):
                                        seleccion = i
                                        break
                    
                    data[elementosDentroMochila[seleccion][0]][2]=0
          
          else:
                    for i in range(cantidadElementos):
                              if(data[i][2] == 0):
                                        cantidadValoresFueraMochila=cantidadValoresFueraMochila + 1     
                                        elementosFueraMochila.append([i,data[i][0]/data[i][1]]) 
                    
                    #vector probabilidades dentro while
                    vectorProbabilidades = np.full((cantidadValoresFueraMochila),fill_value=-1,dtype=float)
                    sumVectorProbabilidades = 0
                    for i in range(cantidadValoresFueraMochila):
                              vectorProbabilidades[i] = (i+1)** -tau
                              sumVectorProbabilidades = sumVectorProbabilidades+((i+1)** -tau)
                   
                    #vector de proporciones dentro while
                    vectorProporciones = np.full((cantidadValoresFueraMochila),fill_value=-1,dtype=float)
                    sumVectorProporciones = 0
                    for i in range(cantidadValoresFueraMochila):
                              vectorProporciones[i]=vectorProbabilidades[i]/sumVectorProbabilidades
                    
                    #vector ruleta dentro while
                    vectorRuleta = np.full((cantidadValoresFueraMochila),fill_value=-1,dtype=float)
                    for i in range(cantidadValoresFueraMochila):
                              if(i==0):
                                        vectorRuleta[i]=vectorProporciones[i]
                              else:
                                        vectorRuleta[i] = vectorRuleta[i-1]+vectorProporciones[i]
                    
                    #lista ordenada
                    elementosFueraMochila = sorted(elementosFueraMochila, key=lambda fitness : fitness[1],reverse=True)
                    
                    #seleccion ruleta
                    numRandom = np.random.rand(1)
                    for i in range(vectorRuleta.shape[0]):
                              if(numRandom <= vectorRuleta[i]):
                                        seleccion = i
                                        break
                    
                    data[elementosFueraMochila[seleccion][0]][2]=1
                    
          print('Generacion: ',generacion)

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