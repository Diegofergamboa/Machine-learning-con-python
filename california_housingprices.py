# -*- coding: utf-8 -*-
'''
    Proyecto para mejorar los conocimiento aprendidos en la aplicacion
    de regresion lineal
'''

#Importacion de librerias

import numpy as np
import matplotlib.pyplot as plt

#De donde se extraen los datos directamente siendo de Scikit learn

from sklearn import datasets, linear_model

#Primero conocer los datos con los que estoy tratando importando y sacando datos

california = datasets.load_boston()
print(california)
print()
#Keys es la informacion mas relevante de la data
print('Informacion de los datos')
print('')
print(california.keys())
print()
#COn DESCR conozco mas a profundida la naturaleza de los datos
print('La informacion de los datos a profundidad es: ')
print(california.DESCR)