# Nota: Evita usar palabras clave de clase como int, str, list y dict como nombres de variables / parámetros.
# 1. Actualiza los valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


print("1. Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].")


def ex1_1(arr):
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            if arr[i][j] == 10:
                arr[i][j] = 15
    return arr


print(ex1_1(x))

print()
print("1.2. Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'")


def ex_1_2(arr):
    arr[0]['last_name'] = 'Bryant'
    return arr


print(ex_1_2(students))

print()
print("1.3. En el directorio sports_directory, cambia 'Messi' a 'Andres'")


def ex_1_3(d):
    d['soccer'][0] = 'Andres'
    return d


print(ex_1_3(sports_directory))

print()
print("1.4. Cambia el valor 20 en z a 30")


def ex_1_4(arr):
    arr[0]['y'] = 30
    return arr


print(ex_1_4(z))


# Itera a través de una lista de diccionarios
print("\n")
print("2. Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada "
      "diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:")
students = [
         {'first_name':  'Michael', 'last_name': 'Jordan'},
         {'first_name': 'John', 'last_name': 'Rosales'},
         {'first_name': 'Mark', 'last_name': 'Guillen'},
         {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(some_list):
    for i in range(0, len(some_list)):
        print([key for key in some_list[i].keys()][0] + " - " + [value for value in some_list[i].values()][0] + ", "
              + [key for key in some_list[i].keys()][1] + " - " + [value for value in some_list[i].values()][1])


iterateDictionary(students)


# Obtén valores de una lista de diccionarios
print("\n")
print("3. Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre "
      "de clave, la función imprima el valor almacenado en esa clave para cada diccionario.")


def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])


# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
# Michael
# John
# Mark
# KB
iterateDictionary2('first_name', students)

# Y iterateDictionary2('last_name', students) debería generar:
# Jordan
# Rosales
# Guillen
# Tonel
iterateDictionary2('last_name', students)


# Itera a través de un diccionario con valores de listas
print("\n")
print("4. Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima "
      "el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la "
      "lista de cada clave.")


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, value in some_dict.items():
        size = len(some_dict[key])
        name = key.upper()
        print(size, name)
        for i in range(0, len(some_dict[key])):
            print(some_dict[key][i])
        print()


# Por ejemplo:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
#
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
printInfo(dojo)
