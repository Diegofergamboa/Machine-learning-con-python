#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:48:21 2020

@author: diegofergamboa
"""

import numpy as np

a = np.array([1,2,3])
print('1D array:')
print(a)
print()
b = np.array([(1,2,3),(4,5,6)])
print(('2D array:'))
print(b)

#Creacion de matrices vacias con Numpy
#Las matrices vacias se usan mas que todo para colocar con espacios
#que luego van a ser rellenados

import numpy as np

unos = np.ones((3,4))
print(unos) 

#Para que la matriz tenga solo ceros
#Se usa np zeros

ceros = np.zeros((3, 4))
print(ceros)

#numeros aleatorios
#se invoca primero la funcion random

aleatorio = np.random.random((2,2))
print(aleatorio)

#Para generar matrices vacias
#invocamos la funcion de la libreria empty

vacia = np.empty((1,1))
print(vacia)

#Para generar matrices con un solo valor en toda la matriz
#se invoca la funcion full

lleno = np.full((200,2),1)
print(lleno)

#Para generar espaciados uniformes
#Muy importante usar la funcion arange para int
#Muy importante usar la funcion linspace para floats

espaciado1 = np.arange(0,100,10)
print(espaciado1)

espaciado2 = np.linspace(0,10,5)
print(espaciado2)

#La tipica matriz de idenidad de Algebra Lineal
#Esta se usa invocando la funcion identify o la funcion 'eye' de la librea np

identidad1 = np.identity(4)
print(identidad1)

identidad2 = np.eye(5,5)
print(identidad2)