import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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
        insertion_sort(arr)
        end_time = time.time()

        print("Array ordenado:")
        print(arr)

        elapsed_time = end_time - start_time
        print(f"Tempo de ordenação: {elapsed_time:.6f} segundos")

    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
