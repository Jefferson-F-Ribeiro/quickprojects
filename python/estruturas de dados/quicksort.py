import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

class QuickSortTestCase:
    def __init__(self, name, arr):
        self.name = name
        self.arr = arr

    def run(self):
        print(f"Caso de Teste: {self.name}")
        print("Array original:")
        print(self.arr)

        start_time = time.time()
        sorted_arr = quick_sort(self.arr)
        end_time = time.time()

        print("Array ordenado:")
        print(sorted_arr)

        elapsed_time = end_time - start_time
        print(f"Tempo de ordenação: {elapsed_time:.6f} segundos")
        print("\n")

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def main():
    # Caso de Teste 1: Array aleatório com 5 elementos.
    test_case_1 = QuickSortTestCase("Array Aleatório", [5, 2, 1, 4, 3])

    # Caso de Teste 2: Array crescente com 5 elementos.
    test_case_2 = QuickSortTestCase("Array Crescente", [1, 2, 3, 4, 5])

    # Caso de Teste 3: Array decrescente com 5 elementos.
    test_case_3 = QuickSortTestCase("Array Decrescente", [5, 4, 3, 2, 1])

    # Caso de Teste 4: Array com elementos repetidos com 5 elementos.
    test_case_4 = QuickSortTestCase("Array com Repetição", [3, 2, 1, 2, 3])

    # Caso de Teste 5: Array aleatório com 50 elementos.
    random_array_1 = generate_random_array(50)
    test_case_5 = QuickSortTestCase("Array Aleatório 50", random_array_1)

    # Caso de Teste 6: Array crescente com 50 elementos.
    test_case_6 = QuickSortTestCase("Array Crescente 50", list(range(1, 51)))

    # Caso de Teste 7: Array decrescente com 50 elementos.
    test_case_7 = QuickSortTestCase("Array Decrescente 50", list(range(50, 0, -1)))

    # Caso de Teste 8: Array com elementos repetidos com 50 elementos.
    repeated_array = [random.randint(1, 10) for _ in range(50)]
    test_case_8 = QuickSortTestCase("Array com Repetição 50", repeated_array)

    # Caso de Teste 9: Array aleatório com 100 elementos.
    random_array_1 = generate_random_array(100)
    test_case_9 = QuickSortTestCase("Array Aleatório 100", random_array_1)

    # Caso de Teste 10: Array crescente com 100 elementos.
    test_case_10 = QuickSortTestCase("Array Crescente 100", list(range(1, 101)))

    # Caso de Teste 11: Array decrescente com 100 elementos.
    test_case_11 = QuickSortTestCase("Array Decrescente 100", list(range(100, 0, -1)))

    # Caso de Teste 12: Array com elementos repetidos com 100 elementos.
    repeated_array = [random.randint(1, 10) for _ in range(100)]
    test_case_12 = QuickSortTestCase("Array com Repetição 100", repeated_array)


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


if __name__ == "__main__":
    main()
