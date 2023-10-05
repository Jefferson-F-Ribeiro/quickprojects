class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.vazia():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        if not self.vazia():
            return self.items[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        return len(self.items)

    def imprimir(self):
        print("Elementos da pilha:", self.items)

def exibir_menu():
    print("\nMenu:")
    print("1. Push (Adicionar elemento)")
    print("2. Pop (Remover elemento)")
    print("3. Topo (Consultar o elemento no topo)")
    print("4. Imprimir toda a pilha")
    print("5. Sair")

if __name__ == "__main__":
    pilha = Pilha()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            elemento = input("Digite o elemento a ser adicionado: ")
            pilha.push(elemento)
            print(f"{elemento} foi adicionado à pilha.")
        elif escolha == "2":
            if not pilha.vazia():
                elemento_removido = pilha.pop()
                print(f"{elemento_removido} foi removido da pilha.")
            else:
                print("A pilha está vazia.")
        elif escolha == "3":
            if not pilha.vazia():
                elemento_topo = pilha.topo()
                print(f"O elemento no topo da pilha é: {elemento_topo}")
            else:
                print("A pilha está vazia.")
        elif escolha == "4":
            pilha.imprimir()
        elif escolha == "5":
            break
        else:
            print("Escolha uma opção válida.")

    print("Programa encerrado.")
