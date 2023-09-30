class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Exemplo de uso:
if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)
    doubly_linked_list.append(4)
    doubly_linked_list.append(5)

    doubly_linked_list.display_forward()  # Saída: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None

    doubly_linked_list.prepend(0)
    doubly_linked_list.display_forward()  # Saída: 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None

    doubly_linked_list.delete(3)
    doubly_linked_list.display_forward()  # Saída: 0 <-> 1 <-> 2 <-> 4 <-> 5 <-> None

    doubly_linked_list.display_backward()  # Saída: 5 <-> 4 <-> 2 <-> 1 <-> 0 <-> None
