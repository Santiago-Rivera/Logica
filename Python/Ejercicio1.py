"""
Operadores
"""

# Operadores aritméticos
print(f"Suma: {5 + 3} = {5 + 3}")
print(f"Resta: {5 - 3} = {5 - 3}")
print(f"Multiplicación: {5 * 3} = {5 * 3}")
print(f"División: {5 / 3} = {5 / 3}")
print(f"División entera: {5 // 3} = {5 // 3}")
print(f"Módulo: {5 % 3} = {5 % 3}")
print(f"Exponenciación: {5 ** 3} = {5 ** 3}")

# Operadores de comparación
print(f"¿5 es igual a 3? {5 == 3}")
print(f"¿5 es diferente de 3? {5 != 3}")
print(f"¿5 es mayor que 3? {5 > 3}")
print(f"¿5 es menor que 3? {5 < 3}")
print(f"¿5 es mayor o igual a 3? {5 >= 3}")
print(f"¿5 es menor o igual a 3? {5 <= 3}")

# Operadores lógicos
print(f"¿5 es mayor que 3 y menor que 10? {(5 > 3) and (5 < 10)}")
print(f"¿5 es mayor que 3 o menor que 2? {(5 > 3) or (5 < 2)}")
print(f"¿No es cierto que 5 es menor que 3? {not (5 < 3)}")

# Operadores de asignación
x = 5
print(f"Valor inicial de x: {x}")
x += 3
print(f"Después de x += 3: {x}")
x -= 2
print(f"Después de x -= 2: {x}")
x *= 4
print(f"Después de x *= 4: {x}")
x /= 2
print(f"Después de x /= 2: {x}")
x //= 3
print(f"Después de x //= 3: {x}")
x %= 2
print(f"Después de x %= 2: {x}")
x **= 2
print(f"Después de x **= 2: {x}")

# Operadores de identidad
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(f"¿a es b? {a is b}")
print(f"¿a es c? {a is not c}")
print(f"¿a es igual a c? {a == c}")

# Operadores de pertenencia
print(f"¿3 está en a? {3 in a}")
print(f"¿4 está en a? {4 in a}")
print(f"¿5 no está en a? {5 not in a}")

# Operadores bit a bit
print(f"AND bit a bit: {5 & 3} = {bin(5)} & {bin(3)} = {bin(5 & 3)}")
print(f"OR bit a bit: {5 | 3} = {bin(5)} | {bin(3)} = {bin(5 | 3)}")
print(f"XOR bit a bit: {5 ^ 3} = {bin(5)} ^ {bin(3)} = {bin(5 ^ 3)}")
print(f"Desplazamiento a la izquierda: {5 << 1} = {bin(5)} << 1 = {bin(5 << 1)}")
print(f"Desplazamiento a la derecha: {5 >> 1} = {bin(5)} >> 1 = {bin(5 >> 1)}")
print(f"NOT bit a bit: ~5 = ~{bin(5)} = {bin(~5)}")

"""
Estructuras de control
"""

# Estructura condicional if
x = 10
if x > 0:
    print(f"{x} es un número positivo.")
elif x < 0:
    print(f"{x} es un número negativo.")
else:
    print(f"{x} es cero.")

# Estructura de repetición for
print("Números del 0 al 4:")
for i in range(5):
    print(i)

# Estructura de repetición while
print("Números del 0 al 4 usando while:")
i = 0
while i < 5:
    print(i)
    i += 1 

# Estructura de control de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Este bloque se ejecuta siempre, haya o no una excepción.")
    
print("Dificultad extra:")
for i in range(10, 55):
    if i % 2 == 0 and i != 16 and i % 3 != 0: # Si i es par, no es 16 y no es múltiplo de 3, entonces se imprime
        print(i)