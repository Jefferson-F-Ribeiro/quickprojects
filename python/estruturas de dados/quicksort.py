import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

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
        sorted_arr = quick_sort(arr)
        end_time = time.time()

        print("Array ordenado:")
        print(sorted_arr)

        elapsed_time = end_time - start_time
        print(f"Tempo de ordenação: {elapsed_time:.6f} segundos")

    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
