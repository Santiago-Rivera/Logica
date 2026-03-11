# https://python.org

# Este es un comentario de una sola linea

''' 
Este es 
un comentario
de varias
lineas
'''

"""
Este es un comentario 
de varias lineas 
usando comillas dobles
"""

int = 10 # int es una palabra reservada es solo para numeros enteros, pero se puede usar como nombre de variable aunque no es recomendable

int = 23 # se puede reasignar el valor de una variable, pero no se puede cambiar su tipo de dato, por ejemplo, no se puede asignar un string a una variable que ya tiene un int, pero si se puede asignar un float a una variable que ya tiene un int, porque el float es un tipo de dato que puede contener un int.

MY_CONSTANT = 3.14 # por convención

float = 3.4 # float es una palabra reservada es solo para numeros decimales
str = "Hola Mundo" # str es una palabra reservada es solo para cadenas de texto
bool = True # bool es una palabra reservada es solo para valores lógicos

print("¡Hola, Python!")

print(type(int))
print(type(float))
print(type(str))
print(type(bool))