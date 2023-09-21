import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

class BubbleSortTestCase:
    def __init__(self, name, arr, sorting_function):
        self.name = name
        self.arr = arr
        self.sorting_function = sorting_function

    def run(self):
        print(f"Caso de Teste: {self.name}")
        print("Array original:")
        print(self.arr)

        start_time = time.time()
        self.sorting_function(self.arr)  # Chama a função de ordenação fornecida
        end_time = time.time()

        print("Array ordenado:")
        print(self.arr)

        elapsed_time = end_time - start_time
        print(f"Tempo de ordenação: {elapsed_time:.6f} segundos")
        print("\n")

def main():
    # Caso de Teste 1: Array já ordenado em ordem crescente.
    test_case_1 = BubbleSortTestCase("Array Crescente", [1, 2, 3, 4, 5], bubble_sort)

    # Caso de Teste 2: Array já ordenado em ordem decrescente.
    test_case_2 = BubbleSortTestCase("Array Decrescente", [5, 4, 3, 2, 1], bubble_sort)

    # Caso de Teste 3: Array com elementos aleatórios.
    test_case_3 = BubbleSortTestCase("Array Aleatório", [7, 2, 4, 1, 8, 5, 3, 6], bubble_sort)

    # Caso de Teste 4: Array com elementos repetidos.
    test_case_4 = BubbleSortTestCase("Array com Repetição", [3, 2, 1, 2, 3, 1], bubble_sort)

    # Executar os casos de teste
    test_case_1.run()
    test_case_2.run()
    test_case_3.run()
    test_case_4.run()

if __name__ == "__main__":
    main()
