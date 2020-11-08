# -*- coding: utf-8 -*-

'''
    Regresion lineal practica para predecir el valor de las casas en Boston
'''

import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

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

#Con shape se cuenta la cantidad de datos que tienen

print('La cantidad de datos es de: ')
print(boston.data.shape)

#Con este podemos ver la informacion de las columnas con mas detalle
#Tan solo el nombre que tiene cada columna

print('El nombre de las columnas!: ')
print(boston.feature_names)

'''
    En este punto ya se va a empezar a definir como tal el 
    algoritmo de regresion lineal simple
'''

# Se seleccionan las columnas o variables que se van a usar 
# Para este ejemplo se va a usar la numero 5
# Para eso lo definimos de la siguiente manera

X = boston.data[:, np.newaxis, 5]

#Definir los datos correspondientes a las etiquetas

y = boston.target

######################## GRAFICAR LO QUE SE LLEVA CON SCATTER

plt.scatter(X, y)
plt.xlabel('Numero de habitaciones')
plt.ylabel('Valor medio')
plt.show()

'''
    Como lo primero que debemos hacer es separar los datos 
    en entrenamiento y prueba lo hacemos utilizando la instrucción
    train_test_split, no si antes importando la respectiva librería.
'''

#Importo el test de la libreria

from sklearn.model_selection import train_test_split

#Ahora se separan los datos de train con los de prueba real

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Definimos el algoritmo a utilizar que en este caso va a ser Regresion Lineal

lr = linear_model.LinearRegression()

#Entrenamos el modelo con los datos de entrenamiento y utilizando la instruccion fit

#Se entrena

lr.fit(X_train, y_train)

#Finalmente, realizamos la prediccion

Y_pred = lr.predict(X_test)

#Graficamos los datos junto con el modelo

plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title('Regresión Lineal Simple')
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()

#Terminar de modelar la ecuacion

print('DATOS DEL MODELO REGRESIÓN LINEAL SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a":')
print(lr.coef_)
print('Valor de la intersección o coeficiente "b":')
print(lr.intercept_)
print()
print('La ecuación del modelo es igual a:')
print('y = ', lr.coef_, 'x ', lr.intercept_)

# Precision del modelo o R cuadrado

print('Precisión del modelo:')
print(lr.score(X_train, y_train))