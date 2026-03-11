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

# Listas
frutas = ["manzana", "banana", "cereza"]
print(f"Frutas: {frutas}")

# Tuples
coordenadas = (10, 20)
print(f"Coordenadas: {coordenadas}")

# Sets
numeros = {1, 2, 3, 4, 5}
print(f"Números: {numeros}")

# Frozensets
colores = frozenset(["rojo", "verde", "azul"])
print(f"Colores: {colores}")

# Diccionarios
persona = {"nombre": "Alice", "edad": 30, "ciudad": "Madrid"}
print(f"Persona: {persona}")

# Bytearrays
datos = bytearray(b"Hola Mundo")
print(f"Datos: {datos}")

# Range
rango = range(1, 10)
print(f"Rango: {list(rango)}")

# Memoryview
memoria = memoryview(b"Hola Mundo")
print(f"Memoria: {memoria}")