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

if __name__ == "__main__":
    pilha = Pilha()

    pilha.push(1)
    pilha.push(2)
    pilha.push(3)

    print("Elementos da pilha:")
    while not pilha.vazia():
        print(pilha.pop())

