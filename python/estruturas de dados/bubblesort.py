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
        bubble_sort(arr)
        end_time = time.time()

        print("Array ordenado:")
        print(arr)

        elapsed_time = end_time - start_time
        print(f"Tempo de ordenação: {elapsed_time:.6f} segundos")

    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
    