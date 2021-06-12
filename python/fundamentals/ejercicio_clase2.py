# Ejercicio Propuesto

# Se necesita realizar una compra de productos en un local comercial
# Se debe imprimir un menu (definir el menu en una función)
# El menú de opciones tienes lo siguiente

# Menú

# 1. Ingrese el nombre y rut
# 2. De la lista de productos elija el elemento a comprar
# 3. Ingrese la cantidad de unidades a comprar
# 4. Imprimir en pantalla los datos de la compra
# Nombre: Juanito Perez
# Rut: 12345678-5
# Producto comprado: Bebida de 2Lt. # Definir la lista de productos
# Número de unidades: 3
# Precio por unidad: 1500 # Definir la lista de precio
# Precio total a pagar sin IVA: 4500
# Precio total a pagar con IVA: ???
def show_main_menu():
    print("-----------------------------------------------------")
    print("---------------------BIENVENIDO----------------------")
    print("-----------------------------------------------------")
    print("\nSeleccione la opción que quiere realizar:")
    print("1. Ingresar datos del cliente")
    print("2. Mostrar lista de productos")
    print("3. Ingresar cantidad de unidades")
    print("4. Mostrar resumen de compra")
    seleccion = input("Selección: ")

    if seleccion == "1":
        client = set_client_info()
    elif seleccion == "2":
        product = show_products()
    elif seleccion == "3":
        qty = set_qty(product)
    elif seleccion == "4":
        show_summary(client, product, qty)


def set_client_info():
    nombre = input("Nombre: ")
    rut = input("RUT: ")
    return {"nombre": nombre, "rut": rut}


def show_products():
    lista = [{"nombre": "Bebida de 2L.", "precio": 1500},
             {"nombre": "Papas fritas", "precio": 2300},
             {"nombre": "Helados", "precio": 1850},
             {"nombre": "Cabritas", "precio": 1500},
             {"nombre": "Limonada", "precio": 1800}]
    print("-----------------------------------------------------")
    print("---------------------PRODUCTOS-----------------------")
    print("-----------------------------------------------------\n")
    for i in range(len(lista)):
        print((i + 1) + ". " + lista[i]["nombre"] + "($" + lista[i]["precio"] + ")")

