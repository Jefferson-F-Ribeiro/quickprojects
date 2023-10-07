class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Adicionar elemento")
        print("2. Inserir no início")
        print("3. Excluir elemento")
        print("4. Exibir lista")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            elemento = int(input("Digite o elemento a ser adicionado: "))
            linked_list.append(elemento)
        elif escolha == "2":
            elemento = int(input("Digite o elemento a ser inserido no início: "))
            linked_list.prepend(elemento)
        elif escolha == "3":
            elemento = int(input("Digite o elemento a ser excluído: "))
            linked_list.delete(elemento)
        elif escolha == "4":
            linked_list.display()
        elif escolha == "5":
            break
        else:
            print("Escolha uma opção válida.")

    print("Programa encerrado.")
