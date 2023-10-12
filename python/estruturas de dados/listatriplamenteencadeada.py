import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.upper = None

class TriplyLinkedList:
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

    def append_upper(self, data, base_data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == base_data:
                new_node.upper = current
                if current.upper:
                    current.upper.next = new_node
                current.upper = new_node
                return
            current = current.next

    def empty(self):
        self.head = None
        self.tail = None

    def fill_random(self, n):
        self.empty()
        for _ in range(n):
            elemento = random.randint(1, 100)  # Altere o intervalo conforme necessário
            self.append(elemento)

if __name__ == "__main__":
    triply_linked_list = TriplyLinkedList()

    while True:
        print("\nMenu:")
        print("1. Adicionar elemento")
        print("2. Inserir no início")
        print("3. Excluir elemento")
        print("4. Exibir lista (Forward)")
        print("5. Exibir lista (Backward)")
        print("6. Adicionar elemento na camada superior")
        print("7. Esvaziar lista")
        print("8. Preencher com elementos aleatórios")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            elemento = int(input("Digite o elemento a ser adicionado: "))
            triply_linked_list.append(elemento)
        elif escolha == "2":
            elemento = int(input("Digite o elemento a ser inserido no início: "))
            triply_linked_list.prepend(elemento)
        elif escolha == "3":
            elemento = int(input("Digite o elemento a ser excluído: "))
            triply_linked_list.delete(elemento)
        elif escolha == "4":
            triply_linked_list.display_forward()
        elif escolha == "5":
            triply_linked_list.display_backward()
        elif escolha == "6":
            elemento = int(input("Digite o elemento a ser adicionado na camada superior: "))
            base_data = int(input("Digite o elemento base na camada inferior: "))
            triply_linked_list.append_upper(elemento, base_data)
        elif escolha == "7":
            triply_linked_list.empty()
        elif escolha == "8":
            n = int(input("Digite a quantidade de elementos aleatórios a serem adicionados: "))
            triply_linked_list.fill_random(n)
        elif escolha == "9":
            break
        else:
            print("Escolha uma opção válida.")

    print("Programa encerrado.")
