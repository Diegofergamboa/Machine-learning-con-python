#Script para empezar a usar con mas propiedad la libreria de Pandas.

import pandas as pd


datos = pd.read_excel('data_tienda.xlsx')


print(datos)

print('Estadisticas del Frame: ')

print(datos.describe())



