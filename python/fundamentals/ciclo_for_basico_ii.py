# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a
# "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def biggie_size(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr


print("---------------------")
print("Executing exercise 1")
print("---------------------")
print(biggie_size([-1, 3, 5, -5]))


# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el
# número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def count_positives(arr):
    num = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            num += 1
    arr[-1] = num
    return arr


print("\n\n")
print("---------------------")
print("Executing exercise 2")
print("---------------------")
print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))


# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sum_total(arr):
    total = 0
    for i in range(0, len(arr)):
        total += arr[i]
    return total

print("\n\n")
print("---------------------")
print("Executing exercise 3")
print("---------------------")
print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))


# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def promedio(arr):
    num = 0
    total = len(arr)
    for i in range(0, total):
        num += arr[i]
    return num / total


print("\n\n")
print("---------------------")
print("Executing exercise 4")
print("---------------------")
print(promedio([1, 2, 3, 4]))


# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0
def longitud(arr):
    return len(arr)


print("\n\n")
print("---------------------")
print("Executing exercise 5")
print("---------------------")
print(longitud([37, 2, 1, -9]))
print(longitud([]))


# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
# Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False
def minimo(arr):
    if len(arr) > 0:
        num = arr[0]
        for i in range(0, len(arr)):
            if arr[i] < num:
                num = arr[i]
        return num
    else:
        return False


print("---------------------")
print("Executing exercise 6")
print("---------------------")
print(minimo([37, 2, 1, -9]))
print(minimo([]))


# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía,
# haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False
def maximo(arr):
    if len(arr) > 0:
        num = arr[0]
        for i in range(0, len(arr)):
            if arr[i] > num:
                num = arr[i]
        return num
    else:
        return False


print("---------------------")
print("Executing exercise 7")
print("---------------------")
print(maximo([37, 2, 1, -9]))
print(maximo([]))


# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total,
# promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9,
# 'máximo': 37, 'longitud': 4}
def ultimate_analysis(arr):
    total = 0
    min_ = arr[0]
    max_ = arr[0]
    size = len(arr)
    for i in range(0, size):
        total += arr[i]
        if arr[i] < min_:
            min_ = arr[i]
        if arr[i] > max_:
            max_ = arr[i]
    return {'totalTotal': total, 'promedio': total / size, 'minimo': min_, 'maximo': max_, 'longitud': size}


print("---------------------")
print("Executing exercise 8")
print("---------------------")
print(ultimate_analysis([37, 2, 1, -9]))


# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos.
# Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def reverse_list(arr):
    size = len(arr)
    for i in range(0, int(size / 2)):
        num1 = arr[i]
        num2 = arr[-1 - i]
        arr[i] = num2
        arr[-1 - i] = num1
    return arr


print("---------------------")
print("Executing exercise 9")
print("---------------------")
print(reverse_list([37, 2, 1, -9]))
