import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    try:
        n = int(input("Digite o número de elementos no array: "))
        arr = []
        for i in range(n):
            element = int(input(f"Digite o elemento {i + 1}: "))
            arr.append(element)

        print("Array original:")
        print(arr)

        start_time = time.time()
        selection_sort(arr)
        end_time = time.time()

        print("Array ordenado:")
        print(arr)

        elapsed_time = end_time - start_time
        print(f"Tempo de ordenação: {elapsed_time:.6f} segundos")

    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
