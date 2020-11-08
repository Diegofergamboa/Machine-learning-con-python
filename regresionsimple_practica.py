# -*- coding: utf-8 -*-

'''
    Regresion lineal practica para predecir el valor de las casas en Boston
'''

import numpy as np
from sklearn import datasets, linear_model
import matplotlib as plt

########## PREPARAR LA DATA #########

#Importamos los datos de la misma libreria Scikit - learn
boston = datasets.load_boston()
print(boston)
print()

########## ENTENDIMIENTO DE LA DATA ########

#Verificacion de la informacion contenida en el dataset

print('Informacion de los datos')
print('')
print(boston.keys())
print()

##### CARACTERISTICAS DEL DATASET #######

print('Caracteristicas del Dataset')
print(boston.DESCR)