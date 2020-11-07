# -*- coding: utf-8 -*-

'''
    Practica
'''

'''
    Grafica de barras
'''
import matplotlib.pyplot as plt

x1 = [0.5,1.0,1.5,2.0] 
y1 = [10,20,30,40]
x2 = [3.0,4.0,5.0,5.0]
y2 = [3,4,3,7]

#Configurar las caracteristicas del grafico

plt.bar(x1,y1, align = 'center', color = 'red')
plt.bar(x2,y2,align = 'center', color = 'black')

#Dando formato a lo creado anteriormente

plt.title('Grafico de barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Dando la orden
plt.legend()
plt.show()