#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:29:39 2020

@author: diegofergamboa
"""
#Importando librerias

from sklearn import datasets, linear_model
import numpy as np
import matplotlib as plt

#Importa la base de datos desde  scilearn

boston = datasets.load_boston()

#Informaciòn del Dataset

print('La informacion general de la data es: ')
print(boston.keys())

print('La nombres de las columnas de datos de la data es de: ')
print(boston.feature_names)

print('La informacion completa del data set')
print(boston.DESCR)

print('La cantidad de datos es: ')
print(boston.data.shape)
print('Es decir hay 506 datos en 13 modulos')

'''
    Para el modelo se van a usar como vaariables explicativas 'AGE' como edad,
    'RM' la cantidad de habitaciones y, 'DIS' la cual es la distancia de las casas
    de los centros de trabajo mas importantes de la ciudad
'''

#Comenzamos a construir
#Son las celdas 5, 6 y 7 del SET de datos.

#Construimos el constructor de X

X_multiple = boston.data[:,5:8]

#Definimos ahora y

y_multiple = boston.target

'''
    Ahora se van a separar los datos en entrenamiento y en base normal
'''

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

#Defino el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

#Usamos linear regresion

lr_multiple.fit(X_train, y_train)

#Realizamos la prediccion

Y_pred_multiple = lr_multiple.predict(X_test)

'''
    Valores de los coeficientes
'''

print('DATOS DEL MODELO REGRESIÓN LINEAL MULTIPLE')
print()
print('Valor de las pendientes o coeficientes "a":')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b":')
print(lr_multiple.intercept_)

'''
    Presiciòn del modelo con R cuadrado
'''

print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train))


