# Utilice funciones para calcular lo siguiente
# Ingrese por pantalla 4 notas de un alumno (Pruebas)
# Calcule el promedio de notas de presentación a examen
# Solicite la nota del examen
# Calcule el promedio final de la nota de presentación y la nota del examen
# nota_final = nota_presentacion*0.7+examen*0.3
# Valide el rango de las notas entre (1-7)
# El alumno debe obtener en el examen al menos un 3.5 para aprobar el curso
# El aprueba con un promedio o nota final es mayor o igual a 3.95
# Imprima en pantalla el promedio y el estado del alumno ("Aprobado", "Reprobado")
def main():
    # Pedir notas parciales al usuario:
    notas_parciales = []
    while len(notas_parciales) < 4:
        nota_parcial = ingresar_nota_parcial()
        if validacion_nota(nota_parcial):
            notas_parciales.append(nota_parcial)
        else:
            print("Valor ingresado no corresponde a una nota válida")

    # Calcular nota de presentación a examen:
    nota_presentacion = calcular_nota_presentacion(notas_parciales)

    # Pedir nota de examen al usuario:
    nota_examen = ingresar_nota_examen()
    while not validacion_nota(nota_examen):
        print("Valor ingresado no corresponde a una nota válida")
        nota_examen = ingresar_nota_examen()

    # Calcular nota final
    promedio = nota_final(nota_presentacion, nota_examen)

    # Validar si aprobó
    if aprueba(nota_examen, nota_presentacion):
        print("El estudiante APROBÓ con promedio", promedio)
    else:
        print("El estudiante REPROBÓ con promedio", promedio)


# ------------------------------------- #
def ingresar_nota_parcial():
    return float(input("Nota parcial: "))


def calcular_nota_presentacion(arr):
    suma = 0
    for i in range(0, len(arr)):
        suma += arr[i]

    return suma / len(arr)


def ingresar_nota_examen():
    return float(input("Ingrese nota del examen: "))


def nota_final(nota_presentacion, nota_examen):
    return 0.7 * nota_presentacion + 0.3 * nota_examen


def validacion_nota(nota):
    if 1 <= nota <= 7:
        return True
    else:
        return False


def aprueba(nota_examen, nota_final):
    if nota_examen >= 3.5 and nota_final >= 3.95:
        return True
    else:
        return False


main()
