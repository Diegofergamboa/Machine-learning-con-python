
'''
    Practica
'''

'''
    Grafica de linea
'''
import matplotlib.pyplot as plt

#Se crean los datos
x1 = [3,4,5,6] 
y1 = [2,5,8,7]
x2 = [7,8,10,11]
y2 = [3,4,3,7]

#Caracteristicas del grafico

plt.plot(x1, y1, label = 'Linea 1', linewidth = 4, color = 'red')
plt.plot(x2, y2, label = 'Linea 2', linewidth = 4, color = 'blue')

#Definir titulo y nombres de graficos

plt.title('Diagrama de lineas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar leyenda cuadricula y figura

plt.legend()
plt.grid()
plt.show()










































# -*- coding: utf-8 -*-

