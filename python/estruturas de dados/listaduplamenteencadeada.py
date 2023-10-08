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

if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    while True:
        print("\nMenu:")
        print("1. Adicionar elemento")
        print("2. Inserir no início")
        print("3. Excluir elemento")
        print("4. Exibir lista (Forward)")
        print("5. Exibir lista (Backward)")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            elemento = int(input("Digite o elemento a ser adicionado: "))
            doubly_linked_list.append(elemento)
        elif escolha == "2":
            elemento = int(input("Digite o elemento a ser inserido no início: "))
            doubly_linked_list.prepend(elemento)
        elif escolha == "3":
            elemento = int(input("Digite o elemento a ser excluído: "))
            doubly_linked_list.delete(elemento)
        elif escolha == "4":
            doubly_linked_list.display_forward()
        elif escolha == "5":
            doubly_linked_list.display_backward()
        elif escolha == "6":
            break
        else:
            print("Escolha uma opção válida.")

    print("Programa encerrado.")
