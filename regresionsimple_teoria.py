# -*- coding: utf-8 -*-
'''
    Practica de Regresion Lineal
'''
'''
DEFINIR ALGORITMO =
linear_model.LinearRegression()
ESTRENAR MODELO =
fit(x,y)
PREDECIR MODELO =
predict(x)
CONOCER PENDIENTE (A)
coef_
CONOCER INTERCEPTO (B)
intercept()
PRESICION DEL MODELO
score(x)`

#MInimizar la distancia vertical y la linea que seria el modelo
#Se va a usar MCO LinearRegression con Scikit Learn

# y = ax1 + ax2 + ax3 + b

#Para conocer el valor de la pendiente a, la formula es: a= algoritmo.coef_
#Para la interseccion se usa la formula que es b = algoritmo.intercept_

#EL rendimiento del algoritmo se evalua directamente despues de realizar
#la estimacion, de lo contrario arrojarà un error el modelo
#Evaluar el rendimiento del logaritmo 
#Usando el R al cuadrado
# precision = algoritmo.score(x_prueba, y_prueba)

