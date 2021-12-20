from os import sep
import sys
import time
import numpy as np
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

data = pd.read_csv(entrada,sep='\t',header=None).to_numpy()
nombreArchivo = data[0][0]
cantidadElementos = data[1][1]
capacidadMochila = data[2][1]
valorOptimo = data[3][1]
data = pd.read_csv(entrada,sep='\t',header=None, skiprows=5, skipfooter=1, engine='python')
data = data.drop(columns=0, axis=1).to_numpy()
print(data)
print(' <---Datos leidos --->\nNombre Archivo: ', nombreArchivo,'\nCantidad elementos: ', cantidadElementos,'\nCapacidad mochila: ', capacidadMochila,'\nValor optimo: ',valorOptimo)