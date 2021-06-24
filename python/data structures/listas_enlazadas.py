class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)  # crea una instancia de la clase Node usando el valor dado
        current_head = self.head  # salva la cabecera actual en una variable
        new_node.next = current_head  # Coloca el proximo nodo en la lista de la cabecera actual
        self.head = new_node  # Coloca la lista de la cabecera al nodo que se creó en el paso anterior
        return self  # return self para permitir las cadenas

    def print_values(self):
        runner = self.head  # un puntero al primer nodo de la lista
        while runner is not None:
            print(runner.value)  # imprimir el valor del nodo actualcopy
            runner = runner.next  # Establecer el corredor a su vecino
        return self  # Una vez que el bucle está terminado, regrese a sí mismo para permitir el encadenamiento

    def add_to_back(self, val):  # acepta un valor
        if self.head is None:  # si la lista está vacia
            self.add_to_front(val)  # ejecuta el método add_to_front
            return self  # asegurémonos de que el resto de esta función no suceda si agregamos al frente

        new_node = SLNode(val)  # crea una nueva instancia de nuestra clase Node con el valor dado
        runner = self.head  # establece un iterador para que comience al principio de la lista
        while runner.next is not None:  # iterador hasta que el iterador no tenga un vecino
            runner = runner.next  # Incrementa el corredor al siguiente nodo de la lista.
        runner.next = new_node  # Incrementa el corredor al siguiente nodo de la lista.
        return self  # retorna self para permitir el encadenamiento

    # remove_from_front(self) - eliminar el primer nodo y devolver su valor
    def remove_from_front(self):
        if self.head is None:
            return self
        self.head = self.head.next
        return self

    # remove_from_back(self) - eliminar el último nodo y devolver su valor
    def remove_from_back(self):
        previous_runner = None
        if self.head is None:
            return self
        runner = self.head
        while runner.next is not None:
            previous_runner = runner
            runner = runner.next
        previous_runner.next = None
        return self

    # remove_val(self, val) - eliminar el primer nodo con el valor dado
    def remove_val(self, val):
        if self.head is None:
            return self
        runner = self.head  # un puntero al primer nodo de la lista
        previous_runner = None
        while runner is not None:
            if runner.value == val:
                if previous_runner is None:
                    self.remove_from_front()
                    return self
                previous_runner.next = runner.next
                return self
            previous_runner = runner
            runner = runner.next
        print("val not found")
        return self

    # insert_at(self, val, n) - insertar un nodo con valor val como el nº nodo en la lista
    def insert_at(self, val, n):
        if self.head is None:
            if n == 0:
                self.add_to_front(val)
            else:
                print("n is out of range")
            return self
        i = 0
        previous_runner = None
        runner = self.head
        while runner is not None:
            if i == n:
                new_node = SLNode(val)
                new_node.next = runner
                previous_runner.next = new_node
                return self
            previous_runner = runner
            runner = runner.next
            i += 1
        if i == n:
            new_node = SLNode(val)
            previous_runner.next = new_node
            return self
        print("n is out of range")
        return self


my_list = SList()  # crear una nueva instancia de una lista
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()  # encadenamiento, yeah!
# la salida deberia ser:
# Linked lists
# are
# fun!

# my_list.remove_from_front().print_values()
# my_list.remove_from_back().print_values()
# my_list.remove_val("Linked lists").print_values()
# my_list.remove_val("are").print_values()
# my_list.remove_val("fun!").print_values()
# my_list.insert_at("Hey, ", 0).print_values()
# my_list.insert_at("so ", 2).print_values()
# my_list.insert_at(":)", 3).print_values()
# SList().insert_at("Hello", 2).print_values()


