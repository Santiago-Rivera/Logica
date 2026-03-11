"""
Funciones
"""

# Simple

def function():
    print("Hello World")

# con retorno

def function_with_parameters(name):
    return f"Hello {name}"

# con argumentos

def function_with_arguments(name, age):
    return f"Hello {name}, you are {age} years old"

# con argumentos por defecto

def function_with_default_arguments(name="World"):
    return f"Hello {name}"

# Con argumentos y return

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Brais"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")


variable_arg_greet("Python", "Brais", "MoureDev", "comunidad")

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("MoureDev"))
print(type(36))
print("MoureDev".upper())

"""
Variables locales y globales
"""

global_var = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")


print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()

"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))