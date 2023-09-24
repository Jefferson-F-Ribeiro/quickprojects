import time
import random

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

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def main():
    # Caso de Teste 1: Array já ordenado em ordem crescente.
    test_case_1 = BubbleSortTestCase("Array Crescente", [1, 2, 3, 4, 5], bubble_sort)

    # Caso de Teste 2: Array já ordenado em ordem decrescente.
    test_case_2 = BubbleSortTestCase("Array Decrescente", [5, 4, 3, 2, 1], bubble_sort)

    # Caso de Teste 3: Array com elementos aleatórios.
    test_case_3 = BubbleSortTestCase("Array Aleatório", [7, 2, 4, 1, 8, 5, 3, 6], bubble_sort)

    # Caso de Teste 4: Array com elementos repetidos.
    test_case_4 = BubbleSortTestCase("Array com Repetição", [3, 2, 1, 2, 3, 1], bubble_sort)

    # Caso de Teste 5: Array já ordenado em ordem crescente (tamanho 50).
    test_case_5 = BubbleSortTestCase("Array Crescente 50", list(range(1, 51)), bubble_sort)

    # Caso de Teste 6: Array já ordenado em ordem decrescente (tamanho 50).
    test_case_6 = BubbleSortTestCase("Array Decrescente 50", list(range(50, 0, -1)), bubble_sort)

    # Caso de Teste 7: Array com elementos aleatórios (tamanho 50).
    random_array = generate_random_array(50)
    test_case_7 = BubbleSortTestCase("Array Aleatório 50", random_array, bubble_sort)

    # Caso de Teste 8: Array com elementos repetidos (tamanho 50).
    repeated_array = [random.randint(1, 10) for _ in range(50)]
    test_case_8 = BubbleSortTestCase("Array com Repetição 50", repeated_array, bubble_sort)

    # Caso de Teste 9: Array já ordenado em ordem crescente (tamanho 100).
    test_case_9 = BubbleSortTestCase("Array Crescente 100", list(range(1, 101)), bubble_sort)

    # Caso de Teste 10: Array já ordenado em ordem decrescente (tamanho 100).
    test_case_10 = BubbleSortTestCase("Array Decrescente 100", list(range(100, 0, -1)), bubble_sort)

    # Caso de Teste 11: Array com elementos aleatórios (tamanho 100).
    random_array = generate_random_array(100)
    test_case_11 = BubbleSortTestCase("Array Aleatório 100", random_array, bubble_sort)

    # Caso de Teste 12: Array com elementos repetidos (tamanho 100).
    repeated_array = [random.randint(1, 10) for _ in range(100)]
    test_case_12 = BubbleSortTestCase("Array com Repetição 100", repeated_array, bubble_sort)

    # Caso de Teste 13: Array já ordenado em ordem crescente (tamanho 500).
    test_case_13 = BubbleSortTestCase("Array Crescente 500", list(range(1, 501)), bubble_sort)

    # Caso de Teste 14: Array já ordenado em ordem decrescente (tamanho 500).
    test_case_14 = BubbleSortTestCase("Array Decrescente 500", list(range(500, 0, -1)), bubble_sort)

    # Caso de Teste 15: Array com elementos aleatórios (tamanho 500).
    random_array = generate_random_array(500)
    test_case_15 = BubbleSortTestCase("Array Aleatório 500", random_array, bubble_sort)

    # Caso de Teste 16: Array com elementos repetidos (tamanho 500).
    repeated_array = [random.randint(1, 10) for _ in range(500)]
    test_case_16 = BubbleSortTestCase("Array com Repetição 500", repeated_array, bubble_sort)



    # Executar os casos de teste
    test_case_1.run()
    test_case_2.run()
    test_case_3.run()
    test_case_4.run()
    test_case_5.run()
    test_case_6.run()
    test_case_7.run()
    test_case_8.run()
    test_case_9.run()
    test_case_10.run()
    test_case_11.run()
    test_case_12.run()
    test_case_13.run()
    test_case_14.run()
    test_case_15.run()
    test_case_16.run()

if __name__ == "__main__":
    main()
