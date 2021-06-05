# Básico : imprime todos los enteros del 0 al 150.
def ex1(init_num, final_num):
    print("---------------------")
    print("Executing exercise 1")
    print("---------------------")
    for i in range(init_num, final_num + 1):
        print(i)


# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
def ex2(init_num, final_num):
    print("\n\n")
    print("---------------------")
    print("Executing exercise 2")
    print("---------------------")
    for i in range(init_num, final_num + 1, 5):
        print(i)


# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar.
# Si es divisible por 10, imprima "Coding Dojo".
def ex3(init_num, final_num):
    print("\n\n")
    print("---------------------")
    print("Executing exercise 3")
    print("---------------------")
    for i in range(init_num, final_num + 1):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)


# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
def ex4(init_num, final_num):
    print("\n\n")
    print("---------------------")
    print("Executing exercise 4")
    print("---------------------")
    total = 0
    for i in range(init_num, final_num + 1):
        if i % 2 == 0:
            total += i

    print(total)


# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
def ex5(init_num, final_num):
    print("\n\n")
    print("---------------------")
    print("Executing exercise 5")
    print("---------------------")
    n = init_num
    while n > final_num:
        print(n)
        n -= 4


# Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum,
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle
# debe imprimir 3, 6, 9 (en líneas sucesivas)
def ex6(lowNum, highNum, mult):
    print("\n\n")
    print("---------------------")
    print("Executing exercise 6")
    print("---------------------")
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)


# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?
def ex7(init_num, final_num):
    print("\n\n")
    print("---------------------")
    print("Executing exercise 7")
    print("---------------------")
    no_prime_nums = []
    for i in range(2, final_num + 1):
        for j in range(2, final_num + 1):
            no_prime_nums.append(i * j)

    prime_nums = []
    for i in range(init_num, final_num + 1):
        if i not in no_prime_nums:
            prime_nums.append(i)
    print(prime_nums)
    print("or")
    print(prime_nums[1:])
    print("?")


ex1(0, 150)
ex2(5, 1000)
ex3(1, 100)
ex4(0, 500000)
ex5(2018, 0)
ex6(2, 9, 3)
ex7(1, 1000)
