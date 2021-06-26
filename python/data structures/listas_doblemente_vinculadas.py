class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_before(self, node, value):
        new_node = Node(value)
        new_node.next = node
        if node.prev is None:
            self.head = new_node
        else:
            new_node.prev = node.prev
            new_node.prev.next = new_node
        node.prev = new_node
        return self

    def insert_head(self, value):
        new_head = Node(value)
        if self.head is None:
            self.head = new_head
            self.tail = new_head
        # TODO: Complete

    def insert_after(self, node, value):
        new_node = Node(value)
        new_node.prev = node
        if node.next is None:
            self.tail = new_node
        else:
            new_node.next = node.next
            new_node.next.prev = new_node
        node.next = new_node
        return self

    def insert_tail(self, value):
        # TODO: Complete
        pass
