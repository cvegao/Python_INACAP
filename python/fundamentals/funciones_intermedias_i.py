# El objetivo de esta asignación es escribir una sola función, randInt() que tome hasta 2 argumentos.
# Si no se proporcionan argumentos, la función debería devolver un entero aleatorio entre 0 y 100.
# Si solo se proporciona un número máximo, la función debe devolver un número entero aleatorio entre 0
# y el número máximo.
# Si solo se proporciona un número mínimo, la función debe devolver un número entero aleatorio entre el
# número mínimo y 100
# Si se proporcionan un número mínimo y máximo, la función debe devolver un número entero aleatorio entre
# esos 2 valores.
import random


def randInt(min=0 , max=100):
    if max < 0:
        return "ERROR: max no puede ser menor que 0"
    elif min > max:
        return "ERROR: min no puede ser mayor que max"
    num = round(random.random() * (max - min) + min)
    return num


print(randInt())  # debería imprimir un número aleatorio entre 0 a 100
print(randInt(max=50))  # debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50))  # debería imprimir un número aleatorio entre 50 a 100
print(randInt(min=50, max=500))  # debería imprimir un número aleatorio entre 50 y 500
print(randInt(max=-1))
print(randInt(2, 1))
