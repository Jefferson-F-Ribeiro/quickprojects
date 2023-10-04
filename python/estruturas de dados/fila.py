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

if __name__ == "__main__":
    fila = Fila()

    fila.enfileirar(1)
    fila.enfileirar(2)
    fila.enfileirar(3)

    print("Elementos da fila:")
    while not fila.vazia():
        print(fila.desenfileirar())
