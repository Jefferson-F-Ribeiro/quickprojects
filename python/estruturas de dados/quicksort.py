import time

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

def main():
    # Caso de Teste 1: Array aleatório com 5 elementos.
    test_case_1 = QuickSortTestCase("Array Aleatório", [5, 2, 1, 4, 3])

    # Caso de Teste 2: Array crescente com 5 elementos.
    test_case_2 = QuickSortTestCase("Array Crescente", [1, 2, 3, 4, 5])

    # Caso de Teste 3: Array decrescente com 5 elementos.
    test_case_3 = QuickSortTestCase("Array Decrescente", [5, 4, 3, 2, 1])

    # Caso de Teste 4: Array com elementos repetidos com 5 elementos.
    test_case_4 = QuickSortTestCase("Array com Repetição", [3, 2, 1, 2, 3])

    # Executar os casos de teste
    test_case_1.run()
    test_case_2.run()
    test_case_3.run()
    test_case_4.run()

if __name__ == "__main__":
    main()
