class Fila:
    def __init__(self):
        self.items = []

    def vazia(self):
        return len(self.items) == 0

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.items.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def frente(self):
        if not self.vazia():
            return self.items[0]
        else:
            raise IndexError("A fila está vazia")

    def tamanho(self):
        return len(self.items)

    def imprimir(self):
        print("Elementos da fila:", self.items)

def exibir_menu():
    print("\nMenu:")
    print("1. Enfileirar (Adicionar elemento)")
    print("2. Desenfileirar (Remover elemento)")
    print("3. Frente (Consultar o elemento na frente)")
    print("4. Imprimir toda a fila")
    print("5. Sair")

if __name__ == "__main__":
    fila = Fila()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            elemento = input("Digite o elemento a ser enfileirado: ")
            fila.enfileirar(elemento)
            print(f"{elemento} foi enfileirado.")
        elif escolha == "2":
            if not fila.vazia():
                elemento_removido = fila.desenfileirar()
                print(f"{elemento_removido} foi removido da fila.")
            else:
                print("A fila está vazia.")
        elif escolha == "3":
            if not fila.vazia():
                elemento_frente = fila.frente()
                print(f"O elemento na frente da fila é: {elemento_frente}")
            else:
                print("A fila está vazia.")
        elif escolha == "4":
            fila.imprimir()
        elif escolha == "5":
            break
        else:
            print("Escolha uma opção válida.")

    print("Programa encerrado.")
