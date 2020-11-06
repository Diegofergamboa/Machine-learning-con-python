# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
 
name_age = {'Name' : ['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
'Age' : [32, 55, 20, 43, 30]}
data_frame = pd.DataFrame(name_age)
print (data_frame)


paises_capitales_clima = {'Pais': ['Colombia','Argentina','Peru','Mexico','Chile'],
                    'Capital': ['Bogota','Buenos Aires','LIma','CDMX','Santiago'],
                    'Clima': ['Frio','Seasons','Frio','Caliente','Frio'] }
frame_modelo = pd.DataFrame(paises_capitales_clima)
print(frame_modelo)

#Muestra la forma de los datos .shape

print(frame_modelo.shape)

#Con la funcion LEN con index muestra la altura de los datos

print(len(frame_modelo.index))

#Estadisticas del DataFrame (Preferible con datos numeros)

print('Estadisticas del Frame: ')
print(frame_modelo.describe())

#Para la media usar .MEAN

print(data_frame.mean)

#Para la correlacion entre variables CORR

print(frame_modelo.corr())

#Para contar la cantidad de datos

print(data_frame.count())

#Para conocer el maximo -max- para conocer el minimo -min-
#Para conocer la mediana es con la funcion median
#Para conocer la desviacion se usa STD

print('La primera columna de los paises es: ')
print(data_frame['Pais'])


#Importar los datos.  Abrir un archivo local usar importante

#pd.read_tipodearchivo()




