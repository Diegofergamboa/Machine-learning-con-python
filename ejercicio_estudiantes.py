#Script para empezar a usar con mas propiedad la libreria de Pandas.

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_excel('data_tienda.xlsx')


#Linea de comandos para estadistica.
print(datos)

#Linea de comandos para para estadistica.

print('Estadisticas del Frame: ')

#LInea de comenados para sacar datos estadisticos datos cuantitativos

print(datos.describe())

#Grafico matplob

#declaracion de variables

a =[1,2,3,4] 
b =[7,10,11,15]

plt.plot(a,b)
plt.show()










