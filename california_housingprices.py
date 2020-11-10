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

#Con DESCR conozco mas a profundida la naturaleza de los datos

print('La informacion de los datos a profundidad es: ')
print(california.DESCR) 

#Con shape se cuenta la cantidad de datos que hay, hay que poner la data antes

print('La cantidad de datos que hay es: ')
print(california.data.shape)

#Con este podemos ver el nombre de las columnas

print('EL nombre de las columnas es: ')
print(california.feature_names)

#Con este podemos importar el porcentaje de personas de bajo nivel

X = california.data[:, np.newaxis, 7]

#Definir el target

y = california.target

######################## GRAFICAR LO QUE SE LLEVA CON SCATTER

plt.scatter(X, y)
plt.xlabel('Porcentaje de personas pobres')
plt.ylabel('Valor medio')
plt.show()

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
plt.xlabel('Porcentaje de personas pobres')
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